import React from 'react';

//test CardIcon
import CardIcon from "src/components/Card/CardIcon.jsx";
import Assignment from "@material-ui/icons/Assignment";


class Test extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Testing</h1>
        <CardIcon color="success">
          <Assignment />
        </CardIcon>
      </div>
    )
  }
}

export default Test;