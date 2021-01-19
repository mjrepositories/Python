 // Create firs chart with general coverage
var ctx = document.getElementById('myChart').getContext('2d');
        ctx.canvas.width = 500;
        ctx.canvas.height = 300;
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',
    // The data for our dataset
    data: {
        labels: dates,
        datasets: [{
            label: 'Coverage of rates in %',
            backgroundColor: colors,
            borderColor: 'rgb(255, 99, 132)',
            data: daily
        }]
    },

    // Configuration options go here
    options: {
        responsive: false,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    min:90   // minimum value will be 90.
                }
            }]
          }

    }
});