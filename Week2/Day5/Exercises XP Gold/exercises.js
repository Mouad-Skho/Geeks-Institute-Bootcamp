// Exercise 1 : Divisible by three
// let numbers = [123, 8409, 100053, 333333333, 7]
// for(let element of numbers) {
//     if (element % 3 === 0){
//         console.log(element + ' -> true');
//     }else{
//         console.log(element + ' -> false');
//     }
// }

// Exercise 2 : Attendance
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}
let userName = prompt('Please enter your name:');
for(let key in guestList){
    if (key === userName){
        console.log(`Hi! I'm ${key}, and I'm from ${guestList[key]}.`);
        break;
    }else{
        console.log(`Hi! I'm a guest.`);
        break;
    }
}
