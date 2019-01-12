import { connect } from 'react-redux';
import EditTable from "src/components/Table/EditTable/EditTable.jsx";
import {
  onBeforeLoad,
  onLoadSuccess,
  setAlert,
  onAddRow,
  onCellChange,
  onEditRow,
  onSaveSuccess
} from "src/components/Table/EditTable/actions.jsx";



const mapStateToProps = state => {
  return {
    data: state.data,
    pages: state.pages,
    loading: state.loading,
    alert: state.alert,
    editingIndex: state.editingIndex,
    isNew: state.isNew,
    editingRow: state.editingRow
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  let { trackingKeys } = ownProps.tableConfig;
  return {
    onBeforeLoad: () => dispatch(onBeforeLoad()),
    onLoadSuccess: res => dispatch(onLoadSuccess(res)),
    setAlert: alert => dispatch(setAlert(alert)),
    onAddRow: () => dispatch(onAddRow(trackingKeys)),
    onCellChange: (name, value) => dispatch(onCellChange(name, value)),
    onEditRow: (data, index) => dispatch(onEditRow(trackingKeys, data, index)),
    onSaveSuccess: () => dispatch(onSaveSuccess())
  }
}

const EditTableContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(EditTable);

export default EditTableContainer;