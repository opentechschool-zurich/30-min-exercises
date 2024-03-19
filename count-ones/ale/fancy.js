const countOnes = (number) => {
  let count = 0;
  while (number > 0) {
    count += number & 1; // is the last bit a 1
    number >>= 1; // shift by 1
    // number /= 2; // remove the last bit (... it's a power of two)
  }
  return count;
}

console.log(countOnes(11))
