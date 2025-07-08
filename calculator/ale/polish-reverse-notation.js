// - The expression is evaluated from left to right.
// - Push the values (normally two of them, or as many as the operator needs) on the stack the
//   operator is encountered, perform the calculation and replace the values from the list
//   with the result.

sum = (a, b) => a + b
mul = (a, b) => a * b
sub = (a, b) => a - b
div = (a, b) => a / b

calculation = [3, 2, sum, 4, mul]

while (calculation.length > 1) {
  calculation.splice(0, 3, calculation[2](calculation[0], calculation[1]))
}

console.log(calculation[0])
