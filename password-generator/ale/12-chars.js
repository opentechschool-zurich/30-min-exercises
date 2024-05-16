// Create a 12 chars long random password, with no constraint
//
// https://stackoverflow.com/a/8084248/5239250
let password = (Math.random() + 1).toString(36).substring(6);
password += (Math.random() + 1).toString(36).substring(6);
console.log(password);
