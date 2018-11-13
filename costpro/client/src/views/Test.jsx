import React from 'react';

import Grid from "@material-ui/core/Grid";
import withStyles from "@material-ui/core/styles/withStyles";
//test CardIcon
import GridContainer from "src/components/Grid/GridContainer.jsx";
import GridItem from "src/components/Grid/GridItem.jsx";
import Card from "src/components/Card/Card.jsx";
import CardBody from "src/components/Card/CardBody.jsx";
import CardHeader from "src/components/Card/CardHeader.jsx";
import CardIcon from "src/components/Card/CardIcon.jsx";
import CustomButton from "src/components/CustomButton.jsx";
import TableToolbar from "src/components/Table/TableToolbar.jsx";

import Divider from '@material-ui/core/Divider';

import Assignment from "@material-ui/icons/Assignment";
import AddShoppingCart from "@material-ui/icons/AddShoppingCart";


import Add from "@material-ui/icons/Add";
import Favorite from "@material-ui/icons/Favorite";
import Build from "@material-ui/icons/Build";
import Edit from "@material-ui/icons/Edit";

import { cardTitle } from "src/assets/jss/globalStyle.jsx";

import { DATA_BASE_URL, DATA_SUB_URL } from "src/global/globalVars.jsx"
import axios from 'axios';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

import TextField from '@material-ui/core/TextField';



const CELL_BINDS = {
  action: 'action',
  editable: 'editable'
}

const TABLE_CONFIG = {
  defulatPageSize: 5,
  pageSizeOptions: [5, 10],
  columns: [
    {
      Header: 'Action',
      width: 200,
      cellBind: CELL_BINDS.action
    },
    {
      Header: 'ID',
      accessor: 'id',
      width: 100,
    },
    {
      Header: 'Category Name',
      accessor: 'name',
      width: 200,
      cellBind: CELL_BINDS.editable
    },
    {
      Header: 'Category Description',
      accessor: 'desc',
      width: 500,
      cellBind: CELL_BINDS.editable
    }
  ]
}


class Table extends React.Component {

  constructor(props) {
    super(props);

    this.refs = React.createRef();

    console.log(typeof this.refs);
    console.log(this.refs);

    this.onFetchData = this.onFetchData.bind(this);
    this.onAdd = this.onAdd.bind(this);
    this.onSave = this.onSave.bind(this);
    this.renderEditableCell = this.renderEditableCell.bind(this);

    this.buildCells();
    let { columns, defulatPageSize } = this.props.tableConfig;

    this.state = {
      columns: columns,
      data: [],
      page: 1,
      pageSize: defulatPageSize,
      pages: null,
      loading: true,
      editingIndex: -1
    };
  }

  buildCells() {
    let columns = this.props.tableConfig.columns;
    for(let i = 0; i < columns.length; i++) {
      let col = columns[i];
      if(col.cellBind == this.props.cellBinds.editable) {
        col.Cell = this.renderEditableCell;
      } else if(col.cellBind == this.props.cellBinds.action) {
        col.Cell = this.renderActionCell;
      }
    }
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
          ref={cellProps.column.id}
          style = {{ height: 50, width: '100%' }}
        />
      )
    } else {
      return cellProps.value;
    }
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
    console.log(this.refs.table.refs);
  }

  getProps(tableState, a, b, c) {
    console.log(tableState);
    console.log(a);
    console.log(b);
    console.log(c);
    return {}
  }

  render() {
    let { classes } = this.props;
    let { columns, defulatPageSize, pageSizeOptions } = this.props.tableConfig;
    let { data, pages, loading } = this.state;

    return (
      <GridContainer>
        <GridItem xs={12}>
          <Card>
            <TableToolbar title="Category 1">
              <CustomButton color="github" justIcon round onClick={this.onAdd}>
                <AddShoppingCart />
              </CustomButton>
              <CustomButton color="github" round onClick={this.onSave}>
                <AddShoppingCart />
              </CustomButton>
            </TableToolbar>
            <Divider inset />
            <CardBody>
              <ReactTable
                manual
                columns={columns}
                data={data}
                pages={pages}
                loading={loading}
                onFetchData={this.onFetchData}
                filterable
                defaultPageSize={defulatPageSize}
                pageSizeOptions={pageSizeOptions}
                className="-striped -highlight"
                getProps={this.getProps}
                ref="table"
              />
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    )
  }
}

class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Table
        url={DATA_BASE_URL + DATA_SUB_URL.Category1}
        tableConfig={TABLE_CONFIG}
        cellBinds={CELL_BINDS}
      />
    )
  }
}

export default Test;