import React from 'react';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
// reducer
import appReducer from "src/views/TestReduxApp2/reducers.jsx";
import TodoApp from "src/views/TestReduxApp2/containers.jsx";



class TestReduxApp2 extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(appReducer);
  }

  render() {
    return (
      <Provider store={this.store}>
        <TodoApp />
      </Provider>
    )
  }
}



export default TestReduxApp2;