// Daily challenge: Not Bad
let sentence ='This dinner is bad';
let arr = sentence.split(' ');
let res = '';
let wordBad = null;
let wordNot = null;
for(let i=0;i<arr.length;i++){
    let word = arr[i].replace(/[^a-zA-Z]/g, '').toLowerCase();
    if(word === 'not'){
        wordNot = i;   
    }else if(word === 'bad'){
        wordBad = i;    
    }
}
if (wordNot !== null && wordBad !== null && wordNot < wordBad){
    arr.splice(wordNot, wordBad - wordNot + 1, 'good,');
}else{
    arr[wordBad] = 'good';
}
res = arr.join(' ');
console.log(res);
console.log(wordNot,wordBad);

let result = '';
if (wordNot !== null && wordBad !== null && wordNot < wordBad) {
    result = sentence.replace(/not.*bad/, 'good');
}
console.log(result);
