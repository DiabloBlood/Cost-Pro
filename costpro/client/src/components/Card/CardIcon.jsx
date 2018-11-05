import React from "react";
import classNames from "classnames";
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// jss assets
import cardIconStyle from "src/assets/jss/components/cardIconStyle.jsx";



class CardIcon extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, color } = this.props;

    let cardIconClasses = classNames({
      [classes.cardIcon]: true,
      [classes[color + "CardHeader"]]: color
    });

    return (
      <div className={cardIconClasses}>
        {children}
      </div>
    )
  }
}


CardIcon.propTypes = {
  classes: PropTypes.object.isRequired,
  //className: PropTypes.string,
  color: PropTypes.oneOf([
    "warning",
    "success",
    "danger",
    "info",
    "primary",
    "rose"
  ])
};

export default withStyles(cardIconStyle)(CardIcon);
