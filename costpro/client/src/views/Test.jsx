import React from 'react';

import withStyles from "@material-ui/core/styles/withStyles";
//test CardIcon
import CardHeader from "src/components/Card/CardHeader.jsx";
import CardIcon from "src/components/Card/CardIcon.jsx";
import Assignment from "@material-ui/icons/Assignment";
import { cardTitle } from "src/assets/jss/globalStyle.jsx";



const styles = {
  cardIconTitle: {
    ...cardTitle,
    marginTop: "15px",
    marginBottom: "0px"
  }
};

class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes } = this.props;

    return (
      <div>
        <h1>Testing</h1>
        <CardHeader color="primary" icon>
          <CardIcon color="success">
            <Assignment />
          </CardIcon>
          <h4 className={classes.cardIconTitle}>React Table</h4>
        </CardHeader>
      </div>
    )
  }
}

export default withStyles(styles)(Test);