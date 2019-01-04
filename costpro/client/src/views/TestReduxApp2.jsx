import React from 'react';
import { createStore } from 'redux';
import { connect, Provider } from 'react-redux';



/*
 * action types
 */
const ADD_TODO = 'ADD_TODO';
const TOGGLE_TODO = 'TOGGLE_TODO';
const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';


/*
 * other constants
 */
const VisibilityFilters = {
  SHOW_ALL: 'SHOW_ALL',
  SHOW_COMPLETED: 'SHOW_COMPLETED',
  SHOW_ACTIVE: 'SHOW_ACTIVE'
}


/*
 * action creators
 */
const addTodo = (text) => {
  return { type: ADD_TODO, text }
}

const toggleTodo = (index) => {
  return { type: TOGGLE_TODO, index }
}

const setVisibilityFilter = (filter) => {
  return { type: SET_VISIBILITY_FILTER, filter }
}

const defaultState = {
  visibilityFilter: VisibilityFilters.SHOW_ALL,
  todos: []
}

const reducer = (state = defaultState, action) => {
  switch(action.type) {
    case SET_VISIBILITY_FILTER:
      return Object.assgin({}, state, {
        visibilityFilter: action.filter
      });
      // object spread operator proposal
      // return { ...state, visibilityFilter: action.filter }
    case ADD_TODO:
      return Object.assign({}, state, {
        todos: [
          ...state.todos,
          {
            text: action.text,
            completed: false
          }
        ]
      })
    default:
      return state;
  }
}


class TestReduxApp2 extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>haha</h1>
    )
  }
}



export default TestReduxApp2;