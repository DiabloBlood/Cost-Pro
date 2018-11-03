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
    redirect: true,
    path: '/',
    to: '/dashboard'
  }
]

// trans Table
const TABLE_CONFIG_TRANS = {
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
  defulatPageSize: 5,
  pageSizeOptions: [5, 10],
  columns: [
    {
      Header: 'Category Name',
      accessor: 'name'
    },
    {
      Header: 'Category Description',
      accessor: 'desc'
    }
  ]
}

export {
  LOGO_TEXT,
  DATA_BASE_URL,
  DATA_SUB_URL,
  APP_ROUTES,
  TABLE_CONFIG_TRANS,
  TABLE_CONFIG_CATEGORY
};