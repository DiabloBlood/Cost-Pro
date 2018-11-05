import React from "react";
import classNames from "classnames";
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// jss assets
import cardHeaderStyle from "src/assets/jss/components/cardHeaderStyle.jsx";



class CardHeader extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, color, icon } = this.props;

    console.log(classes);

    let cardHeaderClasses = classNames({
      [classes.cardHeader]: true,
      [classes[color + "CardHeader"]]: color,
      [classes.cardHeaderIcon]: icon,
    });

    return (
      <div className={cardHeaderClasses}>
        {children}
      </div>
    );
  }
}


CardHeader.propTypes = {
  classes: PropTypes.object.isRequired,
  color: PropTypes.oneOf([
    "warning",
    "success",
    "danger",
    "info",
    "primary",
    "rose"
  ]),
  icon: PropTypes.bool,
}

export default withStyles(cardHeaderStyle)(CardHeader);