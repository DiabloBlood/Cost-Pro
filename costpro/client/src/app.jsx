import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from "react-router-dom";
// app layout
import AppLayout from "src/global/AppLayout.jsx";



class App extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path='/' component={AppLayout} />
        </Switch>
      </BrowserRouter>
    )
  }
}


ReactDOM.render(<App />, document.getElementById('app'));