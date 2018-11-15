import React from 'react';
import EditTable from "src/components/Table/EditTable.jsx";

import { DATA_BASE_URL, DATA_SUB_URL, TABLE_CONFIG_CATEGORY } from "src/global/globalVars.jsx"



class Test2 extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <EditTable
        url={DATA_BASE_URL + DATA_SUB_URL.Category1}
        tableConfig={TABLE_CONFIG_CATEGORY}
      />
    )
  }
}

export default Test2;