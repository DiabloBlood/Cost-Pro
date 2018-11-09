import React from 'react';

import Grid from "@material-ui/core/Grid";
import withStyles from "@material-ui/core/styles/withStyles";
//test CardIcon
import GridContainer from "src/components/Grid/GridContainer.jsx";
import GridItem from "src/components/Grid/GridItem.jsx";
import Card from "src/components/Card/Card.jsx";
import CardBody from "src/components/Card/CardBody.jsx";
import CardHeader from "src/components/Card/CardHeader.jsx";
import CardIcon from "src/components/Card/CardIcon.jsx";
import CustomButton from "src/components/CustomButton.jsx";

import Divider from '@material-ui/core/Divider';

import Assignment from "@material-ui/icons/Assignment";


import Add from "@material-ui/icons/Add";
import Favorite from "@material-ui/icons/Favorite";
import Build from "@material-ui/icons/Build";

import { cardTitle } from "src/assets/jss/globalStyle.jsx";

import BaseTable from "src/components/BaseTable.jsx"
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



const styles = {
  cardIconTitle: {
    ...cardTitle,
    marginTop: "15px",
    marginBottom: "0px"
  },
  /*Avoid card header overide svg css*/
  cardHeaderToolBar: {
    "& svg": {
      margin: "-5px 0px"
    }
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
        <GridContainer>
          <GridItem xs={12}>
            <Card>
              <CardHeader icon>
                <Grid container>
                  <Grid item xs={3}>
                    <CardIcon color="success">
                      <Assignment />
                    </CardIcon>
                    <h3 className={classes.cardIconTitle}>Category 1</h3>
                  </Grid>
                  <Grid item xs={9} className={classes.cardHeaderToolBar}>
                    <CustomButton color="github" round>
                      <Add />
                      Add
                    </CustomButton>
                  </Grid>
                </Grid>
              </CardHeader>
              <Divider inset />
              <CardBody>
                <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Category1} tableConfig={TABLE_CONFIG_CATEGORY} />
              </CardBody>
            </Card>
          </GridItem>
        </GridContainer> 
      </div>
    )
  }
}

export default withStyles(styles)(Test);