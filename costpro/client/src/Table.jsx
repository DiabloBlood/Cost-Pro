import React from 'react';
import ReactDOM from 'react-dom';

import ReactTable from 'react-table';
import axios from 'axios'

import 'react-table/react-table.css';



class Table extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      columns: [],
      data: [],
      page: 1,
      pageSize: 10,
      pages: null,
      loading: true
    };
    this.fetchData = this.fetchData.bind(this);
  }

  shouldComponentUpdate(nextProps, nextState) {
    if(nextState.columns.length == 0 && nextState.data.length == 0) {
      return false;
    }
    return true;
  }

  componentDidMount() {
    let url = '/api/v1/columns/TransHistory'
    axios.get(url).then((res) => {
      this.setState({
        columns: res.data.columns,
      });
    }).catch((err) => {
      throw "Load columns failed!"
    });
  }

  fetchData(state, instance) {
    // Whenever the table model changes, or the user sorts or changes pages,
    // this method gets called and passed the current table model.
    // You can set the `loading` prop of the table to true to use the built-in one
    // or show you're own loading bar if you want.

    this.setState({
      loading: true
    });

    let queryParams = {
      page: state.page + 1,
      pageSize: state.pageSize,
      sorted: state.sorted,
      filtered: state.filtered
    }

    //Request the data however you want.

    let url = '/api/v1/data';
    let params = {
      params: {
        value: btoa(JSON.stringify(queryParams))
      }
    }

    axios.get(url, params).then((res) => {
      this.setState({
        data: res.data.rows,
        pages: res.data.total_pages,
        page: state.page + 1,
        pageSize: state.pageSize,
        loading: false
      });
    }).catch((err) => {
      throw "Load server-side data failed!"
    });
  }

  render() {
    const {columns, data, page, pageSize, pages, loading} = this.state;

    return (
      <div>
        <ReactTable
          manual // Forces table not to paginate or sort automatically, so we can handle it server-side
          columns={columns}
          data={data}
          pages={pages} // Display the total number of pages
          loading={loading} // Display the loading overlay when we need it
          onFetchData={this.fetchData} // Request new data when things change
          filterable
          defaultPageSize={10}
          pageSizeOptions={[5, 10, 20]}
          className="-striped -highlight"
        />
      </div>
    )
  }
}


export default Table
//ReactDOM.render(<Table />, document.getElementById('dashboard'))