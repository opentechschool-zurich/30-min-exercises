# Implement a calculator

A calculator can be

- prefix: `+ 3 2`
- infix: `3 + 2`
- postfix: `3 2 +`

## Reverse Polish Notation (RPN, postfix)

Probably, the easiest way to implement a calculator is to use a postfix notation.

_For humans_, it's a rather unusual way to express a calculation, but it's rather easy to manage for a computer and for a programmer.

- https://en.wikipedia.org/wiki/Reverse_Polish_notation

## Introduction to a new language with the Calculator

### First steps

- 3 2 +
- Input as list of strings
- if "+" it's the operator otherwise convert to integer
- Do the calculation
. Output the result

### More complexity

- Calculate: 3 2 + 5 *

### Third step

- Input from a string

### Support all possible basic operators and unlimited tokens
