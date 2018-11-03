import React from 'react';
import BaseTable from "src/components/BaseTable.jsx"
import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_TRANS } from "src/global/globalVars.jsx"



class Table extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <BaseTable url={DATA_BASE_URL + DATA_SUB_URL.Table} tableConfig={TABLE_CONFIG_TRANS} />
      </div>
    )
  }
}

export default Table;