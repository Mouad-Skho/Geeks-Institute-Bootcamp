// Exercise 1 : Colors
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach(function( color, index){
    console.log(`${index + 1}# choice is ${color}`);
    if (color === "Violet") {
        console.log("yeah")
    }else{
        console.log("No...")
    }
});