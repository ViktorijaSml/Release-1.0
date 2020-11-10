function CreateTable() {
   var Phone = new XMLHttpRequest();
   Phone.open('GET', 'https://raw.githubusercontent.com/ViktorijaSml/Release/main/mobiteli.json');
   Phone.onload = function () {
      var data = JSON.parse(Phone.responseText);
      var col = [];
      for (var i = 0; i < data.length; i++) {
         for (var key in data[i]) {
            if (col.indexOf(key) === -1) {
               col.push(key);
            }
         }
      }
      var table = document.createElement("table");
      var tr = table.insertRow(-1);
      for (var i = 0; i < col.length; i++) {
         var th = document.createElement("th");
         th.innerHTML = col[i];
         tr.appendChild(th);
      }
      for (var i = 0; i < data.length; i++) {

         tr = table.insertRow(-1);

         for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = data[i][col[j]];
         }
         var divContainer = document.getElementById("myTable");
         divContainer.innerHTML = "";
         divContainer.appendChild(table);
      }
   }
   Phone.send();
}
function tableToJson(table) {
   var data = [];
   for (var i = 1; i < table.rows.length; i++) {
      var tableRow = table.rows[i];
      var rowData = [];
      for (var j = 0; j < tableRow.cells.length; j++) {
         rowData.push(tableRow.cells[j].innerHTML);;
      }
      data.push(rowData);
   }
   return data;
}
function downloadCSV(csv, filename) {
   var csvFile;
   var downloadLink;

   // CSV file
   csvFile = new Blob([csv], { type: "text/csv" });

   // Download link
   downloadLink = document.createElement("a");

   // File name
   downloadLink.download = filename;

   // Create a link to the file
   downloadLink.href = window.URL.createObjectURL(csvFile);

   // Hide download link
   downloadLink.style.display = "none";

   // Add the link to DOM
   document.body.appendChild(downloadLink);

   // Click download link
   downloadLink.click();
}

function exportTableToCSV(filename) {
   var csv = [];
   var rows = document.querySelectorAll("table tr");

   for (var i = 0; i < rows.length; i++) {
      var row = [], cols = rows[i].querySelectorAll("td, th");

      for (var j = 0; j < cols.length; j++)
         row.push(cols[j].innerText);

      csv.push(row.join(","));
   }

   // Download CSV file
   downloadCSV(csv.join("\n"), filename);
}