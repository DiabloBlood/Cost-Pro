


/*
 * action types
 */
const ON_BEFORE_LOAD = 'ON_BEFORE_LOAD';
const ON_LOAD_SUCCESS = 'ON_LOAD_SUCCESS';
const ON_ADD_ROW = 'ON_ADD_ROW';


/*
 * action creators
 */
const onBeforeLoad = () => {
  return { type: ON_BEFORE_LOAD };
}

const onLoadSuccess = res => {
  return { type: ON_LOAD_SUCCESS, res}
}

const onAddRow = editingRow => {
  return { type: ON_ADD_ROW, editingRow}
}


export {
  ON_BEFORE_LOAD,
  ON_LOAD_SUCCESS,
  ON_ADD_ROW,
  onBeforeLoad,
  onLoadSuccess,
  onAddRow
};