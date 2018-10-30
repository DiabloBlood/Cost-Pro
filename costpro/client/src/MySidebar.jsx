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



class MySidebar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes, image, logo, logoText, routes } = this.props;

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

    const links = (
      <List className={classes.list}>
        {
          routes.map((route, index) => {
            return (
              <NavLink
                to={route.path}
                className={classes.item}
                activeClassName="active"
                key={index}
              >
                <ListItem button className={classes.itemLink}>
                  <ListItemIcon className={classes.itemIcon}>
                    <route.icon />
                  </ListItemIcon>
                  <ListItemText
                    primary={route.sidebarName}
                    className={classes.itemText}
                    disableTypography={true}
                  />
                </ListItem>
              </NavLink>
            )
          })
        }
      </List>
    );

    return (
      <Drawer
        anchor="left"
        variant="permanent"
        open
        classes={{
          paper: classes.drawerPaper
        }}
      >
        {brand}
        <div className={classes.sidebarWrapper}>{links}</div>
        <div
          className={classes.background}
          style={{ backgroundImage: `url(${image})` }}
        />
      </Drawer>
    )
  }
}

export default withStyles(sidebarStyle)(MySidebar)