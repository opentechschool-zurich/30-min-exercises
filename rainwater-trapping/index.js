function get_water_quantity(blocks) {
  if (blocks.length < 3) {
    return 0;
  }
  let volume = 0;
  let max_i = 0;
  
  while (max_i < blocks.length - 1) {
    let max_height = 0;
    start_i = max_i
    
    for (let i = start_i + 1; i < blocks.length; i++) {
      if (blocks[start_i] < blocks[i]) {
        max_i = i;
        max_height = blocks[i];
        break;
      } else if (blocks[i] >= max_height) {
        max_height = blocks[i];
        max_i = i;
      }
    }
    let rain_height = Math.min(blocks[start_i], blocks[max_i]);
    // console.log(rain_height, max_i);
    for (let i = start_i; i < max_i; i++) {
      volume += Math.max(0, rain_height - blocks[i]);
    }

    // console.log(volume);
    
  }

  return volume;
}

console.assert(get_water_quantity([3, 0, 1, 0, 4, 0, 2]) == 10);
console.assert(get_water_quantity( [3, 0, 2, 0, 4]) == 7);
console.assert(get_water_quantity( [1, 2, 3, 4]) == 0);
console.assert(get_water_quantity( [4, 3, 2, 1]) == 0);
console.assert(get_water_quantity( [4, 0, 4, 0, 4]) == 8);
console.assert(get_water_quantity( [4, 0, 4, 0, 0]) == 4);
console.assert(get_water_quantity( [0, 0, 0, 0, 1]) == 0);
console.assert(get_water_quantity( [1, 0, 0, 0, 0]) == 0);

// https://www.geeksforgeeks.org/dsa/trapping-rain-water/
