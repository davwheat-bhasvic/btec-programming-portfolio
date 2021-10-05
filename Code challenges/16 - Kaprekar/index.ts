import prompts from "prompts";
import ora from "ora";

async function getUserNumber(): Promise<number> {
  return new Promise<number>((resolve, reject) => {
    prompts({
      type: "number",
      name: "value",
      message: "Enter number to check",
      validate: (value: number) =>
        value < 2
          ? "Number must be >= 1."
          : !Number.isInteger(value)
          ? "Must be integer."
          : true,
    })
      .then((data) => resolve(data.value))
      .catch(reject);
  });
}

function getDigits(num: number) {
  if (num === 0) return [0];

  let val = num;
  const digits: number[] = [];

  while (val !== 0) {
    const remainder = val % 10;

    val -= remainder;
    val /= 10;

    digits.unshift(remainder);
  }

  return digits;
}

function createArray(length: number) {
  return [...new Array(length)];
}

async function main() {
  const number = await getUserNumber();
  let spinner: ora.Ora;

  spinner = ora("Squaring n-digit number...").start();
  const square = number ** 2;
  spinner.stopAndPersist();

  spinner = ora("Splitting square into its digits...").start();
  const squareDigits = getDigits(square);
  spinner.stopAndPersist();

  spinner = ora("Summing n digits on right and n-1 digits on left...").start();

  const digitCount = squareDigits.length;
  const digitsLeft = Math.floor(digitCount / 2);
  const digitsRight = Math.ceil(digitCount / 2);

  const leftNum = createArray(digitsLeft).reduce(
    (prev, curr, i) => prev + squareDigits[i] * 10 ** (digitsLeft - i - 1),
    0
  );

  const rightNum = createArray(digitsRight).reduce(
    (prev, curr, i) =>
      prev + squareDigits[digitsLeft + i] * 10 ** (digitsRight - i - 1),
    0
  );

  const digitsSum = leftNum + rightNum;

  spinner.stopAndPersist();

  if (digitsSum === number) {
    console.log(`${number} is a Kaprekar number.`);
  } else {
    console.log(`${number} is not a Kaprekar number.`);
  }
}

main();
