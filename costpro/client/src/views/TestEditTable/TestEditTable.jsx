import React from 'react';
// redux, react-redux
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { connect } from 'react-redux';
// reducer
// core components
import editTableReducer from "src/components/Table/EditTable/reducers.jsx";
import EditTableContainer from "src/components/Table/EditTable/containers.jsx";
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



class TestEditTable extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(editTableReducer);
  }

  render() {
    return (
      <Provider store={this.store}>
        <EditTableContainer
          url={DATA_BASE_URL + DATA_SUB_URL.Category1}
          tableConfig={TABLE_CONFIG_CATEGORY}
        />
      </Provider>
    )
  }
}

export default TestEditTable;