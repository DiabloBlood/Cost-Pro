import React from 'react';
import ReactDOM from 'react-dom';
import { Redirect, Route, NavLink } from "react-router-dom";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import MySidebar from "src/MySidebar.jsx";
import Table from "src/Table.jsx"
// @material-ui/icons
import DashboardIcon from "@material-ui/icons/Dashboard";
import HomeIcon from "@material-ui/icons/Home";
import TableChartIcon from "@material-ui/icons/TableChart";
// image assets
import image from 'src/assets/img/sidebar-3.jpg';
import logo from 'src/assets/img/reactlogo.png';
//jss assets
import appLayoutStyle from "src/assets/jss/appLayoutStyle.jsx";




const LOGO_TEXT = 'Cost Pro';

class Dashboard extends React.Component {

  constructor(props) {
    console.log(props);
    super(props);
  }

  render() {
    return (
      <h1>Flask + Webpack + Babel + React</h1>
    )
  }
}


class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>Testing</h1>
    )
  }
}


//dashboard will show all conclusive data
const appRoutes = [
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
    path: '/test',
    sidebarName: 'TEST',
    icon: HomeIcon, 
    component: Test
  },
  {
    redirect: true,
    path: '/',
    to: '/dashboard'
  }
]



class AppLayout extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const classes = this.props.classes;

    let routes = appRoutes;

    const compRoutes = (
      <div>
        {
          routes.map((route, index) => {
            if(route.redirect) {
              return <Redirect from={route.path} to={route.to} key={index} />;
            }
            return (
              <Route
                path={route.path}
                component={route.component}
                key={index}
              />
            )
          })
        }
      </div>
    )


    return (
      <div className={classes.wrapper}>
        <MySidebar
          image={image}
          logo={logo}
          logoText={LOGO_TEXT}
          routes={routes}
        />
        <div className={classes.mainPanel} ref="mainPanel">
          <div className={classes.content}>
            <div className={classes.container}>{compRoutes}</div>
          </div>
        </div>
      </div>
    )
  }
}

export default withStyles(appLayoutStyle)(AppLayout)