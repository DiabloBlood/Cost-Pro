import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import Grid from "@material-ui/core/Grid";



const style = {
  grid: {
    padding: "0 15px !important"
  }
}


class GridItem extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, ...rest } = this.props;

    return (
      <Grid item className={classes.grid} {...rest}>
        {children}
      </Grid>
    )
  }
}

export default withStyles(style)(GridItem);
