let currentScene = null

const sceneLookup = {
  "Cantwell": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Cantwell.csv",
  "Denmark": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Denmark.csv",
  "Eastville": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Eastville.csv",
  "Edgemere": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Edgemere.csv",
  "Elmira": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Elmira.csv",
  "Eudora": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Eudora.csv",
  "Greigsville": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Greigsville.csv",
  "Mosquito": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Mosquito.csv",
  "Pablo": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Pablo.csv",
  "Ribera": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Ribera.csv",
  "Sands": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Sands.csv",
  "Scioto": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Scioto.csv",
  "Sisters": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Sisters.csv",
  "Swormville": "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Swormville.csv"
}

var y = {}

const sceneChange = ({ target: btn }) => {
  const scene = sceneLookup[btn.name]
  
  if (scene) {
    console.log(btn.name)
    currentScene = scene
    console.log(currentScene)
    update()
  }
}

document.querySelectorAll('button')
  .forEach(btn => btn.addEventListener("click", sceneChange))


// set the dimensions and margins of the graph
var margin = {top: 30, right: 10, bottom: 10, left: 0},
  width = 500 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg2 = d3.select("#episodeLevel")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Parse the Data
d3.csv("https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/csv/Cantwell.csv", function(data) {

  // Extract the list of dimensions we want to keep in the plot. Here I keep all except the column called Species
  dimensions = d3.keys(data[0]).filter(function(d) { return d })

  // For each dimension, I build a linear scale. I store all in a y object
  for (i in dimensions) {
    name = dimensions[i]
    y[name] = d3.scaleLinear()
      .domain( d3.extent(data, function(d) { return +d[name]; }) )
      .range([height, 0])
  }
  
  // Build the X scale -> it find the best position for each Y axis
  x = d3.scalePoint()
    .range([0, width])
    .padding(1)
    .domain(dimensions);

  // The path function take a row of the csv as input, and return x and y coordinates of the line to draw for this raw.
  function path(d) {
      return d3.line()(dimensions.map(function(p) { return [x(p), y[p](d[p])]; }));
  }

  // Draw the lines
  svg2
    .selectAll("myPath")
    .data(data)
    .enter().append("path")
    .attr("d",  path)
    .style("fill", "none")
    .style("stroke", "#69b3a2")
    .style("opacity", 1)

  // Draw the axis:
  svg2
    .selectAll("myAxis")
    // For each dimension of the dataset I add a 'g' element:
    .data(dimensions).enter()
    .append("g")
    // I translate this element to its right position on the x axis
    .attr("transform", function(d) { return "translate(" + x(d) + ")"; })
    // And I build the axis with the call function
    .each(function(d) { d3.select(this).call(d3.axisLeft().scale(y[d])); })
    // Add axis title
    .append("text")
      .style("text-anchor", "middle")
      .attr("y", -9)
      .text(function(d) { return d; })
      .style("fill", "black")

})

function update(){
  svg2.selectAll("path").remove()
  svg2.selectAll("g").remove()
  

  d3.csv(currentScene, function(data) {

  // Extract the list of dimensions we want to keep in the plot. Here I keep all except the column called Species
  dimensions = d3.keys(data[0]).filter(function(d) { return d })

  // For each dimension, I build a linear scale. I store all in a y object
  for (var member in y) delete y[member];
  for (i in dimensions) {
    name = dimensions[i]
    y[name] = d3.scaleLinear()
      .domain( d3.extent(data, function(d) { return +d[name]; }) )
      .range([height, 0])
  }

  // Build the X scale -> it find the best position for each Y axis
  x = d3.scalePoint()
    .range([0, width])
    .padding(1)
    .domain(dimensions);

  // The path function take a row of the csv as input, and return x and y coordinates of the line to draw for this raw.
  function path(d) {
      return d3.line()(dimensions.map(function(p) { return [x(p), y[p](d[p])]; }));
  }

  // Draw the lines
  svg2
    .selectAll("myPath")
    .data(data)
    .enter().append("path")
    .attr("d",  path)
    .style("fill", "none")
    .style("stroke", "#69b3a2")
    .style("opacity", 0.5)

  // Draw the axis:
  svg2
    .selectAll("myAxis")
    // For each dimension of the dataset I add a 'g' element:
    .data(dimensions).enter()
    .append("g")
    // I translate this element to its right position on the x axis
    .attr("transform", function(d) { return "translate(" + x(d) + ")"; })
    // And I build the axis with the call function
    .each(function(d) { d3.select(this).call(d3.axisLeft().scale(y[d])); })
    // Add axis title
    .append("text")
      .style("text-anchor", "middle")
      .attr("y", -9)
      .text(function(d) { return d; })
      .style("fill", "black")

})
}