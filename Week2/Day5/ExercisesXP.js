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
// Exercise 2 : Your favorite colors
const colors = ['lilac','violet','Blue Iris','yellow']
const pr = new Intl.PluralRules('en', { type: 'ordinal' });
const suffixMap = { one: 'st', two: 'nd', few: 'rd', other: 'th' };
const ordinal = n => n + suffixMap[pr.select(n)];
console.log('-------------without ordinal number----------')
colors.forEach((color,index)=>{
    console.log(`My #${index+1} choice is ${color}` )
})
console.log('-------------with ordinal number-------------')
colors.forEach((color,index)=>{
    console.log(`My #${ordinal(index+1)} choice is ${color}` )
})

