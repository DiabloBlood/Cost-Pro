import React from "react";
import classNames from "classnames";
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// jss assets
import cardBodyStyle from "src/assets/jss/components/cardBodyStyle.jsx";



class CardBody extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, background, color } = this.props;

    let cardBodyClasses = classNames({
      [classes.cardBody]: true,
      [classes.cardBodyBackground]: background, 
      [classes.cardBodyColor]: color,
    });

    return (
      <div className={cardBodyClasses}>
        {children}
      </div>
    );
  }
}


CardBody.propTypes = {
  classes: PropTypes.object.isRequired,
  background: PropTypes.bool,
  color: PropTypes.bool
};

export default withStyles(cardBodyStyle)(CardBody);
