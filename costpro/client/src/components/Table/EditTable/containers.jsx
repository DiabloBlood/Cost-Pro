import { connect } from 'react-redux';
import NewEditTable from "src/components/Table/EditTable/NewEditTable.jsx";
import {
  onBeforeLoad,
  onLoadSuccess,
  onAddRow,
  onCellChange
} from "src/components/Table/EditTable/actions.jsx";



const mapStateToProps = state => {
  return {
    data: state.data,
    pages: state.pages,
    loading: state.loading
    editingIndex: state.editingIndex,
    isNew: state.isNew,
    editingRow: state.editingRow
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onBeforeLoad: () => dispatch(onBeforeLoad()),

    onLoadSuccess: res => dispatch(onLoadSuccess(res))
  }
}

const NewBaseTableContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(NewEditTable);

export default NewEditTableContainer;