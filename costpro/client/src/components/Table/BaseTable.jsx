import React from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
// css
import 'react-table/react-table.css';



class BaseTable extends React.Component {

  constructor(props) {
    super(props);

    let { columns, defulatPageSize } = this.props.tableConfig;

    this.state = {
      columns: columns,
      data: [],
      page: 1,
      pageSize: defulatPageSize,
      pages: null,
      loading: true
    };
    this.fetchData = this.fetchData.bind(this);
  }

  fetchData(state, instance) {
    this.setState({
      loading: true
    });

    let queryParams = {
      page: state.page + 1,
      pageSize: state.pageSize,
      sorted: state.sorted,
      filtered: state.filtered
    }

    let url = this.props.url;
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
    let { data, pages, loading } = this.state;
    let { columns, defulatPageSize, pageSizeOptions } = this.props.tableConfig;


    return (
      <ReactTable
        manual
        columns={columns}
        data={data}
        pages={pages}
        loading={loading}
        onFetchData={this.fetchData}
        filterable
        defaultPageSize={defulatPageSize}
        pageSizeOptions={pageSizeOptions}
        className="-striped -highlight"
      />
    )
  }
}

export default BaseTable;