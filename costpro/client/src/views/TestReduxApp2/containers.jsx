import React from 'react';
import { connect } from 'react-redux';
import { addTodo, toggleTodo, setVisibilityFilter, VisibilityFilters } from "src/views/TestReduxApp2/actions.jsx";
import { AddTodo, TodoList, Link } from "src/views/TestReduxApp2/components.jsx";



const mapDispatchToProps = dispatch => {
  return {
    addTodo: text => dispatch(addTodo(text))
  }
}

const AddTodoContainer = connect(
  null,
  mapDispatchToProps
)(AddTodo);


const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    case VisibilityFilters.SHOW_ALL:
      return todos
    case VisibilityFilters.SHOW_COMPLETED:
      return todos.filter(item => item.completed)
    case VisibilityFilters.SHOW_ACTIVE:
      return todos.filter(item => !item.completed)
    default:
      throw new Error('Unknown filter: ' + filter)
  }
}

const mapStateToPropsTodoList = state => {
  return {
    todos: getVisibleTodos(state.todos, state.visibilityFilter)
  }
}

const mapDispatchToPropsTodoList = dispatch => {
  return {
    onTodoClick: index => dispatch(toggleTodo(index))
  }
}

const TodoListContainer = connect(
  mapStateToPropsTodoList,
  mapDispatchToPropsTodoList
)(TodoList);


const mapStateToPropsLink = (state, ownProps) => {
  return {
    active: ownProps.filter === state.visibilityFilter
  }
}

const mapDispatchToPropsLink = (dispatch, ownProps) => {
  return {
    onClick: () => dispatch(setVisibilityFilter(ownProps.filter))
  }
}

const LinkContainer = connect(
  mapStateToPropsLink,
  mapDispatchToPropsLink
)(Link);


class FooterContainer extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <React.Fragment>
        <span>Show: </span>
        <LinkContainer filter={VisibilityFilters.SHOW_ALL}>
          All
        </LinkContainer>
        <LinkContainer filter={VisibilityFilters.SHOW_ACTIVE}>
          Active
        </LinkContainer>
        <LinkContainer filter={VisibilityFilters.SHOW_COMPLETED}>
          Completed
        </LinkContainer>
      </React.Fragment>
    )
  }
}


class TodoApp extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <React.Fragment>
        <AddTodoContainer />
        <TodoListContainer />
        <FooterContainer />
      </React.Fragment>
    )
  }
}

export default TodoApp;