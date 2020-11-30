//Write a function called rotate that given a string and a positive whole number will rotate characters in the string by that number to the right.
function rotate(str, num) {
    let newStr = "";
    // your code here
    //end from str.length -num
    var end = (str.length) - num

    for (i = end; i < str.length; i++) {
        newStr += str[i]
        // console.log("1st: ", newStr ,'-', i)
    }
    for (let i = 0; i < end; i++) {
        newStr += str[i];
        // console.log(newStr)

    }
    return newStr;
}

console.log(rotate("Boris Godunov", 4));
// should return "novBoris Godu"
console.log(rotate("Bingo", 2));
console.log('--------------------------')


//Write a function called isRotation that given 2 strings will return true if they are rotations of each other
function isRotation(str1, str2) {
    let theyMatch = false;
    var newStr = ""
    // your code here
    if (str1.length != str2.length) {
        theyMatch = false;
    } else {
        for (var i = 0; i < str1.length; i++) {
            newStr = rotate(str1, i + 1)
            if(newStr == str2){
                theyMatch=true;
                break;
            }
        }
    }
    return theyMatch;
}

console.log(isRotation("Bingo", "goBin")); 
console.log(isRotation("Bingo", "oBing")); 
console.log(isRotation("Bingo", "Bingo")); 
// should return true
console.log(isRotation("Bingo", "gBin")); 
// should return false 
console.log(isRotation("Bingo", "ogniB")); 
  // should return false