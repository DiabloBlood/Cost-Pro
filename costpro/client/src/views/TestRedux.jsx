import React from 'react';
import { createStore } from 'redux';



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
    console.log(this.props);
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


const defaultState = 0;
const counter = (state = defaultState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
}

const store = createStore(counter);


class TestRedux extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Counter
        value={store.getState()}
        onIncrement={() => store.dispatch({ type: 'INCREMENT' })}
        onDecrement={() => store.dispatch({ type: 'DECREMENT' })}
      />
    )
  }
}

export default TestRedux;