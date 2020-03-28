function createChart({id, type, labels, datasets, yAxesStepSize, aspectRatio=2}){

    console.log(datasets);
    var ctx = document.getElementById(id).getContext('2d');
    var chartOptions = {
        aspectRatio: aspectRatio,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    };
    if (yAxesStepSize) {
        chartOptions.scales.yAxes[0].ticks.stepSize = yAxesStepSize;
    }
    var myChart = new Chart(ctx, {
        type: type,
        data: {
            labels: labels,
            datasets: datasets
        },
        options: chartOptions
    });

};

