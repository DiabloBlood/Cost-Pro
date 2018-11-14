import React from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
// core components
import BaseTable from "src/components/Table/BaseTable.jsx";
// global vars
// css
import 'react-table/react-table.css';



/***
  1. EditTable do all filter, sort, change page job.
  2. EditTable do all CURD jobs.
***/

class EditTable extends React.Component {

  constructor(props) {
    super(props);

    this.fetchData = this.fetchData.bind(this);
    /*Build cells first, for bind cell render function*/
    this.buildCells();
    let { columns, defulatPageSize } = this.props.tableConfig;

    this.state = {
      columns: columns,
      loading: true
    };
  }

  onFetchData(state, instance) {
    this.setState({
      loading: true
    });

    let queryParams = {
      page: state.page + 1,
      pageSize: state.pageSize,
      sorted: state.sorted,
      filtered: state.filtered
    }

    let url = this.props.url;
    let params = {
      params: {
        value: btoa(JSON.stringify(queryParams))
      }
    }

    axios.get(url, params).then((res) => {
      this.setState({
        data: res.data.rows,
        pages: res.data.total_pages,
        page: state.page + 1,
        pageSize: state.pageSize,
        loading: false
      });
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
  }

  renderActionCell(cellProps) {
    return (
      <CustomButton color='success' justIcon>
        <Edit />
      </CustomButton>
    )
  }

  renderEditableCell(cellProps) {
    let { editingIndex } = this.state;
    if(editingIndex == cellProps.index) {
      return (
        <TextField
          label={cellProps.column.Header}
          margin="none"
          variant="filled"
          required
          onChange={this.editableCellOnChange}
          name={cellProps.column.id}
          style={{ height: 50, width: '100%' }}
        />
      )
    } else {
      return cellProps.value;
    }
  }

  editableCellOnChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  onAdd(e) {
    this.setState((state) => {
      let newData = state.data.map((value) => {
        return value;
      });
      newData.unshift({
        id: '',
        name: '',
        desc: ''
      });
      return {
        data: newData,
        editingIndex: 0
      }
    });
  }

  onSave(e) {
    //console.log(this.refs.table.refs);
    console.log(this.state);
  }

  render() {
    let { data, pages, loading } = this.state;
    let { tableConfig, onFetchData } = this.props;


    return (
      <BaseTable
        tableConfig={tableConfig}
        data={data}
        pages={pages}
        loading={loading}
        onFetchData={onFetchData}
      />
    )
  }
}

export default EditTable;