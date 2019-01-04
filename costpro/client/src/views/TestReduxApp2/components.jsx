import React from 'react'
import PropTypes from 'prop-types'



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

Todo.propTypes = {
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

export {
  TodoItem,
  TodoList
};