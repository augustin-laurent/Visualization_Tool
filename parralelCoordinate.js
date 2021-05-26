const btn = document.querySelectorAll('button');

for (let i = 0; i < btn.length; i++) {
  btn[i].addEventListener("click", sceneChange());
}

var pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Cantwell.csv"

function sceneChange(){
  if(btn.name == "Cantwell"){
    console.log("Cantwell")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Cantwell.csv"
    return(pickedScene);
  }
  else if(btn.name == "Denmark"){
    console.log("Denmark")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Denmark.csv"
    return(pickedScene);
  }
  else if(btn.name == "Eastville"){
    console.log("Eastville")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Eastville.csv"
    return(pickedScene);
  }
  else if(btn.name == "Edgemere"){
    console.log("Edgemere")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Edgemere.csv"
    return(pickedScene);
  }
  else if(btn.name == "Elmira"){
    console.log("Elmira")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Elmira.csv"
    return(pickedScene);
  }
  else if(btn.name == "Eudora"){
    console.log("Eudora")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Eudora.csv"
    return(pickedScene);
  }
  else if(btn.name == "Greigsville"){
    console.log("Greigsville")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Greigsville.csv"
    return(pickedScene);
  }
  else if(btn.name == "Mosquito"){
    console.log("Mosquito")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Mosquito.csv"
    return(pickedScene);
  }
  else if(btn.name == "Pablo"){
    console.log("Pablo")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Pablo.csv"
    return(pickedScene);
  }
  else if(btn.name == "Ribera"){
    console.log("Ribera")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Ribera.csv"
    return(pickedScene);
  }
  else if(btn.name == "Sands"){
    console.log("Sands")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Sands.csv"
    return(pickedScene);
  }
  else if(btn.name == "Scioto"){
    console.log("Scioto")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Scioto.csv"
    return(pickedScene);
  }
  else if(btn.name == "Sisters"){
    console.log("Sisters")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Sisters.csv"
    return(pickedScene);
  }
  else if(btn.name == "Swormville"){
    console.log("Swormville")
    pickedScene = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/Swormville.csv"
    return(pickedScene);
  }
  
}

// set the dimensions and margins of the graph
var margin = {top: 30, right: 50, bottom: 10, left: 50},
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
d3.csv(pickedScene, function(data) {

  // Color scale: give me a specie name, I return a color
  var color = d3.scaleLinear()
    .range(["#ff4040","#ff423d","#ff453a","#ff4838","#fe4b35","#fe4e33","#fe5130","#fd542e","#fd572b","#fc5a29","#fb5d27","#fa6025","#f96322","#f96620","#f7691e","#f66c1c","#f56f1a","#f47218","#f37517","#f17815","#f07c13","#ee7f11","#ed8210","#eb850e","#e9880d","#e88b0c","#e68e0a","#e49209","#e29508","#e09807","#de9b06","#dc9e05","#d9a104","#d7a403","#d5a703","#d2aa02","#d0ad02","#ceb001","#cbb301","#c9b600","#c6b800","#c3bb00","#c1be00","#bec100","#bbc300","#b8c600","#b6c900","#b3cb01","#b0ce01","#add002","#aad202","#a7d503","#a4d703","#a1d904","#9edc05","#9bde06","#98e007","#95e208","#92e409","#8ee60a","#8be80c","#88e90d","#85eb0e","#82ed10","#7fee11","#7cf013","#78f115","#75f317","#72f418","#6ff51a","#6cf61c","#69f71e","#66f920","#63f922","#60fa25","#5dfb27","#5afc29","#57fd2b","#54fd2e","#51fe30","#4efe33","#4bfe35","#48ff38","#45ff3a","#42ff3d","#40ff40","#3dff42","#3aff45","#38ff48","#35fe4b","#33fe4e","#30fe51","#2efd54","#2bfd57","#29fc5a","#27fb5d","#25fa60","#22f963","#20f966","#1ef769","#1cf66c","#1af56f","#18f472","#17f375","#15f178","#13f07c","#11ee7f","#10ed82","#0eeb85","#0de988","#0ce88b","#0ae68e","#09e492","#08e295","#07e098","#06de9b","#05dc9e","#04d9a1","#03d7a4","#03d5a7","#02d2aa","#02d0ad","#01ceb0","#01cbb3","#00c9b6","#00c6b8","#00c3bb","#00c1be","#00bec1","#00bbc3","#00b8c6","#00b6c9","#01b3cb","#01b0ce","#02add0","#02aad2","#03a7d5","#03a4d7","#04a1d9","#059edc","#069bde","#0798e0","#0895e2","#0992e4","#0a8ee6","#0c8be8","#0d88e9","#0e85eb","#1082ed","#117fee","#137cf0","#1578f1","#1775f3","#1872f4","#1a6ff5","#1c6cf6","#1e69f7","#2066f9","#2263f9","#2560fa","#275dfb","#295afc","#2b57fd","#2e54fd","#3051fe","#334efe","#354bfe","#3848ff","#3a45ff","#3d42ff","#4040ff","#423dff","#453aff","#4838ff","#4b35fe","#4e33fe","#5130fe","#542efd","#572bfd","#5a29fc","#5d27fb","#6025fa","#6322f9","#6620f9","#691ef7","#6c1cf6","#6f1af5","#7218f4","#7517f3","#7815f1","#7c13f0","#7f11ee","#8210ed","#850eeb","#880de9","#8b0ce8","#8e0ae6","#9209e4","#9508e2","#9807e0","#9b06de","#9e05dc","#a104d9","#a403d7","#a703d5","#aa02d2","#ad02d0","#b001ce","#b301cb","#b600c9","#b800c6","#bb00c3","#be00c1","#c100be","#c300bb","#c600b8","#c900b6","#cb01b3","#ce01b0","#d002ad","#d202aa","#d503a7","#d703a4","#d904a1","#dc059e","#de069b","#e00798","#e20895","#e40992","#e60a8e","#e80c8b","#e90d88","#eb0e85","#ed1082","#ee117f","#f0137c","#f11578","#f31775","#f41872","#f51a6f","#f61c6c","#f71e69","#f92066","#f92263","#fa2560","#fb275d","#fc295a","#fd2b57","#fd2e54","#fe3051","#fe334e","#fe354b","#ff3848","#ff3a45","#ff3d42","#ff4040"])

  // Here I set the list of dimension manually to control the order of axis:
  dimensions = ["Start_to_End", "Length_ShortestPath", "Length_ORBSlamPath", "Stop_to_End", "Number_of_collisions"]

  // For each dimension, I build a linear scale. I store all in a y object
  var y = {}
  for (i in dimensions) {
    name = dimensions[i]
    y[name] = d3.scaleLinear()
      .domain( [0,500] ) // --> Same axis range for each group
      // --> different axis range for each group --> .domain( [d3.extent(data, function(d) { return +d[name]; })] )
      .range([height, 0])
  }

  // Build the X scale -> it find the best position for each Y axis
  x = d3.scalePoint()
    .range([0, width])
    .domain(dimensions);

  // Highlight the specie that is hovered
  var highlight = function(d){

    selected_specie = d.Species

    // first every group turns grey
    d3.selectAll(".line")
      .transition().duration(200)
      .style("stroke", "lightgrey")
      .style("opacity", "0.2")
    // Second the hovered specie takes its color
    d3.selectAll("." + selected_specie)
      .transition().duration(200)
      .style("stroke", color(selected_specie))
      .style("opacity", "1")
  }

  // Unhighlight
  var doNotHighlight = function(d){
    d3.selectAll(".line")
      .transition().duration(200).delay(1000)
      .style("stroke", function(d){ return( color(d.Species))} )
      .style("opacity", "1")
  }

  // The path function take a row of the csv as input, and return x and y coordinates of the line to draw for this raw.
  function path(d) {
      return d3.line()(dimensions.map(function(p) { return [x(p), y[p](d[p])]; }));
  }

  // Draw the lines
  svg2
    .selectAll("myPath")
    .data(data)
    .enter()
    .append("path")
      .attr("class", function (d) { return "line " + d.Species } ) // 2 class for each line: 'line' and the group name
      .attr("d",  path)
      .style("fill", "none" )
      .style("stroke", function(d){ return( color(d.Species))} )
      .style("opacity", 0.5)
      .on("mouseover", highlight)
      .on("mouseleave", doNotHighlight )

  // Draw the axis:
  svg2.selectAll("myAxis")
    // For each dimension of the dataset I add a 'g' element:
    .data(dimensions).enter()
    .append("g")
    .attr("class", "axis")
    // I translate this element to its right position on the x axis
    .attr("transform", function(d) { return "translate(" + x(d) + ")"; })
    // And I build the axis with the call function
    .each(function(d) { d3.select(this).call(d3.axisLeft().ticks(5).scale(y[d])); })
    // Add axis title
    .append("text")
      .style("text-anchor", "middle")
      .attr("y", -9)
      .text(function(d) { return d; })
      .style("fill", "black")

})