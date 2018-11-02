import React from 'react';
import classNames from "classnames";
import { NavLink } from "react-router-dom";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import Drawer from "@material-ui/core/Drawer";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
// jss assets
import sidebarStyle from "src/assets/jss/components/sidebarStyle.jsx";



class Sidebar extends React.Component {

  constructor(props) {
    super(props);
  }

  isRouteActive(routeName) {
    return this.props.location.pathname.indexOf(routeName) > -1 ? true : false;
  }

  render() {
    const { classes, logo, logoText, routes, color, image } = this.props;

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

            if (route.redirect) {
              return null;
            }

            let listItemClasses = classNames({
              [' ' + classes[color]]: this.isRouteActive(route.path)
            });

            let whiteFontClasses = classNames({
              [' ' + classes.whiteFont]: this.isRouteActive(route.path)
            });

            return (
              <NavLink
                to={route.path}
                className={classes.item}
                activeClassName="active"
                key={index}
              >
                <ListItem button className={classes.itemLink + listItemClasses}>
                  <ListItemIcon className={classes.itemIcon + whiteFontClasses}>
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

export default withStyles(sidebarStyle)(Sidebar);