// Arrs2Map
// ----------------------------------------------------------------------------------------------------------------
// Given two arrays, create an associative array (map) containing keys of the first, and values of the
// second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc":
// 42, 3: "wassup", "yo": true}.

var originalData = ["abc", 3, "yo"];
var newData = [42, "wassup", true];

var newOrderObject = originalData.reduce(function(obj, key, index) {
obj[key] = newData[index];
return obj;
}, {});

console.log(newOrderObject);

// InvertHash
// ----------------------------------------------------------------------------------------------------------------
// Create invertHash(assocArr) that converts a hash’s keys to values and values to corresponding keys.
// Example: given {"name": "Zaphod"; "numHeads": 2}, return {"Zaphod": "name"; 2:
// "numHeads"}. You will need to learn and use a JavaScript for ... in h ere!
var objHash = {
    "name": "Zaphod",
    "numHeads": 2 
}, 
new_obj = {};

for (const x in objHash) {
    
        new_obj[objHash[x]] = x;
        // const element = object[key];
        
    
}
console.log(new_obj);

// ReverseString
// ----------------------------------------------------------------------------------------------------------------
// Implement a function reverseString(str) that, given a string, will return the string of the same length but
// with characters reversed. Example: given "creature", return "erutaerc". Do not use the built-in
// reverse() function!

function reverseString(str) {
    // Step 1. Use the split() method to return a new array
    var splitString = str.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]

    // Step 2. Use the reverse() method to reverse the new created array
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]

    // Step 3. Use the join() method to join all elements of the array into a string
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"
    
    //Step 4. Return the reversed string
    return joinArray; // "olleh"
}

concole.log(reverseString("hello"));

function Arrs2Map (arr1 , arr2){
    var obj ={};
    for(var i=0 ; i< arr1.length ; i++){
        obj[arr1[i]]= arr2[i];

    }
return obj;
}

console.log(Arrs2Map(["abc" , 3 ,"yo"] , [42 , "wassap" , true]));