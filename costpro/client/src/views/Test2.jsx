import React from 'react';
import classNames from "classnames";
import withStyles from "@material-ui/core/styles/withStyles";
//test CardIcon

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import Icon from '@material-ui/core/Icon';
import MenuIcon from '@material-ui/icons/Menu';


import GridContainer from "src/components/Grid/GridContainer.jsx";
import GridItem from "src/components/Grid/GridItem.jsx";
import Card from "src/components/Card/Card.jsx";
import CardBody from "src/components/Card/CardBody.jsx";
import CardHeader from "src/components/Card/CardHeader.jsx";
import CardIcon from "src/components/Card/CardIcon.jsx";
import CustomButton from "src/components/CustomButton.jsx";

import Assignment from "@material-ui/icons/Assignment";

import Grid from "@material-ui/core/Grid";

import Add from "@material-ui/icons/Add";
import AddShoppingCart from "@material-ui/icons/AddShoppingCart";


import {
  containerFluid,
  defaultFont,
  primaryColor,
  defaultBoxShadow,
  infoColor,
  successColor,
  warningColor,
  dangerColor
} from "src/assets/jss/globalStyle.jsx";



const styles = {
  /*Avoid card header overide svg css*/
  cardHeaderToolBar: {
    "& svg": {
      margin: "-5px 0px"
    }
  },
  menuButton: {
    marginLeft: -18,
    marginRight: 10,
  },
  primary: {
    backgroundColor: primaryColor,
    color: "#FFFFFF",
    ...defaultBoxShadow
  },
  info: {
    backgroundColor: infoColor,
    color: "#FFFFFF",
    ...defaultBoxShadow
  },
  success: {
    backgroundColor: successColor,
    color: "#FFFFFF",
    borderRadius: "15px"
  },
  warning: {
    backgroundColor: warningColor,
    color: "#FFFFFF",
    ...defaultBoxShadow
  },
  danger: {
    backgroundColor: dangerColor,
    color: "#FFFFFF",
    ...defaultBoxShadow
  },
  github: {
    borderRadius: "10px",
    backgroundColor: "#8A8A8A",
    color: "#fff",
    boxShadow:
      "0 2px 2px 0 rgba(51, 51, 51, 0.14), 0 3px 1px -2px rgba(51, 51, 51, 0.2), 0 1px 5px 0 rgba(51, 51, 51, 0.12)",
    "&:hover,&:focus": {
      backgroundColor: "#8A8A8A",
      color: "#fff",
      boxShadow:
        "0 14px 26px -12px rgba(51, 51, 51, 0.42), 0 4px 23px 0px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(51, 51, 51, 0.2)"
    }
  },
  grow: {
    flexGrow: 1
  },
  buttonSection: {
    display: "flex"
  }
};

class TableToolbar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, color } = this.props;

    let appBarClasses = classNames({
      [' ' + classes[color]]: color
    })

    return (
      <Card>
        <CardHeader icon>
          <Grid container>
            <Grid item xs={2}>
              <CardIcon color="success">
                <Assignment />
              </CardIcon>
            </Grid>
            <Grid item xs={10} className={classes.cardHeaderToolBar}>
              <AppBar position="static" className={classes.github}>
                <Toolbar variant="dense">
                  <IconButton className={classes.menuButton} color="inherit">
                    <MenuIcon />
                  </IconButton>
                  <Typography variant="h6" color="inherit">
                    Category 1
                  </Typography>
                  <div className={classes.grow} />
                  <CustomButton color="github" justIcon round>
                    <AddShoppingCart />
                  </CustomButton>
                </Toolbar>
              </AppBar>
            </Grid>
          </Grid>
        </CardHeader>
      </Card>
    )
  }
}

TableToolbar = withStyles(styles)(TableToolbar)

class Test2 extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes } = this.props;

    return (
      <TableToolbar color="success" />
    )
  }
}

export default Test2;