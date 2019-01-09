import {
  ON_BEFORE_LOAD,
  ON_LOAD_SUCCESS,
  ON_ADD_ROW
} from "src/components/Table/EditTable/actions.jsx";



const defaultState = {
  data: [],
  pages: 0,
  alert: null,
  loading: true,
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
    case ON_ADD:
      return {
        data: [ action.editingRow, ...state.data ],
        editingIndex: 0,
        isNew: true,
        ...state
      };
    default:
      return state;
  }
}


export default editTableReducer;