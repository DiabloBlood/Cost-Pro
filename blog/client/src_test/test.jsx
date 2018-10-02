import React from 'react';
import ReactDOM from 'react-dom';



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

ReactDOM.render(
    <ShoppingList name="test" />,
    document.getElementById('test_field')
);