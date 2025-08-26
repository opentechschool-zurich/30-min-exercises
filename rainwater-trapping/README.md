Given an array arr[] of size n consisting of non-negative integers, where each element represents the height of a bar in an elevation map and the width of each bar is 1, determine the total amount of water that can be trapped between the bars after it rains.

[3, 0, 1, 0, 4, 0, 2] -> 10

```
x = wall
. = water
― = floor

      x          x  
  x   x      x...x  
  x   x x -> x...x.x = 10
  x x x x    x.x.x.x
  ―――――――    ―――――――
```

[3, 0, 2, 0, 4] -> 7

[1, 2, 3, 4] -> 0
