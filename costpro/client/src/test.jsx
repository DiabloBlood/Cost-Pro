import React from 'react';
import ReactDOM from 'react-dom';

//import Sidebar from 'src/components/Sidebar.jsx';
//import image from './assets/img/sidebar-3.jpg';
//import logo from './assets/img/reactlogo.png';
import withStyles from "@material-ui/core/styles/withStyles";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";


import Dashboard from "@material-ui/icons/Dashboard";

import sidebarStyle from "src/assets/jss/styles/components/sidebarStyle.jsx";


class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes } = this.props;

    return (
      <div>
        <List className={classes.list}>
          <ListItem button className={classes.itemLink}>
            <ListItemIcon className={classes.itemIcon}>
              <Dashboard />
            </ListItemIcon>
            <ListItemText primary={'Dashboard'} className={classes.itemText}>
            </ListItemText>
          </ListItem>
        </List>
      </div>
    )
  }
}

App = withStyles(sidebarStyle)(App)



ReactDOM.render(
    <App name="test_app" />,
    document.getElementById('test_field')
);