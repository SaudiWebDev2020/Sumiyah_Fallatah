// Radix Sorting 
// sort ones then tens then hundereds and so on.. 
// Non comparing sorting algorithm

//find max in array 
function Max(arr){
    max = arr[0]
    for(var i = 1 ; i < arr.length; i ++){
        if (arr[i] > max){
            max = arr[i]
        }
    }
    console.log("max in array is: ", max)
    return max
}

function Radix(arr){
    max = Max(arr)
    maxLength = max.toString().length
    console.log('length of max is: ' ,maxLength)
    return arr
}

console.log(Radix([9,15,73,104,52,1,195,81]))