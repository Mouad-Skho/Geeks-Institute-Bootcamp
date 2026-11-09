function compareToTen(num){
    if (num > 10) {
        resolve("I will get the gift");
    } else {
        reject("I won't get the gift");
    }
};
console.log(compareToTen(15));
console.log(compareToTen(5));
