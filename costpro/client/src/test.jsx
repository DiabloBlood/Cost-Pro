import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter, Route, NavLink } from "react-router-dom";

import MySidebar from "src/MySidebar.jsx";


import DashboardIcon from "@material-ui/icons/Dashboard";
import HomeIcon from "@material-ui/icons/Home";
import image from 'src/assets/img/sidebar-3.jpg';
import logo from 'src/assets/img/reactlogo.png';


class Dashboard extends React.Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <h1>Flask + Webpack + Babel + React</h1>
    )
  }
}

class Test extends React.Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <h1>Testing</h1>
    )
  }
}


//dashboard will show all conclusive data
const dashboardRoutes = [
  {
    path: '/dashboard',
    siderbarName: 'Home',
    icon: DashboardIcon,
    component: Dashboard
  },
  {
    path: '/table',
    sidebarName: 'Table',
    icon: DashboardIcon,
    //component: 
  },
  {
    path: '/test',
    sidebarName: 'TEST'
    icon: HomeIcon, 
    component: Test
  }
]



class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes, image, logo, logoText, route } = this.props;

    return (
      <MySidebar
        image={image}
        logo={logo}
        logoText={logoText}
        route={route}
      />
    )
  }
}


ReactDOM.render(
  <BrowserRouter>
    <App
      name="test_app"
      image={image}
      logo={logo}
      logoText={'Cost Pro'}
      route={route}
    />
  </BrowserRouter>,
  document.getElementById('test_field')
);