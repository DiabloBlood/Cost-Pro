import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from "react-router-dom";
// app layout
import AppLayout from "src/AppLayout.jsx";



ReactDOM.render(
  <BrowserRouter>
      <Route
        path='/'
        component={AppLayout}
      />
  </BrowserRouter>,
  document.getElementById('app')
);