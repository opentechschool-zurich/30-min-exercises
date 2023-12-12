function moveZeros(arr) {
  let countzeros = 0; 
  for (i = 0; i < (arr.length); i++) {
    if (arr[i] === 0) {
       countzeros++;
    } else {
      arr[i-countzeros] = arr[i];
    }
  }
  for (i = 0; i<countzeros; i++) {
    arr[arr.length -1 - i] = 0;
  }
  return arr;
}

zip = rows=>rows[0].map((_,c)=>rows.map(row=>row[c]))

console.assert(zip([moveZeros([false,1,0,1,2,0,1,3,"a"]), [false,1,1,2,1,3,"a",0,0]]).reduce((acc, [x, y]) => acc && x == y, true));
