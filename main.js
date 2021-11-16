var barSvg;
var barWidth;
var barHeight;
var barInnerWidth;
var barInnerHeight;
var barMargin = {top: 20, right: 60, bottom: 60, left: 100}

var toolTip;  

document.addEventListener('DOMContentLoaded', function() {
    barSvg = d3.select('#spotify-barchart');
    barWidth = +barSvg.style('width').replace('px','');
    barHeight = +barSvg.style('height').replace('px','');;
    barInnerWidth = barWidth - barMargin.left - barMargin.right;
    barInnerHeight = barHeight - barMargin.top - barMargin.bottom;
    toolTip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);
});

// draws the bar chart 
function drawBar()
{
    const currentMetric = document.getElementById('metric-select').value;

    fetch(`http://localhost:5000/spotifyData?metric=${currentMetric}`)
    .then(response => response.json())
    .then(data => console.log(data));
}