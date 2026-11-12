import people from './data.js';
function averageAge(){
    let totalAge =0;
    for(let person of people){
        totalAge += person.age
    }
    return totalAge / people.length
};
console.log(averageAge());