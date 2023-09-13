google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChartBar);
google.charts.setOnLoadCallback(drawChartColumn1);
google.charts.setOnLoadCallback(drawChartColumn2);

var values = document.getElementById("values")
console.log(values.innerHTML);
let cabecera = [['Personal', 'Ingreso/Salidas',{ role: 'style'}]]

var data2= JSON.parse(values.innerHTML)//[["Personal", "Ingreso/Salidas"], ["PERSONAL QUE INGRESO", 5], ["PERSONAL QUE SALIO", 22]]
console.log(data2);
for (var i=0;i<data2.length;i++)
  cabecera.push(data2[i]);
//cabecera.push(data2[1]);
console.log(cabecera);

function drawChartBar() {
  //var data = google.visualization.arrayToDataTable([["Personal", "Ingreso/Salidas"], ["PERSONAL QUE INGRESO", 5], ["PERSONAL QUE SALIO", 22]]);
  //var data = google.visualization.arrayToDataTable(data2);
  var data = google.visualization.arrayToDataTable(cabecera);
  const optionsBar = {
    //title:'Resumen de Ingresos y Salidas por turno',
    hAxis:{
      title: 'Cantidad de personas',
      minValue:0,
      viewWindow:{
          min:0
        }
    },
    legend: 'none',
  };
  const chart = new google.visualization.BarChart(document.getElementById('myChartBar'));
  chart.draw(data, optionsBar);
};
function drawChartColumn1() {
  var dataColumn1 = google.visualization.arrayToDataTable([
    ['Dia', 'Cantidad Ingresos','Cantidad Salidas'],
    ['Lunes',  15,14],
    ['Martes',  16,12],
    ['Miercoles',  12,11],
    ['Jueves',  19,14],
    ['Viernes',  20,25],
    ['Sabado',  43,42],
    ['Domingo',  12,9]  
  ]);
  const optionsColumn1 = {
    title:'Resumen de cantidad entradas y Salidas por semana',
    hAxis:{
      title: 'Dia de semana',
    },
    vAxis:{
      title: 'Cantidad de personas',
      minValue:0,
      viewWindow:{
          min:0
        }
    },
    legend: 'none',
  };
  const chart2 = new google.visualization.ColumnChart(document.getElementById('myChartColumn1'));
  chart2.draw(dataColumn1, optionsColumn1);
};

function drawChartColumn2() {
  var dataColumn2 = google.visualization.arrayToDataTable([
    ['Dia', 'Hora Ingreso', 'Hora Salida'],
    ['Lunes', [11,5,9], [15,5,9]],
    ['Martes', [12,5,9], [17,5,9]],
    ['Miercoles', [10,5,9], [14,5,9]],
    ['Jueves', [5,5,9], [9,5,9]],
    ['Viernes', [6,5,9], [10,5,9]],
    ['Sabado', [7,5,9], [14,5,9]],
    ['Domingo', [8,5,9], [15,5,9]]

  ]);
  const optionsColumn2 = {
    title:'Promedio de horas entradas y Salidas por semana',
    hAxis:{
      title: 'Dia Semana',
    },
    legend: 'none',
  };
  const chart3 = new google.visualization.ColumnChart(document.getElementById('myChartColumn2'));
  chart3.draw(dataColumn2, optionsColumn2);
};
