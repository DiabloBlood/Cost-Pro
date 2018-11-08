import {
  drawerWidth,
  container
} from "src/assets/jss/globalStyle.jsx";



const appLayoutStyle = {
  wrapper: {
    position: "relative",
    top: "0",
    height: "100%"
  },
  mainPanel: {
    width: `calc(100% - ${drawerWidth}px)`,
    overflow: "auto",
    position: "relative",
    float: "right",
    maxHeight: "100%",
    //overflowScrolling: "touch" //for mobile usage
  },
  content: {
    marginTop: "20px",
    padding: "5x 5px",
    //minHeight: "calc(100vh - 123px)"
  },
  container
}


export default appLayoutStyle;
