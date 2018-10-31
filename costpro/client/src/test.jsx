import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, NavLink } from "react-router-dom";
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



class Dashboard extends React.Component {

  constructor(props) {
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
  }
]



class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes, image, logo, logoText, routes } = this.props;

    const compRoutes = (
      <div>
        {
          routes.map((route, index) => {
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
          logoText={logoText}
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

App = withStyles(appLayoutStyle)(App)


ReactDOM.render(
  <BrowserRouter>
    <App
      name="test_app"
      image={image}
      logo={logo}
      logoText={'Cost Pro'}
      routes={appRoutes}
    />
  </BrowserRouter>,
  document.getElementById('test_field')
);