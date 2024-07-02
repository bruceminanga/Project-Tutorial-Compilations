import React, { useState } from 'react';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleAddTodo = () => {
    if (inputValue.trim() !== '') {
      setTodos([...todos, inputValue]);
      setInputValue('');
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Todo List</h1>
      <div className="flex mb-4">
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          className="flex-grow p-2 border rounded-l"
          placeholder="Enter a new todo"
        />
        <button
          onClick={handleAddTodo}
          className="bg-blue-500 text-white p-2 rounded-r"
        >
          Add
        </button>
      </div>
      <ul className="list-disc pl-5">
        {todos.map((todo, index) => (
          <li key={index} className="mb-2">{todo}</li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;