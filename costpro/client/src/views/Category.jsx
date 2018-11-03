import React from 'react';
import BaseTable from "src/components/BaseTable.jsx"
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



class Category extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Category1} tableConfig={TABLE_CONFIG_CATEGORY} />
        <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Category2} tableConfig={TABLE_CONFIG_CATEGORY} />
        <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Category3} tableConfig={TABLE_CONFIG_CATEGORY} />
      </div>
    )
  }
}

export default Category;