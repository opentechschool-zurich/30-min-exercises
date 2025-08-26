function get_water_quantity(blocks) {
  if (blocks.length < 3) {
    return 0;
  }
  let volume = 0;
  let max_height = 0;
  let max_i = 0;
  for (let i = 1; i < blocks.length; i++) {
    if (blocks[0] <= blocks[i]) {
      max_i = i;
      max_height = blocks[i];
      break;
    } else if (blocks[i] >= max_height) {
      max_height = blocks[i];
      max_i = i;
    }
  }
  let rain_height = Math.min(blocks[0], blocks[max_i]);
  console.log(rain_height, max_i);
  for (let i = 0; i < max_i; i++) {
    volume += Math.max(0, rain_height - blocks[i]);
  }
  console.log(volume);
  return 0;
}

console.log(get_water_quantity( [3, 0, 1, 0, 4, 0, 2]) == 10);
// console.log(get_water_quantity( [3, 0, 2, 0, 4]) == 7);
// console.log(get_water_quantity( [1, 2, 3, 4]) == 0);
