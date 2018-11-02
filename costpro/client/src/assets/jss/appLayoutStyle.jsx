import {
  drawerWidth,
  container
} from "src/assets/jss/globalStyle.jsx";



const appLayoutStyle = theme => ({
  wrapper: {
    position: "relative",
    top: "0",
    height: "100vh"
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
    marginTop: "70px",
    padding: "30px 15px",
    minHeight: "calc(100vh - 123px)"
  },
  container
});


export default appLayoutStyle;
