var wpWidth =21, wpWidthStr = `${wpWidth}cm`, wpHeight = 29.7, wpHeightStr = `${wpHeight}cm`;
var xDivStyles = {};
var pxPerCm = null;
$(document).ready(function () {
  let wPx = $('#label-page-div').outerWidth();
  pxPerCm = wPx/wpWidth;
});

document.addEventListener('alpine:init', () => {
  Alpine.store('xDivStyles', {
    xWidth: wpWidthStr,
    xHeight: wpHeightStr
  })
  xDivStyles = Alpine.store('xDivStyles');
})

var tabledata = [
  {
    id: 1,
    name_cn: "Billy Bob",
    name_ro: "Billy Bob",
    bbd: "22/05/2025",
    masa_net: '500ml',
    age: "12",
    gender: "male",
    height: 1,
    col: "red",
    dob: "",
    cheese: 1,
  }
];
//create Tabulator on DOM element with id "example-table"
$(document).ready(function () {
  var table = new Tabulator("#example-table", {
    height: 205, // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    data: tabledata, //assign data to table
    layout: "fitDataFill",
    responsiveLayout: "collapse",
    rowHeader: {
      formatter: "responsiveCollapse",
      width: 30,
      minWidth: 30,
      hozAlign: "center",
      resizable: false,
      headerSort: false,
    },
    autoColumns: true,
    autoColumnsDefinitions: [
      { field: "name", editor: "input" }, //add input editor to the name column
    ],
    responsiveLayoutCollapseFormatter: function (data) {
      var list = document.createElement("ul");
      data.forEach(function (col) {
        let item = document.createElement("li");
        item.innerHTML = "<strong>" + col.title + "</strong> - " + col.value;
        list.appendChild(item);
      });
      return Object.keys(data).length ? list : "";
    },
  });
});
