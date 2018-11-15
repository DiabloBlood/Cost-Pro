import React from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
// @material-ui/core components
import TextField from '@material-ui/core/TextField';
// core components
import BaseTable from "src/components/Table/BaseTable.jsx";
import CustomButton from "src/components/CustomButton.jsx";
// @material-ui/icons
import AddShoppingCart from "@material-ui/icons/AddShoppingCart";
import Save from "@material-ui/icons/Save";
import Edit from "@material-ui/icons/Edit";
import DeleteForever from "@material-ui/icons/DeleteForever";
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

    this.onFetchData = this.onFetchData.bind(this);
    this.renderActionCell = this.renderActionCell.bind(this);
    this.renderEditableCell = this.renderEditableCell.bind(this);
    this.editableCellOnChange = this.editableCellOnChange.bind(this);
    this.onAdd = this.onAdd.bind(this);
    this.onSave = this.onSave.bind(this);

    this.state = {
      columns: this.props.tableConfig.columns,
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
        loading: false
      });
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
  }

  onSave(e) {
    console.log(this.state);
  }

  renderActionCell(cellProps) {
    return (
      <React.Fragment>
        <CustomButton color='info' justIcon>
          <Save />
        </CustomButton>
        <CustomButton color='success' justIcon onClick={this.onSave}>
          <Edit />
        </CustomButton>
        <CustomButton color='danger' justIcon>
          <DeleteForever />
        </CustomButton>
      </React.Fragment>
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

  render() {
    let { data, pages, loading } = this.state;
    let { tableConfig, onFetchData } = this.props;

    let toolbarButtons = (
      <CustomButton color="github" justIcon round onClick={this.onAdd}>
        <AddShoppingCart />
      </CustomButton>
    );


    return (
      <BaseTable
        tableConfig={tableConfig}
        data={data}
        pages={pages}
        loading={loading}
        onFetchData={this.onFetchData}
        renderActionCell={this.renderActionCell}
        renderEditableCell={this.renderEditableCell}
        toolbarButtons={toolbarButtons}
      />
    )
  }
}

export default EditTable;