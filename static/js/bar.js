var $calorieChart = $("#myChart");
$.ajax({
  url: $calorieChart.data("url"),
  success: function (data) {


    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Breakfast', 'Lunch', 'Snacks', 'Dinner'],
            datasets: [{
                data: data.data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    }
});



// var $populationChart = $("#population-chart");
// $.ajax({
//   url: $populationChart.data("url"),
//   success: function (data) {

//     var ctx = $populationChart[0].getContext("2d");

//     new Chart(ctx, {
//       type: 'bar',
//       data: {
//         labels: data.labels,
//         datasets: [{
//           label: 'Calories',
//           backgroundColor: 'blue',
//           data: data.data
//         }]          
//       },
//       options: {
//         responsive: true,
//         legend: {
//           position: 'top',
//         }
//       }
//     });

 