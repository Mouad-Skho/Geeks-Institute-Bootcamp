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

// Exercise 2 : Shopping List

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];
function myBill(){
    let bill =0;
    for(let item of shoppingList){
        if (stock[item] > 0) {
            bill += prices[item];
            stock[item]--;
        }
    }
    return console.log(`Your bill is ${bill}`);
};

myBill();
console.log(stock);
// output: Your bill is 5.5
// { banana: 5, apple: 0, pear: 12, orange: 31, blueberry: 1 } 
