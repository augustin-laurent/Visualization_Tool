var margin = {top: 30, right: 10, bottom: 10, left: 0},
  width = 500 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

var svg3 = d3.select("map")
    .append("svg")
    .append("g")

var map_image = svg3.append("image")
    .attr("xlink:href", "map/top_down_map0.png")
    