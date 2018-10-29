import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter, Route, NavLink } from "react-router-dom";

//import Sidebar from 'src/components/Sidebar.jsx';
import image from 'src/assets/img/sidebar-3.jpg';
import logo from 'src/assets/img/reactlogo.png';
import withStyles from "@material-ui/core/styles/withStyles";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";

import Drawer from "@material-ui/core/Drawer";

import DashboardIcon from "@material-ui/icons/DashboardRounded";
import HomeIcon from "@material-ui/icons/HomeRounded";

import sidebarStyle from "src/assets/jss/styles/components/sidebarStyle.jsx";


const dashboardRoutes = [
  {
    path: '/',
    siderbarName: 'Home',
    icon: HomeIcon
  },
  {
    path: '/dashboard',
    sidebarName: 'Dashboard',
    icon: DashboardIcon
  }
]

const route = {
  path: '/',
  sidebarName: 'Home',
  icon: HomeIcon
}

class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes, image, logo, logoText, route } = this.props;

    const brand = (
      <div className={classes.logo}>
        <a href="https://www.google.com" className={classes.logoLink}>
          <div className={classes.logoImage}>
            <img src={logo} alt="logo" className={classes.img} />
          </div>
          {logoText}
        </a>
      </div>
    );

    return (
      <BrowserRouter>
        <Drawer
          anchor="left"
          variant="permanent"
          open
          classes={{
            paper: classes.drawerPaper
          }}
        >
          {brand}
          <List className={classes.list}>
            <NavLink
              to={route.path}
              className={classes.item}
              activeClassName="active"
            >
              <ListItem button className={classes.itemLink}>
                <ListItemIcon className={classes.itemIcon}>
                  <DashboardIcon />
                </ListItemIcon>
                <ListItemText
                  primary={route.sidebarName}
                  className={classes.itemText}
                />
              </ListItem>
            </NavLink>
          </List>

          <div
            className={classes.background}
            style={{ backgroundImage: `url(${image})` }}
          />
        </Drawer>
      </BrowserRouter>
    )
  }
}

App = withStyles(sidebarStyle)(App)



ReactDOM.render(
    <App
      name="test_app"
      image={image}
      logo={logo}
      logoText={'Cost Pro'}
      route={route}
    />,
    document.getElementById('test_field')
);