


/*
 * action types
 */
const ON_BEFORE_LOAD = 'ON_BEFORE_LOAD';
const ON_LOAD_SUCCESS = 'ON_LOAD_SUCCESS';
const ON_ADD_ROW = 'ON_ADD_ROW';
const ON_CELL_CHANGE = 'ON_CELL_CHANGE';
const ON_EDIT_ROW = 'ON_EDIT_ROW';


/*
 * action creators
 */
const onBeforeLoad = () => {
  return { type: ON_BEFORE_LOAD };
}

const onLoadSuccess = res => {
  return { type: ON_LOAD_SUCCESS, res }
}

const onAddRow = editingRow => {
  return { type: ON_ADD_ROW, editingRow }
}

const onCellChange = (name, value) => {
  return { type: ON_CELL_CHANGE, name, value }
}

const onEditRow = (editingRow, index) => {
  return { type: ON_EDIT_ROW, editingRow, index }
}


export {
  ON_BEFORE_LOAD,
  ON_LOAD_SUCCESS,
  ON_ADD_ROW,
  ON_CELL_CHANGE,
  ON_EDIT_ROW,
  onBeforeLoad,
  onLoadSuccess,
  onAddRow,
  onCellChange,
  onEditRow
};