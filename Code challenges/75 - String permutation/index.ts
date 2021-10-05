import prompts from "prompts";

async function getString(name: string): Promise<string> {
  return new Promise<string>((resolve, reject) => {
    prompts({
      type: "text",
      name: "value",
      message: `Enter string ${name}`,
      validate: (str: string) =>
        str.length > 0 ? true : "Please enter a string",
    })
      .then((data) => resolve(data.value))
      .catch(reject);
  });
}

async function main() {
  const stringX = await getString("X");
  const stringY = await getString("Y");

  const perm = findLongestPermutation(stringX, stringY);

  console.log(`Longest permutation is ${perm}`);
}

function findLongestPermutation(x: string, y: string): string {
  let longestPermutation = "";

  // Array of chars in the string `x`
  let xArr = [...x];

  /**
   * Updates the longest permutation variable if the provided string is longer
   * than the currently stored one.
   *
   * @param newPerm New permutation
   */
  const updatePermutation = (newPerm: string) => {
    if (longestPermutation.length < newPerm.length)
      longestPermutation = newPerm;
  };

  xArr.forEach((xChar, xIndex) => {
    let currentPermutation = xChar;
    let index = xIndex;

    while (y.includes(currentPermutation)) {
      // Let's look at the next char in this current permutation
      index++;
      updatePermutation(currentPermutation);

      if (index <= x.length - 1) {
        // Add the next char to the permutation and loop again
        currentPermutation += xArr[index];
      } else {
        // If we reached the end of the string, we're done
        break;
      }
    }
  });

  return longestPermutation;
}

main();
