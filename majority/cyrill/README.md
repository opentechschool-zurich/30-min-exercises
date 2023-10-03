# Majority

## Desk Calculator

To run this implementation you need `dc`
(https://en.wikipedia.org/wiki/Dc_(computer_program)).

The script stores `m` in register `m` and `i` on the stack. Register `b` is used
to save temporary blocks of code. Register `_` is used to discard values, which
are no longer needed.

You can find the meaning of all commands here:
https://www.unix.com/man-page/linux/1/dc/

## Haskell

One way to run the Haskell implementation is to use GHCi. You can load the code
using `:load boyer-moore` and execute the `majority` function like this:

```haskell
majority $ 1 :| [1, 2, 1, 3, 1]
```
