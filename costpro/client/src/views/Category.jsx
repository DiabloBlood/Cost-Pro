import React from 'react';
import ReactTable from 'react-table';
import axios from 'axios'



const COLUMNS_CAT1 = [
  {
    Header: 'Category Name',
    accessor: 'name_1'
  },
  {
    Header: 'Category Description',
    accessor: 'desc_1'
  }
]

class Cat1 extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      columns: this.props.columns,
      data: [],
      page: 1,
      pageSize: 5,
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

    //Request the data however you want.

    let url = '/api/v1/category';
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
          manual
          columns={columns}
          data={data}
          pages={pages}
          loading={loading}
          onFetchData={this.fetchData}
          filterable
          defaultPageSize={5}
          pageSizeOptions={[5, 10]}
          className="-striped -highlight"
        />
      </div>
    )
  }
}


class Category extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Cat1 columns={COLUMNS_CAT1} />
    )
  }
}

export default Category;