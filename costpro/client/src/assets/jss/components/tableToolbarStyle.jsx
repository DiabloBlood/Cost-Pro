


const tableToolbarStyle = {
  /*Avoid card header overide svg css*/
  cardHeaderToolBar: {
    "& svg": {
      margin: "-5px 0px"
    }
  },
  grow: {
    flexGrow: 1
  },
  menuButton: {
    marginLeft: -18,
    marginRight: 10,
  },
  toolbarColor: {
    borderRadius: "10px",
    backgroundColor: "#8A8A8A",
    color: "#fff",
    boxShadow:
      "0 2px 2px 0 rgba(51, 51, 51, 0.14), 0 3px 1px -2px rgba(51, 51, 51, 0.2), 0 1px 5px 0 rgba(51, 51, 51, 0.12)",
    "&:hover,&:focus": {
      backgroundColor: "#8A8A8A",
      color: "#fff",
      boxShadow:
        "0 14px 26px -12px rgba(51, 51, 51, 0.42), 0 4px 23px 0px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(51, 51, 51, 0.2)"
    }
  }
}

export default tableToolbarStyle;