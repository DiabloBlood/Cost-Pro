import React from 'react';
// redux, react-redux
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { connect } from 'react-redux';
// util
import Util from "src/global/util.jsx";
// reducer
import editTableReducer from "src/components/Table/EditTable/reducers.jsx";
// core components
import EditTableContainer from "src/components/Table/EditTable/containers.jsx";
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_TRANS } from "src/global/globalVars.jsx"



class Table extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(editTableReducer);
  }

  render() {
    return (
      <Provider store={this.store}>
        <EditTableContainer
          url={DATA_BASE_URL + DATA_SUB_URL.Table}
          tableConfig={Util.buildTableConfig(TABLE_CONFIG_TRANS)}
        />
      </Provider>
    )
  }
}

export default Table;