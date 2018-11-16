import React from "react";
import classNames from "classnames";
import PropTypes from "prop-types";
// material-ui components
import withStyles from "@material-ui/core/styles/withStyles";
import Button from "@material-ui/core/Button";
// jss assets
import customButtonStyle from "src/assets/jss/components/customButtonStyle.jsx";



class CustomButton extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { classes, color, round, children, disabled, simple, size, justIcon, className, ...rest } = this.props;

    let btnClasses = classNames({
      [classes.button]: true,
      [classes[color]]: color,
      [classes.round]: round,
      [classes.disabled]: disabled,
      [classes.simple]: simple,
      [classes[size]]: size,
      [classes.justIcon]: justIcon,
      [className]: className
    });

    return (
      <Button className={btnClasses} {...rest}>
        {children}
      </Button>
    );
  }
}


CustomButton.propTypes = {
  classes: PropTypes.object.isRequired,
  className: PropTypes.string,
  color: PropTypes.oneOf([
    "primary",
    "info",
    "success",
    "warning",
    "danger",
    "rose",
    "white",
    "twitter",
    "facebook",
    "google",
    "linkedin",
    "pinterest",
    "youtube",
    "tumblr",
    "github",
    "behance",
    "dribbble",
    "reddit",
    "transparent"
  ]),
  size: PropTypes.oneOf(["sm", "lg"]),
  simple: PropTypes.bool,
  round: PropTypes.bool,
  disabled: PropTypes.bool,
  justIcon: PropTypes.bool
};

export default withStyles(customButtonStyle)(CustomButton);
