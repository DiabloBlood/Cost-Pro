import React from 'react';
import { createStore } from 'redux';
import { connect, Provider } from 'react-redux';
// reducer
import appReducer from "src/views/TestReduxApp2/reducers.jsx"
import {
  addTodo,
  toggleTodo,
  setVisibilityFilter,
  VisibilityFilters
} from "src/views/TestReduxApp2/actions.jsx"



class TestReduxApp2 extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(appReducer);
  }

  render() {
    return (
      <AddTodo />
    )
  }
}



export default TestReduxApp2;