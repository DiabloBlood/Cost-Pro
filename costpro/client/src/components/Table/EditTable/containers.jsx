import { connect } from 'react-redux';
import EditTable from "src/components/Table/EditTable/EditTable.jsx";
import {
  onBeforeLoad,
  onLoadSuccess,
  onAddRow,
  onCellChange,
  onEditRow
} from "src/components/Table/EditTable/actions.jsx";



const mapStateToProps = state => {
  return {
    data: state.data,
    pages: state.pages,
    loading: state.loading,
    editingIndex: state.editingIndex,
    isNew: state.isNew,
    editingRow: state.editingRow
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onBeforeLoad: () => dispatch(onBeforeLoad()),
    onLoadSuccess: res => dispatch(onLoadSuccess(res)),
    onAddRow: editingRow => dispatch(onAddRow(editingRow)),
    onCellChange: (name, value) => dispatch(onCellChange(name, value)),
    onEditRow: (editingRow, index) => dispatch(onEditRow(editingRow, index))
  }
}

const EditTableContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(EditTable);

export default EditTableContainer;