# Count the digits in a number

Some insights: <https://jstrieb.github.io/posts/digit-length/>

Comments from Hacker News:

- <https://news.ycombinator.com/item?id=21500434>
- <https://news.ycombinator.com/item?id=40581746>
- It's very strange to me that the teacher would push the students from the correct solution using a loop, towards an incorrect solution using a logarithm. A logarithm could work in a language like C where ints can't get too large, but Python has arbitrary precision integers so any solution using floating point numbers is doomed. For example, the code given in the post returns 16 instead of 15 for 999_999_999_999_999.
- I would prefer a solution based on multiplication than division.  
  If the number is less than 10, return one, otherwise is it less than 100, ...
  You should prefer the simplest tool that can do the job. Multiplication is simpler than division. You could digress about floating point errors (Python has infinite-precision integers, but not infinite- precision floats) or performance (division may be in some contexts meaningfully slower) but those are just digressions, the important thing is that it's more complicated.
- In the final log10 version, can't you just solve both problems at once by adding 1 to the input?  
  `math.ceil(math.log10(x+1))`  
  -> probably not.
- instead of math.log10() use np.log10() and also Decimal() for tasks involving precise number crunching.  
  ```py
  def digit_length_clever_2(n):
      if n ==0:
          return 1
      else:
          return math.floor((np.log10(Decimal(n)))) + 1
  ```
- `len(str(x))` or, better `len(str(int(x)))` to strip leading zeros.
  - negative values?
  - python's implementation of `round` uses the conversion to strings:< https://github.com/python/cpython/blob/main/Objects/floatobject.c#L965-L972>


## Variants

- The number of digits in a range of numbers:
  - <https://stackoverflow.com/a/68910571/5239250>
