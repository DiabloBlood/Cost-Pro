import React from "react";
import classNames from "classnames";
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// jss assets
import cardStyle from "src/assets/jss/components/cardStyle.jsx";



class Card extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, children, background, color } = this.props;

    let cardClasses = classNames({
      [classes.card]: true,
      [classes.cardBackground]: background,
      [classes[color]]: color
    });

    return (
      <div className={cardClasses}>
        {children}
      </div>
    );
  }
}


Card.propTypes = {
  classes: PropTypes.object.isRequired,
  background: PropTypes.bool,
  color: PropTypes.oneOf([
    "primary",
    "info",
    "success",
    "warning",
    "danger",
    "rose"
  ])
};

export default withStyles(cardStyle)(Card);
