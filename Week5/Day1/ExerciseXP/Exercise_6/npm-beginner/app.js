const chalk = require("chalk");
console.log(chalk.red("Hello World!"));              
console.log(chalk.blue.bgYellow.bold("Warning"));    
console.log(chalk.hex("#FF5733")("Custom color"));   
console.log(chalk.rgb(255, 99, 132)("RGB color"));   