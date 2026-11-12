import fs from "fs/promises";
const fileContent = await fs.readFile("./files/file-data.txt","utf-8");
console.log(fileContent);