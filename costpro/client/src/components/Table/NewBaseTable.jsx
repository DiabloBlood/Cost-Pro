import React from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
// @material-ui/core components
import Divider from '@material-ui/core/Divider';
// core components
import GridContainer from "src/components/Grid/GridContainer.jsx";
import GridItem from "src/components/Grid/GridItem.jsx";
import Card from "src/components/Card/Card.jsx";
import CardBody from "src/components/Card/CardBody.jsx";
import TableToolbar from "src/components/Table/TableToolbar.jsx";
import CustomButton from "src/components/CustomButton.jsx";
// @material-ui/icons
import Refresh from "@material-ui/icons/Refresh";
// global vars
import { CELL_BINDS } from "src/global/globalVars.jsx";
// css
import 'react-table/react-table.css';



/***
  1. BaseTable bundle all table layouts like TableToolBar, ReactTable, etc.
  2. BaseTable render cells, binding cell functions base on tableConfig.
***/

class BaseTable extends React.Component {

  constructor(props) {
    super(props);
    /*Build cells first, for bind cell render function*/
    //this.buildCells();
    this.tableRef = React.createRef();
    this.onFetchData = this.onFetchData.bind(this);
    this.reload = this.reload.bind(this);
  }

  /*
  buildCells() {
    let columns = this.props.tableConfig.columns;
    let { renderEditableCell, renderActionCell } = this.props;

    for(let i = 0; i < columns.length; i++) {
      let col = columns[i];
      if(col.cellBind == CELL_BINDS.editable) {
        col.Cell = renderEditableCell;
      } else if(col.cellBind == CELL_BINDS.action) {
        col.Cell = renderActionCell;
      }
    }
  }
  */

  onFetchData(state, instance) {
    /*
    this.setState({
      loading: true
    });
    */
    this.props.onBeforeLoad();

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

    /*
    axios.get(url, params).then((res) => {
      this.setState({
        data: res.data.rows,
        pages: res.data.total_pages,
        loading: false,
        editingIndex: -1,
        isNew: false,
        editingRow: null
      });
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
    */
    axios.get(url, params).then((res) => {
      this.props.onLoadSuccess(res);
    }).catch((err) => {
      console.log(err);
      throw "Load server-side data failed!"
    });
  }

  reload(e) {
    let state = this.tableRef.current.state;
    let instance = this.tableRef.current;
    this.tableRef.current.props.onFetchData(state, instance);
  }

  render() {
    let { title, columns, defulatPageSize, pageSizeOptions } = this.props.tableConfig;
    let { data, pages, loading } = this.props;

    return (
      <GridContainer>
        <GridItem xs={12}>
          <Card>
            <TableToolbar title={title}>
              <CustomButton color="github" justIcon round onClick={this.reload}>
                <Refresh />
              </CustomButton>
            </TableToolbar>
            <Divider inset />
            <CardBody>
              <ReactTable
                ref={this.tableRef}
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

export default BaseTable;