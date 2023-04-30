const array= [1,2,3,4,5]
let score = array.reduce((total, elem) => {
    console.log(elem)
    return total + elem
})

console.log(score)