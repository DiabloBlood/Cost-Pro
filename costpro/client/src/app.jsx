import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from "react-router-dom";
// app layout
import AppLayout from "src/global/AppLayout.jsx";



import { createStore } from 'redux';

/*
class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path='/' component={AppLayout} />
        </Switch>
      </BrowserRouter>
    )
  }
}
*/

const defaultState = 0;
const reducer = (state = defaultState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
}

class Counter extends React.Component {

  constructor(props) {
    super(props);
    this.incrementAsync = this.incrementAsync.bind(this);
    this.incrementIfOdd = this.incrementIfOdd.bind(this);
  }

  incrementIfOdd () {
    if(this.props.value % 2 == 1) {
      this.props.onIncrement();
    }
  }

  incrementAsync() {
    setTimeout(this.props.onIncrement, 1000);
  }

  render() {
    const { value, onIncrement, onDecrement } = this.props;
    return (
      <p>
        Clicked: {value} times
        {' '}
        <button onClick={onIncrement}>
          +
        </button>
        {' '}
        <button onClick={onDecrement}>
          -
        </button>
        {' '}
        <button onClick={this.incrementIfOdd}>
          Increment if odd
        </button>
        {' '}
        <button onClick={this.incrementAsync}>
          Increment async
        </button>
      </p>
    )
  }
}

class App extends React.Component {

  constructor(props) {
    console.log('app');
    super(props);
    this.store = createStore(reducer);
    this.store.subscribe(render);
  }

  render() {
    return(
      <Counter
        value={this.store.getState()}
        onIncrement={() => this.store.dispatch({type: 'INCREMENT'})}
        onDecrement={() => this.store.dispatch({type: 'DECREMENT'})}
      />
    )
  }
}

const render = () => {
  ReactDOM.render(<App />, document.getElementById('app'));
}

render();