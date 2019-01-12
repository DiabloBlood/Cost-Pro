


/*
 * action types
 */
const ON_BEFORE_LOAD = 'ON_BEFORE_LOAD';
const ON_LOAD_SUCCESS = 'ON_LOAD_SUCCESS';
const SET_ALERT = 'SET_ALERT';
const ON_ADD_ROW = 'ON_ADD_ROW';
const ON_CELL_CHANGE = 'ON_CELL_CHANGE';
const ON_EDIT_ROW = 'ON_EDIT_ROW';
const ON_SAVE_SUCCESS = 'ON_SAVE_SUCCESS';


/*
 * action creators
 */
const onBeforeLoad = () => {
  return { type: ON_BEFORE_LOAD };
}

const onLoadSuccess = res => {
  return { type: ON_LOAD_SUCCESS, res };
}

const setAlert = alert => {
  return { type: SET_ALERT, alert };
}

const onAddRow = trackingKeys => {
  let editingRow = {};
  for(let i in trackingKeys) {
    editingRow[trackingKeys[i]] = '';
  }
  return { type: ON_ADD_ROW, editingRow };
}

const onCellChange = (name, value) => {
  return { type: ON_CELL_CHANGE, name, value };
}

const onEditRow = (trackingKeys, data, index) => {
  let editingRow = {};
  let row = data[index];
  for(let i in trackingKeys) {
    let key = trackingKeys[i];
    editingRow[key] = row[key];
  }

  return { type: ON_EDIT_ROW, editingRow, index };
}

const onSaveSuccess = () => {
  return { type: ON_SAVE_SUCCESS };
}


export {
  ON_BEFORE_LOAD,
  ON_LOAD_SUCCESS,
  SET_ALERT,
  ON_ADD_ROW,
  ON_CELL_CHANGE,
  ON_EDIT_ROW,
  ON_SAVE_SUCCESS,
  onBeforeLoad,
  onLoadSuccess,
  setAlert,
  onAddRow,
  onCellChange,
  onEditRow,
  onSaveSuccess
};