import prompts from "prompts";
import ora from "ora";

async function getUserNumber(): Promise<number> {
  return new Promise<number>((resolve, reject) => {
    prompts({
      type: "number",
      name: "value",
      message: "Enter number to find prime factors of",
      validate: (value: number) =>
        value < 2
          ? "Number must be > 1."
          : !Number.isInteger(value)
          ? "Must be integer."
          : true,
    })
      .then((data) => resolve(data.value))
      .catch(reject);
  });
}

/**
 * Finds an array of prime numbers up to a specified limit.
 */
async function findPrimesUpToMax(limit: number): Promise<number[]> {
  if (limit < 2) {
    throw "Input must be > 1";
  }

  // Account for starting at 2
  const arrayLength = limit - 1;

  if (arrayLength >= 2 ** 32) {
    throw "Array length is greater than 2^32, which is the maximum for Javascript.";
  }

  // Create an array of required length
  let primeArray = [...Array(arrayLength)];
  // Set every number to range from lower limit to upper limit
  primeArray = primeArray.fill(true);

  // Use prime sieve
  // @see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  const startingNum = 2;
  let p = 2;
  let index = 0;

  while (p ** 2 < limit) {
    // Remove items that are > p and are multiples of p
    primeArray.forEach((_, i) => {
      if (i + startingNum > p && (i + startingNum) % p === 0) {
        primeArray[i] = false;
      }
    });

    index = primeArray.findIndex((isPrime, i) => i > index && isPrime);
    p = index + startingNum;
  }

  const resultsArray: number[] = [];

  primeArray.forEach((isPrime, i) => {
    if (isPrime) {
      resultsArray.push(i + startingNum);
    }
  });

  return resultsArray;
}

/**
 * Finds the factors in a given array that multiply to create a given result.
 *
 * @param result Total that the factors should multiply to create
 * @param primes Array of primes in ascending order
 *
 * @returns JS Object where the keys map to the factors, and the values at those keys specify the count of the respective factor.
 *
 * @example
 * performFactorisation(4, [2, 3]);
 * // returns { 2: 2 }
 * // equates to... (2^2)
 *
 * @example
 * performFactorisation(24, [2, 3]);
 * // returns {2: 3, 3: 1 }
 * // equates to... (2^3) * 3
 */
async function performFactorisation(
  result: number,
  primes: number[]
): Promise<Record<number, number>> {
  // Sort possible factors to be in descending order
  const descPrimes = primes.sort((a, b) => b - a);

  let currentValue = result;
  const factors: Record<number, number> = {};

  while (currentValue !== 1) {
    // .some() so that we stop iterating over possible factors
    // after we have found one
    const found = descPrimes.some((possibleFactor) => {
      if (currentValue % possibleFactor === 0) {
        if (!factors[possibleFactor]) {
          factors[possibleFactor] = 0;
        }

        factors[possibleFactor] += 1;
        currentValue /= possibleFactor;
        return true;
      }

      return false;
    });

    if (!found) {
      // We didn't find a factor. This should be impossible, but we don't
      // want to have an infinite loop, just in case.
      throw `Couldn't find factor of ${currentValue} in the list of possible factors!`;
    }
  }

  return factors;
}

async function main() {
  const number = await getUserNumber();
  let spinner: ora.Ora;

  spinner = ora("Finding primes up to and including your number...").start();

  const primesPromise = findPrimesUpToMax(number);
  const possiblePrimes = await primesPromise;
  spinner.stopAndPersist();

  spinner = ora("Finding prime factors...").start();
  const factorsPromise = performFactorisation(number, possiblePrimes);
  const factors = await factorsPromise;
  spinner.stopAndPersist();

  console.log(`The prime factorisation of ${number} is:`);

  let factorisationStr = "";
  Object.keys(factors).forEach((_factor) => {
    const factor = parseInt(_factor);

    factorisationStr += `(${factor} ^ ${factors[factor]}) * `;
  });
  // Trim off last " * "
  factorisationStr = factorisationStr.substring(0, factorisationStr.length - 3);

  console.log(factorisationStr);
}

main();
