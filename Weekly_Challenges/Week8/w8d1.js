function strToWordArr(str) {
    str+=" ";
    const words = [];
    var newStr = "";
    // your code here
    for (let i = 0; i < str.length; i++) {
        if (str[i] != " ") {
            newStr += str[i];
        } else if (str[i] == " ") {
            words.push(newStr);
            newStr = "";
        }
    }
    if (newStr!="") {
        words.push(newStr);
    }
    console.log(newStr);
    return words;
}

console.log(strToWordArr("Hello world and good morning!"));
// should return ["Hello", "world", "and", "good", "morining!"]

function reverseWords(str) {
    reversed = "";
    strArr = strToWordArr(str);
    // your code here
    for (let i = strArr.length - 1; i >= 0; i--) {
        reversed+=strArr[i]+" ";
    }
    return reversed;
}

console.log(reverseWords("Hello world and good morning!"));
// should return "morning! good and world Hello";