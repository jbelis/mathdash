$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            type: 'spline',
            zoomType: 'xy',
            renderTo: 'container'
        },
        title: {
            text: 'Your scores over time'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000,
            title: {
            	text: 'Time'
            }
        },
        yAxis: {
            title: {
                text: 'Score',
                //margin: 80
            },
            min: 0
        },
        series: history
    });        
});