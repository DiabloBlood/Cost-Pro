/*
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from "react-router-dom";
// app layout
import AppLayout from "src/global/AppLayout.jsx";



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

ReactDOM.render(<App />, document.getElementById('app'));
*/

import ReactDOM from 'react-dom';


import React from 'react';
import { createStore } from 'redux';
import { connect, Provider } from 'react-redux';



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

/*
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
*/

const defaultState = {value: 1};
const reducer = (state = defaultState, action) => {
  let value = state.value;
  switch (action.type) {
    case 'INCREMENT':
      //console.log(state);
      return {value: value + 1};
    case 'DECREMENT':
      return {value: value - 1};
    default:
      return state;
  }
}

/*
      <Counter
        value={store.getState()}
        onIncrement={() => store.dispatch({ type: 'INCREMENT' })}
        onDecrement={() => store.dispatch({ type: 'DECREMENT' })}
      />
*/

const mapStateToProps = (state, ownProps) => {
  return {
    value: state.value
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    onIncrement: () => dispatch({ type: 'INCREMENT' }),
    onDecrement: () => dispatch({ type: 'DECREMENT' })
  }
}

const Container = connect(
  mapStateToProps,
  mapDispatchToProps
)(Counter);


const store = createStore(reducer);


class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Container />
    )
  }
}

ReactDOM.render(
  <Provider store={store}>
    <Container />
  </Provider>,
  document.getElementById('app')
);

console.log(store);