const fs = require("fs");




const helloWorld = fs.writeFile('Hello World.txt', 'Hello World !!', function (err) { 
    if (err){ 
        console.log(err);
    }
    else{
        console.log('Write operation complete.');
    }
});
const byeWorld = fs.writeFile('Bye World.txt', 'Bye World !!', function (err) { 
    if (err){ 
        console.log(err);
    }
    else{
        console.log('Write operation complete.');
    }
});

const info = fs.readFile("Hello World.txt", "utf-8", (err, data) => {
    if (err){ 
        console.log(err);
    }
    else{
        console.log(data);
    };
});
console.log("The file has been read");
exports.info = info;
exports.helloWorld = helloWorld;
exports.byeWorld = byeWorld;
