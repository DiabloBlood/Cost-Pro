import React from 'react';



const defaultState = {
  alert: null,
  //columns: this.props.tableConfig.columns,
  loading: true,
  editingIndex: -1,
  isNew: false,
  editingRow: null
}

/*
const reducer = (state = defaultState, action) => {
  switch (action.type) {
    case ''
  }
}
*/

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


class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>Test</h1>
    )
  }
}

export default Test;