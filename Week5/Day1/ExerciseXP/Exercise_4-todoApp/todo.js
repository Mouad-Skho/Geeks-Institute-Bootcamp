class TodoList{
    constructor() {
        this.todoList = []

    }
    addTask(task){
        this.todoList.push(task);
    }
    markTaskComplete(index){
        this.todoList[index-1].completed = true;
    }
    listTasks(){
        this.todoList.forEach((task, index) => {
            console.log(`${index + 1}. ${task.name} - ${task.completed ? 'Completed' : 'Not Completed'}`);
        });
    }
}
export default TodoList;