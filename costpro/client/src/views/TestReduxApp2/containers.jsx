import React from 'react';
import { connect } from 'react-redux';
import { addTodo } from "src/views/TestReduxApp2/actions.jsx"
import { AddTodo } from "src/views/TestReduxApp2/components.jsx"



const mapDispatchToProps = (dispatch) => {
  return {
    addTodo: text => dispatch(addTodo(text))
  }
}

const TodoApp = connect(
  null,
  mapDispatchToProps
)(TodoApp);

export default TodoApp;