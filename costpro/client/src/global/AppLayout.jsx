import React from 'react';
import { Redirect, Switch, Route, NavLink } from "react-router-dom";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import Sidebar from "src/components/Sidebar.jsx";
// global vars
import { LOGO_TEXT, APP_ROUTES } from "src/global/globalVars.jsx";
// image assets
import image from 'src/assets/img/sidebar-3.jpg';
import logo from 'src/assets/img/reactlogo.png';
//jss assets
import appLayoutStyle from "src/assets/jss/appLayoutStyle.jsx";



class AppLayout extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { classes, ...rest } = this.props;

    const switchRoutes = (
      <Switch>
        {
          APP_ROUTES.map((route, index) => {
            if(route.redirect) {
              return <Redirect from={route.path} to={route.to} key={index} />;
            }
            return (
              <Route path={route.path} component={route.component} key={index} />
            );
          })
        }
      </Switch>
    )

    return (
      <div className={classes.wrapper}>
        <Sidebar
          image={image}
          logo={logo}
          logoText={LOGO_TEXT}
          routes={APP_ROUTES}
          color="blue"
          {...rest}
        />
        <div className={classes.mainPanel} ref="mainPanel">
          <div className={classes.content}>
            <div className={classes.container}>{switchRoutes}</div>
          </div>
        </div>
      </div>
    )
  }
}

export default withStyles(appLayoutStyle)(AppLayout);