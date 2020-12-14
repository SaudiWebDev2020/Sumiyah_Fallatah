function dec2bin(num) {
    let res = '0b'
    let testnum = ''
    while (num !== 0) {
        if (num % 2 === 1) {
            testnum += '1'
            // console.log("%2 =1 ", num % 2)
        } else if (num % 2 === 0) {
            testnum += '0'
            // console.log(" %2=0 ", num % 2)
        }
        num /= 2
        num = Math.floor(num)
        // console.log(num)
    }
    // console.log(testnum)
    for (var i = testnum.length - 1; i >= 0; i--) {
        res += testnum[i]
    }
    return res
}
console.log(dec2bin(13))
//should return '0b1101'