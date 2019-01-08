// @material-ui/icons
import DashboardIcon from "@material-ui/icons/Dashboard";
import HomeIcon from "@material-ui/icons/Home";
import TableChartIcon from "@material-ui/icons/TableChart";
import CategoryIcon from "@material-ui/icons/Category";
// views
import Dashboard from "src/views/Dashboard.jsx"
import Table from "src/views/Table.jsx"
import Category from "src/views/Category.jsx"
import Test from "src/views/Test.jsx"
import Test2 from "src/views/Test2.jsx"
import TestReduxApp1 from "src/views/TestReduxApp1.jsx"
import TestReduxApp2 from "src/views/TestReduxApp2/TestReduxApp2.jsx"
import TestEditTable from "src/views/TestEditTable/TestEditTable.jsx"



const LOGO_TEXT = 'Cost Pro';
const DATA_BASE_URL = '/api/v1/data';

const DATA_SUB_URL = {
  Table: '/trans_history',
  Category1: '/category_1',
  Category2: '/category_2',
  Category3: '/category_3'
}

//dashboard will show all conclusive data
const APP_ROUTES = [
  {
    path: '/dashboard',
    sidebarName: 'Dashboard',
    icon: DashboardIcon,
    component: Dashboard
  },
  {
    path: '/table',
    sidebarName: 'Table',
    icon: TableChartIcon,
    component: Table
  },
  {
    path: '/category',
    sidebarName: 'Category',
    icon: CategoryIcon,
    component: Category
  },
  {
    path: '/test',
    sidebarName: 'Test',
    icon: HomeIcon,
    component: Test
  },
  {
    path: '/test2',
    sidebarName: 'Test2',
    icon: HomeIcon, 
    component: Test2
  },
  {
    path: '/test_redux_app_1',
    sidebarName: 'Test Redux App 1',
    icon: HomeIcon,
    component: TestReduxApp1
  },
  {
    path: '/test_redux_app_2',
    sidebarName: 'Test Redux App 2',
    icon: HomeIcon,
    component: TestReduxApp2
  },
  {
    path: '/test_edit_table',
    sidebarName: 'Test Edit Table',
    icon: HomeIcon,
    component: TestEditTable
  },
  {
    redirect: true,
    path: '/',
    to: '/dashboard'
  }
]

const CELL_BINDS = {
  action: 'action',
  editable: 'editable'
}

// trans Table
const TABLE_CONFIG_TRANS = {
  title: 'Trans Data',
  defulatPageSize: 10,
  pageSizeOptions: [5, 10, 20],
  columns: [
    {
      Header: 'ID',
      accessor: 'id'
    },
    {
      Header: 'Trans ID',
      accessor: 'trans_id'
    },
    {
      Header: 'Trans Date',
      accessor: 'trans_date'
    },
    {
      Header: 'Amount',
      accessor: 'amount'
    },
    {
      Header: 'Trans Type',
      accessor: 'trans_type'
    },
    {
      Header: 'Card Type',
      accessor: 'card_type'
    },
    {
      Header: 'Description',
      accessor: 'description'
    },
    {
      Header: 'Category 1',
      accessor: 'category_1'
    },
    {
      Header: 'Category 2',
      accessor: 'category_2'
    },
    {
      Header: 'Category 2',
      accessor: 'category_2'
    },
    {
      Header: 'Event',
      accessor: 'event'
    }
  ]
}

// Category table
const TABLE_CONFIG_CATEGORY = {
  title: 'Category 1',
  defulatPageSize: 5,
  pageSizeOptions: [5, 10],
  columns: [
    {
      Header: 'Action',
      width: 200,
      cellBind: CELL_BINDS.action
    },
    {
      Header: 'ID',
      accessor: 'id',
      width: 100,
    },
    {
      Header: 'Category Name',
      accessor: 'name',
      width: 200,
      cellBind: CELL_BINDS.editable
    },
    {
      Header: 'Category Description',
      accessor: 'desc',
      width: 500,
      cellBind: CELL_BINDS.editable
    }
  ]
}

class UTIL {

  static getTrackingKeys(columns) {
    let result = []
    for(let i = 0; i < columns.length; i++) {
      let col = columns[i];
      if(col.accessor == 'id' || col.cellBind == CELL_BINDS.editable) {
        result.push(col.accessor);
      }
    }
    return result
  }
}

export {
  UTIL,
  LOGO_TEXT,
  DATA_BASE_URL,
  DATA_SUB_URL,
  APP_ROUTES,
  CELL_BINDS,
  TABLE_CONFIG_TRANS,
  TABLE_CONFIG_CATEGORY
};