import { combineReducers } from 'redux';
import {
  ADD_TODO,
  TOGGLE_TODO,
  SET_VISIBILITY_FILTER,
  VisibilityFilters,
} from "src/views/TestReduxApp2/actions.jsx";



/*
const defaultState = {
  visibilityFilter: VisibilityFilters.SHOW_ALL,
  todos: []
}
*/


const todoReducer = (state = [], action) => {
  switch(action.type) {
    case ADD_TODO:
      return [
        ...state,
        {
          test: action.text,
          completed: false
        }
      ]
    case TOGGLE_TODO:
      return state.map((todo, index) => {
        if(index === action.index) {
          //TODO: try don't use object assign
          return Object.assign({}, todo, { completed: !todo.completed });
        }
        return todo;
      });
    default:
      return state;
  }
}


const visibilityReducer = (state = VisibilityFilters.SHOW_ALL, action) => {
  switch(action.type) {
    case SET_VISIBILITY_FILTER:
      return action.filter;
    default:
      return state;
  }
}


const appReducer = combineReducers({
  visibilityFilter: visibilityReducer,
  todos: todoReducer
});

export default appReducer;

// Note: think why use {} replace default state
/*
const appReducer = (state = {}, action) => {
  return {
    visibilityFilter: visibilityReducer(state.visibilityFilter, action)
    todos: todoReducer(state.todos, action)
  }
}
*/

/*
const reducer = (state = defaultState, action) => {
  switch(action.type) {
    case SET_VISIBILITY_FILTER:
      return Object.assgin({}, state, { visibilityFilter: action.filter });
      // object spread operator proposal
      // return { ...state, visibilityFilter: action.filter }
    case ADD_TODO:
      return Object.assign({}, state, { todos: todoReducer(state.todos, action) });
    case TOGGLE_TODO:
      return Object.assign({}, state, { todos: todoReducer(state.todos, action) });
    default:
      return state;
  }
}
*/
