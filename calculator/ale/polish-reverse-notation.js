// - The expression is evaluated from left to right.
// - Push the values (normally two of them, or as many as the operator needs) on the stack the
//   operator is encountered, perform the calculation and replace the values from the list
//   with the result.

/**
 * A very simplistic function, that only correctly process very simple cases
 */
function calculate_simple(calculation) {
  while (calculation.length > 1) {
    calculation.splice(0, 3, calculation[2](calculation[0], calculation[1]));
  }
  return calculation[0];
}

/**
 * Perform a postfix from a list of values and operators
 */
function calculate(calculation) {
  let operands = [];
  while (calculation.length > 1) {
    let operand = calculation.shift();
    while (!(operand instanceof Function)) {
      operands.push(operand);
      operand = calculation.shift();
    }
    let [a, b] = operands.splice(-2, 2);
    calculation.unshift(operand(a, b));
  }
  return calculation[0];
}

/**
 * Convert a post fix calculation string into tokens: numebrs and operator functions
 */
function tokenize(calculation, operators) {
  tokens = [];
  digits = ''
  for (const c of calculation) {
    if (c >= '0' && c <= '9') {
      digits += c;
      continue;
    }
    if (digits.length > 0) {
      tokens.push(Number(digits));
      digits = ''
    }
    if (c == ' ') {
      continue;
    }
    if (operators.hasOwnProperty(c)) {
      tokens.push(operators[c])
    }
    // invalid character: ignore it
  }
  return tokens;
}

sum = (a, b) => a + b
mul = (a, b) => a * b
sub = (a, b) => a - b
div = (a, b) => a / b

console.assert(calculate_simple([3, 2, sum, 4, mul]) == 20);

console.assert(calculate([3, 2, sum, 4, mul]) == 20);
console.assert(calculate([3, 4, sum, 5, 6, sum, mul]) == 77);

let operators = {
  '+': sum,
  '-': sub,
  '*': mul,
  '/': div,
}

console.assert(calculate(tokenize('3 4 + 5 6 + *', operators)) == 77);
