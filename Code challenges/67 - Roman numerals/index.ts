import prompts from "prompts";

async function getNumber(): Promise<number> {
  return new Promise<number>((resolve, reject) => {
    prompts({
      type: "number",
      name: "value",
      message: "Enter number to convert",
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

async function main() {
  const num = await getNumber();

  console.log(getRomanNumerals(num));

  main();
}

function getRomanNumerals(num: number) {
  let numerals = "";

  {
    const [newNum, newNumeral] = handleThousands(num);
    num = newNum;
    numerals += newNumeral;
  }

  {
    const [newNum, newNumeral] = handleHundreds(num);
    num = newNum;
    numerals += newNumeral;
  }

  {
    const [newNum, newNumeral] = handleTens(num);
    num = newNum;
    numerals += newNumeral;
  }

  {
    const [newNum, newNumeral] = handleUnits(num);
    num = newNum;
    numerals += newNumeral;
  }

  return numerals;
}

function handleThousands(num: number): [number, string] {
  let numeral = "";

  while (num >= 1000) {
    num -= 1000;
    numeral += "M";
  }

  return [num, numeral];
}

function handleHundreds(num: number): [number, string] {
  let numeral = "";

  // num is less than 1000

  if (num >= 900) {
    numeral += "CM"; // 900
    num -= 900;
  } else if (num >= 500) {
    num -= 500;
    numeral += "D"; // 500
  } else if (num >= 400) {
    num -= 400;
    numeral += "CD"; // 400
  }

  while (num >= 100) {
    num -= 100;
    numeral += "C"; // 100
  }

  return [num, numeral];
}

function handleTens(num: number): [number, string] {
  let numeral = "";

  // num is less than 100

  if (num >= 90) {
    numeral += "XC"; // 90
    num -= 90;
  } else if (num >= 50) {
    num -= 50;
    numeral += "L"; // 50
  } else if (num >= 40) {
    num -= 40;
    numeral += "XL"; // 40
  }

  while (num >= 10) {
    num -= 10;
    numeral += "X"; // 10
  }

  return [num, numeral];
}

function handleUnits(num: number): [number, string] {
  let numeral = "";

  // num is less than 10

  if (num === 9) {
    numeral += "IX"; // 9
    num -= 90;
  } else if (num >= 5) {
    num -= 5;
    numeral += "V"; // 5
  } else if (num === 4) {
    num -= 4;
    numeral += "IV"; // 4
  }

  while (num >= 1) {
    num--;
    numeral += "I"; // 1
  }

  return [num, numeral];
}

main();
