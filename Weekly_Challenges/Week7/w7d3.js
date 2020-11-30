function combineArrays(arr1, arr2) {
    let arr3 = [];
    // your code here
    // a while loop 
    // min and max of math 
    // add console log to see the values 
    if (arr1.length < arr2.length){
        // var longarr = arr2
        // var shortarr = arr1
        for(var i =0; i <arr2.length; i ++){
            for(var j =0 ; j<(arr1.length + arr2.length); j++){
                mini = Math.min(arr2[i], arr1[j])
                console.log(mini)
                arr3.push(mini)
                arr3 = arr3.filter((item,index)=>{
                    return (arr3.indexOf(item) == index)
                })
            }
            // arr3.push(arr2[arr2.length-i-1])
        }
    } else{
        // var longarr = arr1
        // var shortarr = arr2
        for(var i =0; i <arr1.length; i ++){
            for(var j =0 ; j<(arr2.length + arr1.length); j++){
                mini = Math.min(arr1[i], arr2[j])
                console.log(mini)
                arr3.push(mini)
                arr3 = arr3.filter((item,index)=>{
                    return (arr3.indexOf(item) == index)
                })
            }
            // arr3.push(arr1[arr1.length-i-1])
        }
    }

    // while(i < longarr){
    //     // Math.min[]
    // }


    
    return arr3;
}

// console.log(combineArrays([2,5], [1,4,6,8]));
// console.log('------------------------------')
// console.log(combineArrays([2,5,7], [1,3,4]));
// this should result in [1, 2, 4, 5, 6, 8]

// if (arr1[i]> arr2[j]){
//     arr3.push(arr2[j])
//     // arr1.pop()
//     // arr3.push(arr2[j])
//     // arr2.pop()
// }  else {
//     arr3.push(arr1[i])
//     // arr3.push(arr1[i])
//     // arr2.pop()
// }

//will's solution!
function combine(a,b){
    const c =[]
    let [i,j] = [0,0]
    while(i<a.length && j <b.length)
        a[i] < b[j] ? c.push(a[i++]) : c.push(b[j++]);
    for(;i<a.length;i++)
        c.push(a[i])
    for(;j<b.length;j++)
        c.push(b[j])
    return c;
}

console.log(combine([2,5], [1,4,6,8]));
console.log('------------------------------')
console.log(combine([2,5,7], [1,3,4]));

function mergesort(arr){
    if(arr.length < 2){
        return arr
    }
    const left = mergesort(arr.slice(0,arr.length/2))
    const right = mergesort(arr.slice(arr.length/2), arr.length)
    console.log(left, right)
    return combine(left,right)
}
// console.log("merge:")
// console.log(mergesort([9,1,7,3,2,8,5,4,6]))