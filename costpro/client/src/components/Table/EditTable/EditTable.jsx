import React from 'react';
import ReactTable from 'react-table';
// AJAX
import axios from 'axios';
// @material-ui/core methods
import withStyles from "@material-ui/core/styles/withStyles";
// @material-ui/core components
import Divider from '@material-ui/core/Divider';
import TextField from '@material-ui/core/TextField';
// Third party components
import SweetAlert from "react-bootstrap-sweetalert";
// core components
import GridContainer from "src/components/Grid/GridContainer.jsx";
import GridItem from "src/components/Grid/GridItem.jsx";
import Card from "src/components/Card/Card.jsx";
import CardBody from "src/components/Card/CardBody.jsx";
import TableToolbar from "src/components/Table/TableToolbar.jsx";
import CustomButton from "src/components/CustomButton.jsx";
// @material-ui/icons
import AddShoppingCart from "@material-ui/icons/AddShoppingCart";
import Refresh from "@material-ui/icons/Refresh";
import Save from "@material-ui/icons/Save";
import Edit from "@material-ui/icons/Edit";
import Cancel from "@material-ui/icons/Cancel";
import DeleteForever from "@material-ui/icons/DeleteForever";
// global vars
import { CELL_BINDS } from "src/global/globalVars.jsx";
// jss assets
import editTableStyle from "src/assets/jss/components/editTableStyle.jsx";
// css
import 'react-table/react-table.css';




class EditTable extends React.Component {

  constructor(props) {
    super(props);

    this.tableRef = React.createRef();
    this.onFetchData = this.onFetchData.bind(this);
    this.reload = this.reload.bind(this);
    // cell render functions
    this.renderActionCell = this.renderActionCell.bind(this);
    this.renderEditableCell = this.renderEditableCell.bind(this);
    // alert
    this.popAlert = this.popAlert.bind(this);
    this.hideAlert = this.hideAlert.bind(this);

    this.onAddRowWrapper = this.onAddRowWrapper.bind(this);
    this.onCellChangeWrapper = this.onCellChangeWrapper.bind(this);
    this.onEditRowWrapper = this.onEditRowWrapper.bind(this);
    this.onCancelRowWrapper = this.onCancelRowWrapper.bind(this);
    this.onSaveRowWrapper = this.onSaveRowWrapper.bind(this);
    this.onDeleteRowWrapper = this.onDeleteRowWrapper.bind(this);

    /*Build cells, for bind cell render function*/
    this.buildCells();
  }

  onFetchData(state, instance) {

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

  buildCells() {
    let columns = this.props.tableConfig.columns;
    let { renderEditableCell, renderActionCell } = this.props;

    for(let i = 0; i < columns.length; i++) {
      let col = columns[i];
      if(col.cellBind == CELL_BINDS.editable) {
        col.Cell = this.renderEditableCell;
      } else if(col.cellBind == CELL_BINDS.action) {
        col.Cell = this.renderActionCell;
      }
    }
  }

  renderActionCell(cellProps) {
    let classes = this.props.classes;
    return (
      <React.Fragment>
        <CustomButton color='info' className={classes.actionButton} onClick={(e) => this.onSaveRowWrapper(cellProps.index, e)}>
          <Save className={classes.icon} />
        </CustomButton>
        <CustomButton color='success' className={classes.actionButton} onClick={(e) => this.onEditRowWrapper(cellProps.index, e)}>
          <Edit className={classes.icon} />
        </CustomButton>
        <CustomButton color='warning' className={classes.actionButton} onClick={(e) => this.onCancelRowWrapper(cellProps.index, e)}>
          <Cancel className={classes.icon} />
        </CustomButton>
        <CustomButton color='danger' className={classes.actionButton} onClick={(e) => this.onDeleteRowWrapper(cellProps.index, e)}>
          <DeleteForever className={classes.icon} />
        </CustomButton>
      </React.Fragment>
    )
  }

  renderEditableCell(cellProps) {
    let { editingIndex } = this.props;
    let value = cellProps.value;

    if(editingIndex == cellProps.index) {
      return (
        <TextField
          label={cellProps.column.Header}
          margin="none"
          variant="filled"
          required
          onChange={this.onCellChangeWrapper}
          name={cellProps.column.id}
          defaultValue={value}
          style={{ height: 50, width: '100%' }}
        />
      )
    }
    return value;
  }

  getAlertCard() {
    return (
      <SweetAlert
        type="warning"
        title="Please save the current editing row first!"
        onConfirm={this.hideAlert}
        focusConfirmBtn={false}
        confirmBtnCssClass={
          this.props.classes.button + " " + this.props.classes.warning
        }
      />
    )
  }

  popAlert() {
    this.props.setAlert(true);
  }

  hideAlert() {
    this.props.setAlert(false);
  }

  onCellChangeWrapper(e) {
    this.props.onCellChange(e.target.name, e.target.value);
  }

  onAddRowWrapper(e) {
    let { editingIndex } = this.props;

    if(editingIndex > -1) {
      this.popAlert();
      return;
    }

    this.props.onAddRow();
  }

  onEditRowWrapper(index, e) {
    let { editingIndex, data } = this.props;

    if(editingIndex > -1 && editingIndex != index) {
      this.popAlert();
      return;
    }

    this.props.onEditRow(data, index);
  }

  onCancelRowWrapper(index, e) {
    let { editingIndex } = this.props;

    if(editingIndex == -1 || editingIndex != index) {
      return;
    }

    this.props.onCancelRow();
  }

  onSaveRowWrapper(index, e) {
    let { editingIndex, isNew, editingRow } = this.props;

    if(editingIndex == -1 || editingIndex != index) {
      return;
    }

    let url = this.props.url;
    let params = {
      isNew: isNew,
      editingRow: editingRow
    }

    axios.post(url, params).then((res) => {
      this.props.onSaveSuccess(res);
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
  }

  onDeleteRowWrapper(index, e) {
    let { editingIndex, data } = this.props;

    if(editingIndex > -1) {
      this.popAlert();
      return;
    }

    let url = this.props.url;
    let params = {
      data: {
        id: data[index].id
      }
    }

    axios.delete(url, params).then((res) => {
      this.props.onDeleteSuccess(index);
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
  }

  render() {
    let { title, columns, defulatPageSize, pageSizeOptions } = this.props.tableConfig;
    let { data, pages, alert, loading } = this.props;

    let alertCard = alert ? this.getAlertCard() : null;

    return (
      <React.Fragment>
        { alertCard }
        <GridContainer>
          <GridItem xs={12}>
            <Card>
              <TableToolbar title={title}>
                <CustomButton color="github" justIcon round onClick={this.onAddRowWrapper}>
                  <AddShoppingCart />
                </CustomButton>
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
      </React.Fragment>
    )
  }
}

export default withStyles(editTableStyle)(EditTable);