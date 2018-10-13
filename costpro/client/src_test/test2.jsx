import React from 'react';
import ReactDOM from 'react-dom';

import ReactTable from 'react-table';
import 'react-table/react-table.css';



class DataGrid extends React.Component {

  render() {
    const data = [{
      name: 'Tom1',
      age: 26
    }, {
      name: 'Tom2',
      age: 36
    }]

    const columns = [
      {
        Header: 'Name',
        accessor: 'name'
      }, {
        Header: 'Age',
        accessor: 'age'
      }
    ]

    return (
      <div>
        <ReactTable
          data={data}
          columns={columns}
          defaultPageSize={3}
          pageSizeOptions={[3, 6]}
        />
      </div>
    )
  }
}

ReactDOM.render(<DataGrid />, document.getElementById('test_field'))