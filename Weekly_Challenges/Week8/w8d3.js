function dedupe(str) {
    // your code here
    let newStr = "";
    let letter = str[0];


    newStr += letter
    for (var i = 1; i < str.length; i++) {
        letter = str[i]
        for (var j = 0; j < newStr.length; j++) {
            if (!newStr.includes(letter)) {
                newStr += letter
            }
        }
    }


    return newStr;
}

console.log(dedupe("hello world"));
console.log(dedupe("Snap, crackle and pop!"));
// should return something like "Snap, crkledo!"