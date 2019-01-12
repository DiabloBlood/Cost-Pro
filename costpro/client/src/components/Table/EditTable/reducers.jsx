import {
  ON_BEFORE_LOAD,
  ON_LOAD_SUCCESS,
  SET_ALERT,
  ON_ADD_ROW,
  ON_CELL_CHANGE,
  ON_EDIT_ROW,
  ON_SAVE_ROW
} from "src/components/Table/EditTable/actions.jsx";



const defaultState = {
  data: [],
  pages: 0,
  loading: true,
  alert: false,
  editingIndex: -1,
  isNew: false,
  editingRow: {}
}


const editTableReducer = (state = defaultState, action) => {
  switch (action.type) {
    case ON_BEFORE_LOAD:
      return { ...state, loading: true };
    case ON_LOAD_SUCCESS:
      return {
        data: action.res.data.rows,
        pages: action.res.data.total_pages,
        loading: false,
        editingIndex: -1,
        isNew: false,
        editingRow: null
      };
    case SET_ALERT:
      return {
        ...state,
        alert: action.alert
      }
    case ON_ADD_ROW:
      return {
        ...state,
        data: [ action.editingRow, ...state.data ],
        editingIndex: 0,
        isNew: true,
        editingRow: action.editingRow
      };
    case ON_CELL_CHANGE:
      return {
        ...state,
        editingRow: {
          ...state.editingRow,
          [action.name]: action.value
        }
      }
    case ON_EDIT_ROW:
      return {
        ...state,
        editingIndex: action.index,
        isNew: false,
        editingRow: action.editingRow 
      }
    case ON_SAVE_ROW:
      return {}
    default:
      return state;
  }
}


export default editTableReducer;