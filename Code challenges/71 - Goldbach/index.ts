import prompts from "prompts";
import ora from "ora";

async function getUserNumber(): Promise<number> {
  return new Promise<number>((resolve, reject) => {
    prompts({
      type: "number",
      name: "value",
      message: "Enter number to find the sum of two primes for",
      validate: (value: number) =>
        value <= 2 || value % 2 === 1
          ? "Number must be > 2 and even."
          : !Number.isInteger(value)
          ? "Must be integer."
          : true,
    })
      .then((data) => resolve(data.value))
      .catch(reject);
  });
}

async function findPrimes(sum: number): Promise<[number, number]> {
  const LOWER_LIMIT = 2;
  const UPPER_LIMIT = sum - LOWER_LIMIT;

  if (UPPER_LIMIT < 2) {
    throw "Invalid user input. Number must be even and greater than 2.";
  }

  const arrayLength = UPPER_LIMIT - LOWER_LIMIT + 1;

  if (arrayLength >= 2 ** 32) {
    throw "Array length is greater than 2^32, which is the maximum for Javascript.";
  }

  // Create an array of required length
  let primeArray = [...Array(arrayLength)];
  // Set every number to range from lower limit to upper limit
  primeArray = primeArray.fill(true);

  // Use prime sieve
  // @see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  let p = 2;
  let index = 0;

  while (p ** 2 < UPPER_LIMIT) {
    // Remove items that are > p and are multiples of p
    primeArray.forEach((_, i) => {
      if (i + LOWER_LIMIT > p && (i + LOWER_LIMIT) % p === 0) {
        primeArray[i] = false;
      }
    });

    index = primeArray.findIndex((isPrime, i) => i > index && isPrime);
    p = index + LOWER_LIMIT;
  }

  const resultsArray: number[] = [];

  primeArray.forEach((isPrime, i) => {
    if (isPrime) {
      resultsArray.push(i + LOWER_LIMIT);
    }
  });

  /**
   * FIND ANY PRIME THAT MAKES `sum` WHEN DOUBLED.
   */

  const double = resultsArray.find((x) => x === sum / 2);

  if (double) {
    return [double, double];
  }

  /**
   * FIND TWO PRIMES THAT SUM TO `sum`.
   */

  let frontIndex = 0;
  let rearIndex = resultsArray.length - 1;

  while (frontIndex < rearIndex) {
    let fPrime = resultsArray[frontIndex];
    let rPrime = resultsArray[rearIndex];

    if (fPrime + rPrime > sum) {
      rearIndex--;
      continue;
    } else if (fPrime + rPrime < sum) {
      frontIndex++;
    } else {
      return [fPrime, rPrime];
    }
  }

  return [0, 0];
}

async function main() {
  const number = await getUserNumber();

  const spinner = ora("Calculating two primes...").start();

  const primes = findPrimes(number);

  const res = await primes;
  spinner.stop();

  console.log(`\nWe found two primes that sum to ${number}:`);
  console.log(`${res[0]} and ${res[1]}`);
}

main();
