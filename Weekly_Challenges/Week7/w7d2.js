function insertionSort(arr) {
    // your code here
    for (var i = 0; i < arr.length; i ++){
        var value = arr[i]
        for ( var j = i-1; j >=0 && arr[j] > value ; j --){
            arr[j+1] = arr[j]
            // console.log(j, " j :", arr)
        }
        // console.log(i, " i1 :", arr)
        arr[j+1] = value
        // console.log(i, " i2 :", arr)
    }
    return arr;
}

console.log(insertionSort([3,2,5,4,1]));
console.log(insertionSort([10,224,53,24,15]));