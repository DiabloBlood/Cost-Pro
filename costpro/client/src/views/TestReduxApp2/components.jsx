import React from 'react'
import PropTypes from 'prop-types'



//This is the add todo input field with a button
class AddTodo extends React.Component {

  constructor(props) {
    super(props);
    this.inputRef = React.createRef();
    this.addTodo = this.addTodo.bind(this);
  }

  addTodo() {
    let inputText = this.inputRef.current.value.trim();
    if(!inputText) {
      return;
    }
    this.props.addTodo(inputText);
    //this.inputRef.current.value = '';
  }

  render() {
    return (
      <div>
        <input ref={this.inputRef} />
        <button onClick={this.addTodo}>Add Todo</button>
      </div>
    )
  }
}

AddTodo.propTypes = {
  addTodo: PropTypes.func.isRequired
}


// This is a single todo item
class TodoItem extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { onClick, completed, text } = this.props;
    return (
      <li onClick={onClick} style={{ textDecoration: completed ? 'line-through' : 'none' }}>
        {text}
      </li>
    )
  }
}

TodoItem.propTypes = {
  onClick: PropTypes.func.isRequired,
  completed: PropTypes.bool.isRequired,
  text: PropTypes.string.isRequired
}


class TodoList extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { todos, onTodoClick } = this.props;
    let todoItems = todos.map((todo, index) => {
      return <Todo key={index} {...todo} onClick={() => onTodoClick(index)} />
    });

    return (
      <ul>todoItems</ul>
    )
  }
}

TodoList.propTypes = {
  todos: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      completed: PropTypes.bool.isRequired,
      text: PropTypes.string.isRequired
    }).isRequired
  ).isRequired,
  onTodoClick: PropTypes.func.isRequired
}


class TodoApp extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { addTodo } = this.props;
    return (
      <AddTodo addTodo={addTodo} />
    )
  }
}

export {
  AddTodo,
  TodoItem,
  TodoList,
  TodoApp
};