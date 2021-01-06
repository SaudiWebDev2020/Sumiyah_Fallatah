// function allCombinations(words) {
//     const combinations = [];
//     // your code here
//     return combinations;
// }

// const words = [["quick", "lazy"],
// ["brown", "red", "grey"],
// ["fox", "dog"]];

// console.log(allCombinations(words));
// should return ["quick brown fox", "quick brown dog", "quick red fox", "quick red dog", "quick grey fox", "quick grey dog", "lazy brown fox", "lazy brown dog", "lazy red fox", "lazy red dog", "lazy grey fox", "lazy grey dog"]

var arr2d = [['red', 'blue'], ['cotton', 'polyester', 'silk'], ['large', 'medium', 'small']]

function combos(list, n = 0, result = [], current = []) {
    if (n === list.length) result.push(current)
    else list[n].forEach(item => combos(list, n + 1, result, [...current, item]))

    return result
}

console.log(combos(arr2d))
