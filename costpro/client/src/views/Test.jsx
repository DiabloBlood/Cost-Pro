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

import { cardTitle } from "src/assets/jss/globalStyle.jsx";

import { DATA_BASE_URL, DATA_SUB_URL } from "src/global/globalVars.jsx"
import axios from 'axios';
import ReactTable from 'react-table';
import 'react-table/react-table.css';



let tableConfig = {
  defulatPageSize: 5,
  pageSizeOptions: [5, 10],
  columns: [
    {
      Header: 'Action',
      Cell: (props) => {
        return (
          <AddShoppingCart />
        )
      }
    },
    {
      Header: 'ID',
      accessor: 'id',
      width: 100
    },
    {
      Header: 'Category Name',
      accessor: 'name',
      width: 200,
    },
    {
      Header: 'Category Description',
      accessor: 'desc',
      width: 500
    }
  ]
}


class Test extends React.Component {

  constructor(props) {
    super(props);

    let { columns, defulatPageSize } = tableConfig;

    this.state = {
      columns: columns,
      data: [],
      page: 1,
      pageSize: defulatPageSize,
      pages: null,
      loading: true
    };

    this.onFetchData = this.onFetchData.bind(this);
    this.handleAdd = this.handleAdd.bind(this);
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

    let url = DATA_BASE_URL + DATA_SUB_URL.Category1;
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

  handleAdd(e) {
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
        data: newData
      }
    });
  }

  /*
  getTbodyProps(state, rowInfo, column) {
    console.log(state);
    console.log(rowInfo);
    console.log(column);
    //console.log(instance);
    return {
      style: {
        background: this.state.cc
      }
    }
  }
  */

  render() {
    let { classes } = this.props;
    let { columns, defulatPageSize, pageSizeOptions } = tableConfig;
    let { data, pages, loading } = this.state;

    return (
      <GridContainer>
        <GridItem xs={12}>
          <Card>
            <TableToolbar title="Category 1">
              <CustomButton color="github" justIcon round onClick={this.handleAdd}>
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
              />
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    )
  }
}

export default Test;