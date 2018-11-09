import React from 'react';
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import Grid from "@material-ui/core/Grid";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
// custom components
import CardHeader from "src/components/Card/CardHeader.jsx";
import CardIcon from "src/components/Card/CardIcon.jsx";
// @material-ui/icons
import Assignment from "@material-ui/icons/Assignment";
import MenuIcon from '@material-ui/icons/Menu';
// jss assets
import tableToolbarStyle from "src/assets/jss/components/tableToolbarStyle.jsx";



class TableToolbar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, title, children } = this.props;

    return (
      <CardHeader icon>
        <Grid container>
          <Grid item xs={2}>
            <CardIcon color="success">
              <Assignment />
            </CardIcon>
          </Grid>
          <Grid item xs={10} className={classes.cardHeaderToolBar}>
            <AppBar position="static" className={classes.toolbarColor}>
              <Toolbar variant="dense">
                <IconButton className={classes.menuButton} color="inherit">
                  <MenuIcon />
                </IconButton>
                <Typography variant="h6" color="inherit">
                  { title }
                </Typography>
                <div className={classes.grow} />
                { children }
              </Toolbar>
            </AppBar>
          </Grid>
        </Grid>
      </CardHeader>
    )
  }
}


TableToolbar.propTypes = {
  classes: PropTypes.object.isRequired,
  toolbarTitle: PropTypes.string
};


export default withStyles(tableToolbarStyle)(TableToolbar);