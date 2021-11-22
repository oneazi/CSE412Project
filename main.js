var barSvg;
var barWidth;
var barHeight;
var barInnerWidth;
var barInnerHeight;
var barMargin = {top: 40, right: 40, bottom: 80, left: 100}

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

// disable the input textbox if "artist" is the value chosen in the dropdown
function checkOption() {
    if (document.getElementById('metric-select').value === 'artistp' || document.getElementById('metric-select').value === 'artistf') {
        document.getElementById('name-input').disabled = true;
        document.getElementById('name-input').value = '';
    }
    else {
        document.getElementById('name-input').disabled = false;
    }
}

// hepler function to capitalize the first letter in a word
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// draws the bar chart 
function drawBar()
{
    const currentMetric = document.getElementById('metric-select').value;
    const currentArtist = document.getElementById('name-input').value.trim();

    if (currentMetric === 'artistf') {
        fetch(`http://localhost:5000/artist/followers`)
        .then(response => response.json())
        .then(data => drawArtistBar(data, 'Followers'))
        .catch((error) => {
            console.log(error)
        });
    }
    else if (currentMetric === 'artistp') {
        fetch(`http://localhost:5000/artist/popularity`)
        .then(response => response.json())
        .then(data => drawArtistBar(data, 'Popularity'))
        .catch((error) => {
            console.log(error)
        });
    }
    else if (currentMetric === 'album') {
        if (currentArtist === '')
        {
            fetch(`http://localhost:5000/album`)
            .then(response => response.json())
            .then(data => drawAlbumBar(data, currentArtist))
            .catch((error) => {
                console.log(error)
            });
        }
        else {
            fetch(`http://localhost:5000/album/artist?artist=${currentArtist}`)
            .then(response => response.json())
            .then(data => drawAlbumBar(data, currentArtist))
            .catch((error) => {
                console.log(error)
            });
        }
    }
    else {
        if (currentArtist === '')
        {
            fetch(`http://localhost:5000/metric?metric=${currentMetric}`)
            .then(response => response.json())
            .then(data => drawMetricBar(data, currentMetric, currentArtist))
            .catch((error) => {
                console.log(error)
            });
        }
        else {
            fetch(`http://localhost:5000/metric/artist?metric=${currentMetric}&artist=${currentArtist}`)
            .then(response => response.json())
            .then(data => drawMetricBar(data, currentMetric, currentArtist))
            .catch((error) => {
                console.log(error)
            });
        }
        
    }
}

function drawMetricBar(data, currentMetric, currentArtist) {
    data = data['results']
    console.log(data)
    const xScale = d3.scaleLinear()
                    .domain([0, d3.max(data, function(d) {  return d[4]; })])
                    .range([0, barInnerWidth]);
    const yScale = d3.scaleBand()
                        .domain(data.map(function(d) { return d[3];}))
                        .range([0, barInnerHeight])
                        .padding(0.1);
    
    barSvg.select('g').remove();
    
    const g = barSvg.append('g')
            .attr('transform', 'translate('+barMargin.left+', '+barMargin.top+')');

    g.selectAll('g')
        .data(data)
        .join(
            enter => {
                const glyph = enter.append('g')
                            .attr('transform', (d) => `translate(${xScale(0)}, ${yScale(d[3])})`)
                            .on('mouseover', function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[0]}<br>Album: ${d[1]}<br>Song: ${d[3]}<br>Label: ${d[2]}<br>${capitalizeFirstLetter(currentMetric)}: ${d[4]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mousemove',function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[0]}<br>Album: ${d[1]}<br>Song: ${d[3]}<br>Label: ${d[2]}<br>${capitalizeFirstLetter(currentMetric)}: ${d[4]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mouseout', () => {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 0);
                                })
                                .on('click', function(d) {
                                    let query = `${d[0]} ${d[3]}`
                                    let url ='http://www.google.com/search?q=' + query;
                                    window.open(url);
                                });
                glyph.append('rect')
                    .attr('height', yScale.bandwidth())
                    .attr('width', xScale(0));

                glyph.selectAll("rect")
                    .transition()
                    .delay(function () {return Math.random()*1000 + 100;})
                    .duration(1000)
                    .attr("width", function(d) { return xScale(d[4]); });
                    
                glyph.append('text')
                    .transition()
                    .delay(1100)
                    .attr('x', (d) => xScale(d[4])/2)
                    .attr('y', yScale.bandwidth()/2)
                    .style('fill', 'black')
                    .style('alignment-baseline','middle')
                    .style('text-anchor','middle')
                    .text(d => d[3]);
            }
        )

    // add all axis labels, titles, and scales
    const yAxis = d3.axisLeft(yScale);
    var gYAxis = g.append('g').call(yAxis);
    gYAxis.selectAll('text, .tick line').remove();

    const xAxis = d3.axisBottom(xScale);
    var gXAxis = g.append('g').call(xAxis);                 
    gXAxis.attr('transform',`translate(0,${barInnerHeight})`)
    .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-10px")
        .attr("dy", "0px")
        .attr("transform", "rotate(-45)" );
    
    g.append('text')
        .attr('class','axis-label')
        .attr('text-anchor','middle')
        .attr('x', barInnerWidth/2)
        .attr('y', barInnerHeight+70)
        .text(`${capitalizeFirstLetter(currentMetric)}`)    
    
    let header = `Top songs ranked by ${capitalizeFirstLetter(currentMetric)}`;
    if (currentArtist !== '') {
        header = header + ` for ${currentArtist}`
    }
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y', -10)
        .attr('x', barInnerWidth/2)
        .text(header);
    
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y','-30px')
        .attr('x',-barInnerHeight/2)
        .attr("transform", "rotate(-90)" )
        .text(`Songs`);
}

function drawArtistBar(data, currentMetric) {
    data = data['results']
    console.log(data)
    const xScale = d3.scaleLinear()
                    .domain([0, d3.max(data, function(d) {  return d[1]; })])
                    .range([0, barInnerWidth]);
    const yScale = d3.scaleBand()
                        .domain(data.map(function(d) { return d[0];}))
                        .range([0, barInnerHeight])
                        .padding(0.1);
    
    barSvg.select('g').remove();
    
    const g = barSvg.append('g')
            .attr('transform', 'translate('+barMargin.left+', '+barMargin.top+')');

    g.selectAll('g')
        .data(data)
        .join(
            enter => {
                const glyph = enter.append('g')
                            .attr('transform', (d) => `translate(${xScale(0)}, ${yScale(d[0])})`)
                            .on('mouseover', function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[0]}<br>${currentMetric}: ${d[1]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mousemove',function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[0]}<br>${currentMetric}: ${d[1]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mouseout', () => {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 0);
                                })
                                .on('click', function(d) {
                                    let query = `${d[0]}`
                                    let url ='http://www.google.com/search?q=' + query;
                                    window.open(url);
                                });
                glyph.append('rect')
                    .attr('height', yScale.bandwidth())
                    .attr('width', xScale(0));

                glyph.selectAll("rect")
                    .transition()
                    .delay(function () {return Math.random()*1000 + 100;})
                    .duration(1000)
                    .attr("width", function(d) { return xScale(d[1]); });
                    
                glyph.append('text')
                    .transition()
                    .delay(1100)
                    .attr('x', (d) => xScale(d[1])/2)
                    .attr('y', yScale.bandwidth()/2)
                    .style('fill', 'black')
                    .style('alignment-baseline','middle')
                    .style('text-anchor','middle')
                    .text(d => d[0]);
            }
        )

    // add all axis labels, titles, and scales
    const yAxis = d3.axisLeft(yScale);
    var gYAxis = g.append('g').call(yAxis);
    gYAxis.selectAll('text, .tick line').remove();

    const xAxis = d3.axisBottom(xScale);
    var gXAxis = g.append('g').call(xAxis);                 
    gXAxis.attr('transform',`translate(0,${barInnerHeight})`)
    .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-10px")
        .attr("dy", "0px")
        .attr("transform", "rotate(-45)" );
    
    g.append('text')
        .attr('class','axis-label')
        .attr('text-anchor','middle')
        .attr('x', barInnerWidth/2)
        .attr('y', barInnerHeight+70)
        .text(`${currentMetric}`)    
    
    let header = `Top artists ranked by ${currentMetric}`;
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y', -10)
        .attr('x', barInnerWidth/2)
        .text(header);
    
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y','-30px')
        .attr('x',-barInnerHeight/2)
        .attr("transform", "rotate(-90)" )
        .text(`Artists`);
}

function drawAlbumBar(data, currentArtist) {
    data = data['results']
    console.log(data)
    const xScale = d3.scaleLinear()
                    .domain([0, d3.max(data, function(d) {  return d[1]; })])
                    .range([0, barInnerWidth]);
    const yScale = d3.scaleBand()
                        .domain(data.map(function(d) { return d[0];}))
                        .range([0, barInnerHeight])
                        .padding(0.1);
    
    barSvg.select('g').remove();
    
    const g = barSvg.append('g')
            .attr('transform', 'translate('+barMargin.left+', '+barMargin.top+')');

    g.selectAll('g')
        .data(data)
        .join(
            enter => {
                const glyph = enter.append('g')
                            .attr('transform', (d) => `translate(${xScale(0)}, ${yScale(d[0])})`)
                            .on('mouseover', function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[2]}<br>Album: ${d[0]}<br>Popularity: ${d[1]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mousemove',function(d) {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 1);
                                let toolTipText = `Artist: ${d[2]}<br>Album: ${d[0]}<br>Popularity: ${d[1]}`;
                                toolTip.html(toolTipText)
                                    .style("left", (d3.event.pageX + 10) + "px")
                                    .style("top", (d3.event.pageY - 15) + "px");
                                })
                                .on('mouseout', () => {
                                toolTip.transition()
                                    .duration(50)
                                    .style("opacity", 0);
                                })
                                .on('click', function(d) {
                                    let query = `${d[2]} ${d[0]}`
                                    let url ='http://www.google.com/search?q=' + query;
                                    window.open(url);
                                });
                glyph.append('rect')
                    .attr('height', yScale.bandwidth())
                    .attr('width', xScale(0));

                glyph.selectAll("rect")
                    .transition()
                    .delay(function () {return Math.random()*1000 + 100;})
                    .duration(1000)
                    .attr("width", function(d) { return xScale(d[1]); });
                    
                glyph.append('text')
                    .transition()
                    .delay(1100)
                    .attr('x', (d) => xScale(d[1])/2)
                    .attr('y', yScale.bandwidth()/2)
                    .style('fill', 'black')
                    .style('alignment-baseline','middle')
                    .style('text-anchor','middle')
                    .text(d => d[0]);
            }
        )

    // add all axis labels, titles, and scales
    const yAxis = d3.axisLeft(yScale);
    var gYAxis = g.append('g').call(yAxis);
    gYAxis.selectAll('text, .tick line').remove();

    const xAxis = d3.axisBottom(xScale);
    var gXAxis = g.append('g').call(xAxis);                 
    gXAxis.attr('transform',`translate(0,${barInnerHeight})`)
    .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-10px")
        .attr("dy", "0px")
        .attr("transform", "rotate(-45)" );
    
    g.append('text')
        .attr('class','axis-label')
        .attr('text-anchor','middle')
        .attr('x', barInnerWidth/2)
        .attr('y', barInnerHeight+70)
        .text(`Popularity`)
    
    let header = `Top albums ranked by Popularity`;
    if (currentArtist !== '') {
        header = header + ` for ${currentArtist}`
    }
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y', -10)
        .attr('x', barInnerWidth/2)
        .text(header);
    
    g.append('text')
        .attr('class','title')
        .attr('text-anchor','middle')
        .attr('y','-30px')
        .attr('x',-barInnerHeight/2)
        .attr("transform", "rotate(-90)" )
        .text(`Albums`);
}
