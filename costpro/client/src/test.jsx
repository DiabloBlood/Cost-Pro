import React from 'react';
import ReactDOM from 'react-dom';

import Sidebar from 'src/components/Sidebar.jsx';
//import image from './assets/img/sidebar-3.jpg';
//import logo from './assets/img/reactlogo.png';


class App extends React.component {
  render() {
    return (
      <Sidebar
        logoText={"Creative Tim"}
        color="blue"
      />
    )
  }
}



ReactDOM.render(
    <App name="test_app" />,
    document.getElementById('test_field')
);