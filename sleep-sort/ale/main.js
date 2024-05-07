const nums = [5,3,2,6,7];
for (const n of nums) {
  setTimeout(() => console.log(n), n * 200);
}
