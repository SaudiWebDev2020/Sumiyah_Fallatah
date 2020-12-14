function bin2dec(str) {
  let res = 0;
  let power = 0;
  // your code here
  if((str[0] === '0' ) && (str[1]==='b')){
    for(var i = str.length-1 ; i > 1; i--){
      if(str[i] ==='1'){
        // console.log("2^power: ",Math.pow(2,power))
        res += (Math.pow(2,power))
        power ++
        // console.log("res is: ", res)
      } else {
        power++
      }
    }


    return res;
  } else {
    return `The number you gave -${str}- is not binary`
  }
}
console.log(bin2dec("0b1101"));
// this should return 13
console.log(bin2dec("0b11101"));
// this should return 29
console.log(bin2dec("11101"));