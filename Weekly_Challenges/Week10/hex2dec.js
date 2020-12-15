const hexValues = {
  '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'a': 10,
  'b': 11,
  'c': 12,
  'd': 13,
  'e': 14,
  'f': 15
}
// some value ommitted

function hex2dec(str) {
  let res = 0;
  let power = 0 
  // your code here
  if ((str[0] === '0') && (str[1] === 'x')) {
    for(var i = str.length-1 ; i > 1; i--){
          res += (Math.pow(16,power) * hexValues[str[i]])
          power++
        
      
    }
    return res;
  } else {
    return `The number you gave - ${str} - is not hexadecimal`
  }
}
console.log(hex2dec('0x3a'));
// expect something like 58 back
console.log(hex2dec('0x23a'));
// expect something like 570 back
console.log(hex2dec('0x1000'));
console.log(hex2dec('0x1504aef'));
// expect something like 22039279 back
console.log(hex2dec('3a'));

