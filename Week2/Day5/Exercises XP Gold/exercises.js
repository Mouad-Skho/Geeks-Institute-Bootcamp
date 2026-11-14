// Exercise 1 : Divisible by three
let numbers = [123, 8409, 100053, 333333333, 7]
for(let element of numbers) {
    if (element % 3 === 0){
        console.log(element + ' -> true');
    }else{
        console.log(element + ' -> false');
    }
}
