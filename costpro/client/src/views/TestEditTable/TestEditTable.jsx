import React from 'react';
//import EditTable from "src/components/Table/EditTable.jsx";
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { connect } from 'react-redux';
import NewBaseTable from "src/components/Table/NewBaseTable.jsx";
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



class TestEditTable extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(reducer);
  }

  render() {
    return (
      <Provider store={this.store}>
        <NewBaseTableContainer
          url={DATA_BASE_URL + DATA_SUB_URL.Category1}
          tableConfig={TABLE_CONFIG_CATEGORY}
        />
      </Provider>
    )
  }
}

export default TestEditTable;