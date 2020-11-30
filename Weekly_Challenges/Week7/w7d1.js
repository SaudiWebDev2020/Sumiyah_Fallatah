function bubbleSort(arr) {
    for(let i=0; i<arr.length; i++) {
        let inOrder = true;
        for(let j=0; j<arr.length-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                inOrder = false;
            }
        }
        if(inOrder) {
            return arr;
        }
    }
    return arr;
}
console.log(bubbleSort([1,2,3,4,5]));
///////////////////////////////////

function bubbleSort(arr){
    for (var i = 0 ; i < arr.length-1; i ++){
        for (var j = 0 ; j < arr.length-i-1; j++){
            if (arr[j] > arr[j+1]){
                var temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    return arr
}
console.log('bubble  :', bubbleSort([1,2,3,4,5]));
console.log('bubble  :', bubbleSort([4,2,1,5,3]));

//////////////////////////////////

function selectionSort(arr){
    for(var i = 0; i < arr.length-1; i++){
        var min = i
        for (var j = i+1; j <arr.length; j++){
            if(arr[j] < arr[min]){
                min = j
            }
        }
    var temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp
    }
    return arr
}

console.log('selection  :', selectionSort([1,2,3,6,9,8,7,1,4,5]));
console.log('selection  :', selectionSort([4,2,1,5,3,3,3,3,2,0,8,4]));