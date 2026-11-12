import TodoList from "./todo.js";
const todo1 = new TodoList();
todo1.addTask({name:'Task1',completed:false});
todo1.addTask({name:'Task2',completed:false});
todo1.addTask({name:'Task3',completed:false});
todo1.addTask({name:'Task4',completed:false});
console.log('--------------------------------------')
todo1.markTaskComplete(2);
todo1.markTaskComplete(3);
console.log('--------------------------------------')
todo1.listTasks();