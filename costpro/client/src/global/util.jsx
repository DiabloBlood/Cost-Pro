// global vars
import { CELL_BINDS } from "src/global/globalVars.jsx"



class Util {

  static getTrackingKeys(columns) {
    let result = []
    for(let i = 0; i < columns.length; i++) {
      let col = columns[i];
      if(col.accessor == 'id' || col.cellBind == CELL_BINDS.editable) {
        result.push(col.accessor);
      }
    }
    return result
  }

  static buildTableConfig(tableConfig) {
    tableConfig.trackingKeys = this.getTrackingKeys(tableConfig.columns);
    return tableConfig;
  }
}


export default Util;

