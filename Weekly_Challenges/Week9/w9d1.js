// result.push(arr1.filter (x => arr2.includes(x))) // - why does this give me all the 2's ?

function intersect(arr1, arr2) {
    const result = [];
    // your code here
    if (arr1.length == 0 && arr2.length == 0) {
        return "arrays are empty"
    } else if (arr1.length == 0 && arr2.length > 0) {
        return arr2
    } else if (arr1.length > 0 && arr2.length == 0) {
        return arr1
    } else {
        while (arr1.length > 0 && arr2.length > 0) {
            if (arr1[0] < arr2[0]) {
                arr1.shift()
            } else if (arr1[0] > arr2[0]) {
                arr2.shift()
            } else {
                result.push(arr1.shift())
                result.push(arr1.shift())
                arr2.shift()
            }
        }
    }
    return result;
}

// console.log(intersect([1, 2, 2, 2, 7], [2, 2, 6, 6, 7]));
// this should return [2, 2, 7]


function union(arr1, arr2) {
    const result = [];
    // your code here
    if (arr1.length == 0 && arr2.length == 0) {
        return "arrays are empty"
    } else if (arr1.length == 0 && arr2.length > 0) {
        return arr2
    } else if (arr1.length > 0 && arr2.length == 0) {
        return arr1
    } else {
        while (arr1.length > 0 && arr2.length > 0) {
            if (arr1[0] < arr2[0]) {
                result.push(arr1.shift())
            } else if (arr1[0] > arr2[0]) {
                result.push(arr2.shift())
            } else {
                result.push(arr1.shift())
                arr2.shift()
            }
        }
    }


    return result;
}

// console.log(union([1, 2, 2, 2, 7], [2, 2, 6, 6, 7]));
console.log(union([], [2, 2, 6, 6, 7]));
  // this should return [1, 2, 2, 2, 6, 6, 7]