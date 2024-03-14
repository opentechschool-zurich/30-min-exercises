function primes(n) {
  let numbers = Array(n);
    
  numbers.fill(true);
  numbers[0] = false;
  numbers[1] = false;

  for (let i = 3; i < Math.sqrt(n); i += 2) {

    if (numbers[i] === true) {
      for (let j = i * 2; j < n; j += i) {
        numbers[j] = false;
      }
    }
  }


  let primes = [2];
  for (i = 3; i < n; i += 2) {
    if (numbers[i]) {
      primes.push(i);
    }
  }

  return primes;
}

console.log(primes(100))
