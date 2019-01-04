


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


export {
  ADD_TODO,
  TOGGLE_TODO,
  SET_VISIBILITY_FILTER,
  VisibilityFilters,
  addTodo,
  toggleTodo,
  setVisibilityFilter
}