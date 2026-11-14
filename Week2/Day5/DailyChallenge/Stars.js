// Daily challenge: Stars
console.log('-------------Stars with repeat method----------------')
for(let i=0;i<5;i++){
    console.log('*'.repeat(i+1))
}
console.log('-------------Stars with for loop----------------')
for(let i = 0; i < 5; i++){
    let stars = '';
    for(let j = 0; j <= i; j++){
        stars += '*';
    }
    console.log(stars);
}