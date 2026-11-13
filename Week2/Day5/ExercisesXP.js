// Exercise 1 : List of people
console.log('Part I - Review about arrays')
const people = ["Greg", "Mary", "Devon", "James"];
people.shift()
console.log(people)

people[3] = "Jason"
console.log(people)

people.push('Mouad')
console.log(people)

console.log(people.indexOf('Mary'))

const last = people.slice(1,people.length-1)
console.log(last)

console.log('Part II - Loops')

people.forEach(person => console.log(person))
console.log('--------------------------------------')
for(let person of people){
    if (person == 'Devon'){
        console.log(person)
        break
    }else{
        console.log(person)
    }
    
}
