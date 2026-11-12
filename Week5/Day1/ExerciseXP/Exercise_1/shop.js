const products = require('./products.js');
function getproduct(name){
    return products.find(product => product.name == name)
}

console.log(getproduct("Wireless Bluetooth Headphones"))
console.log(getproduct("Organic Cotton T-Shirt"))
console.log(getproduct("Stainless Steel Water Bottle"))
console.log(getproduct("Yoga Mat Non-Slip"))
console.log(getproduct("Smartphone Case"))
