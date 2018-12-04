import React from 'react';
import { createStore } from 'redux';



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

//const StoreContext = React.createContext(null);

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

class TestRedux extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(counter);
    this.state = {
      storeState: this.store.getState()
    }
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this._isMounted = true;
    this.subscribe();
  }

  handleChange() {
    let newStoreState = this.store.getState();

    this.setState(prevState => {
      if(prevState.storeState === newStoreState) {
        return null;
      }

      return { storeState: newStoreState }
    });
  }

  subscribe() {
    this.unsubscribe = this.store.subscribe(this.handleChange);
  }

  render() {
    return (
      <Counter
        value={this.state.storeState}
        onIncrement={() => this.store.dispatch({ type: 'INCREMENT' })}
        onDecrement={() => this.store.dispatch({ type: 'DECREMENT' })}
      />
    )
  }
}

export default TestRedux;