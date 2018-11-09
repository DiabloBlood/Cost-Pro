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
import TableToolbar from "src/components/Table/TableToolbar.jsx";

import Divider from '@material-ui/core/Divider';

import Assignment from "@material-ui/icons/Assignment";
import AddShoppingCart from "@material-ui/icons/AddShoppingCart";


import Add from "@material-ui/icons/Add";
import Favorite from "@material-ui/icons/Favorite";
import Build from "@material-ui/icons/Build";

import { cardTitle } from "src/assets/jss/globalStyle.jsx";

import BaseTable from "src/components/Table/BaseTable.jsx"
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes } = this.props;

    return (
      <GridContainer>
        <GridItem xs={12}>
          <Card>
            <TableToolbar title="Category 1">
              <CustomButton color="github" justIcon round>
                <AddShoppingCart />
              </CustomButton>
            </TableToolbar>
            <Divider inset />
            <CardBody>
              <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Category1} tableConfig={TABLE_CONFIG_CATEGORY} />
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    )
  }
}

export default Test;