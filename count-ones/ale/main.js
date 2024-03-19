function countOnes(binary) {
    let count = 0;
    for (let i = 0; i < binary.length; i++) {
        // console.log(i, binary[i]); // there are 32 characters: 0..31
        if (binary[i] === '1') {
            // it's a good one
            count = count + 1;
        }
    }
    return count;
}

// let number = 83;
let binary = '00000000000000000000000010000000';
	
console.log(countOnes(binary));
