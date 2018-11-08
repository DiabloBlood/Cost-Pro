import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import Grid from "@material-ui/core/Grid";



const style = {
  grid: {
    margin: "0 -15px",
    width: "calc(100% + 30px)"
  }
}


class GridContainer extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, ...rest } = this.props;

    return (
      <Grid container className={classes.grid} {...rest}>
        {children}
      </Grid>
    )
  }
}

export default withStyles(style)(GridContainer);
