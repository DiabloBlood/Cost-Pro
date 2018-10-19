import React from 'react';
import ReactDOM from 'react-dom';

import ReactTable from 'react-table';
import 'react-table/react-table.css';



class App extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [],
      pages: null,
      loading: true
    };
    this.fetchData = this.fetchData.bind(this);
  }
}

class DataGrid extends React.Component {

  constructor() {
    super();
    this.state = {
      data: [],
      pages: null,
      loading: true
    };
    this.fetchData = this.fetchData.bind(this);
  }

  fetchData(state, instance) {
    // Whenever the table model changes, or the user sorts or changes pages,
    // this method gets called and passed the current table model.
    // You can set the `loading` prop of the table to true to use the built-in one
    // or show you're own loading bar if you want.
    this.setState({ loading: true });
    // Request the data however you want.
    requestData(
      state.pageSize,
      state.page,
      state.sorted,
      state.filtered
    ).then(res => {
      // Now just get the rows of data to your React Table (and update anything else like total pages or loading)
      this.setState({
        data: res.rows,
        pages: res.pages,
        loading: false
      });
    });
  }

  render() {
    const { data, pages, loading } = this.state;

    const columns = [
      {
        Header: 'trans_id',
        accessor: 'trans_id'
      }, {
        Header: 'amount',
        accessor: 'amount'
      }
    ]

    return (
      <div>
        <ReactTable
          columns={columns}
          manual // Forces table not to paginate or sort automatically, so we can handle it server-side
          data={data}
          pages={pages} // Display the total number of pages
          loading={loading} // Display the loading overlay when we need it
          onFetchData={this.fetchData} // Request new data when things change
          filterable
          defaultPageSize={10}
          pageSizeOptions={[10, 20]}
          className="-striped -highlight"
        />
      </div>
    )
  }
}

ReactDOM.render(<DataGrid />, document.getElementById('test_field'))