import React from 'react';
//import EditTable from "src/components/Table/EditTable.jsx";
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { connect } from 'react-redux';
import NewBaseTable from "src/components/Table/NewBaseTable.jsx";
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



/*
const defaultState = {
  alert: null,
  //columns: this.props.tableConfig.columns,
  loading: true,
  editingIndex: -1,
  isNew: false,
  editingRow: null
}
*/


const defaultState = {
  data: [],
  pages: 0,
  alert: null,
  //columns: this.props.tableConfig.columns,
  loading: true,
  editingIndex: -1,
  isNew: false,
  editingRow: null
}

const defaultTableDataState = {
  //columns: this.props.tableConfig.columns
  data: [],
  pages: 0,
  loading: true
}


const ON_BEFORE_LOAD = 'ON_BEFORE_LOAD';
const ON_LOAD_SUCCESS = 'ON_LOAD_SUCCESS';
//const LOAD_SUCCESS = 'LOAD_SUCCESS';

const onBeforeLoad = () => {
  return { type: ON_BEFORE_LOAD };
}

const onLoadSuccess = res => {
  return { type: ON_AFTER_LOAD, res}
}

const loadReducer = (state = defaultTableDataState, action) => {
  switch (action.type) {
    case ON_BEFORE_LOAD:
      return { ...state, loading: true };
    case ON_LOAD_SUCCESS:
      return {
        data: res.data.rows,
        pages: res.data.total_pages,
        loading: false
      };
    default:
      return state;
  }
}

const mapStateToProps = state => {
  return {
    data: state.data,
    pages: state.pages,
    loading: state.loading
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onBeforeLoad: () => dispatch(onBeforeLoad),
    onLoadSuccess: res => dispatch(onLoadSuccess)
  }
}

const NewBaseTableContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(NewBaseTable);


class TestEditTable extends React.Component {

  constructor(props) {
    super(props);
    this.store = createStore(loadReducer);
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