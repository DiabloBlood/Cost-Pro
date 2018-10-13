import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button'



class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h2>Shopping List for {this.props.name}</h2>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

const App = () => {
    return (
      <Button variant="contained" color="primary">Hello World</Button>
    );
};

ReactDOM.render(
    <ShoppingList name="test" />,
    document.getElementById('test_field')
);

ReactDOM.render(
    <App name="test_button" />,
    document.getElementById('test_field')
);