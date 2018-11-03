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

export {
  LOGO_TEXT,
  APP_ROUTES
};