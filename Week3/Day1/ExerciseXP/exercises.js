// Exercise 1 : Find the numbers divisible by 23
function displayNumbersDivisible(divisor) {
    let sum = 0;
    console.log("Outcome : ");
    for (let i = 1; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }

    console.log(`sum : ${sum}`);
}
console.log("--------Divisible by 23--------");
displayNumbersDivisible(23);
console.log("--------Divisible by 3--------");
displayNumbersDivisible(3);
console.log("--------Divisible by 45--------");
displayNumbersDivisible(45);