var img = document.createElement("img")
img.src = "https://raw.githubusercontent.com/augustin-laurent/Visualization_Tool/master/map/top_down_map0.png"
var src = document.getElementById("map")
src.appendChild(img)

let data = [{
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1285,
    "yVal": 424
}, {
    "xVal": 1283,
    "yVal": 459
}, {
    "xVal": 1283,
    "yVal": 459
}, {
    "xVal": 1283,
    "yVal": 459
}, {
    "xVal": 1272,
    "yVal": 493
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1258,
    "yVal": 525
}, {
    "xVal": 1223,
    "yVal": 529
}, {
    "xVal": 1188,
    "yVal": 533
}, {
    "xVal": 1153,
    "yVal": 537
}, {
    "xVal": 1118,
    "yVal": 541
}, {
    "xVal": 1083,
    "yVal": 545
}, {
    "xVal": 1048,
    "yVal": 549
}, {
    "xVal": 1013,
    "yVal": 553
}, {
    "xVal": 978,
    "yVal": 557
}, {
    "xVal": 943,
    "yVal": 561
}, {
    "xVal": 907,
    "yVal": 565
}, {
    "xVal": 872,
    "yVal": 568
}, {
    "xVal": 837,
    "yVal": 572
}, {
    "xVal": 802,
    "yVal": 576
}, {
    "xVal": 767,
    "yVal": 580
}, {
    "xVal": 732,
    "yVal": 584
}, {
    "xVal": 697,
    "yVal": 588
}, {
    "xVal": 662,
    "yVal": 592
}, {
    "xVal": 627,
    "yVal": 596
}, {
    "xVal": 627,
    "yVal": 596
}, {
    "xVal": 592,
    "yVal": 593
}, {
    "xVal": 592,
    "yVal": 593
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 557,
    "yVal": 597
}, {
    "xVal": 531,
    "yVal": 573
}, {
    "xVal": 531,
    "yVal": 573
}, {
    "xVal": 511,
    "yVal": 545
}, {
    "xVal": 490,
    "yVal": 516
}, {
    "xVal": 469,
    "yVal": 488
}, {
    "xVal": 469,
    "yVal": 488
}, {
    "xVal": 453,
    "yVal": 456
}, {
    "xVal": 438,
    "yVal": 425
}, {
    "xVal": 438,
    "yVal": 425
}, {
    "xVal": 421,
    "yVal": 392
}, {
    "xVal": 411,
    "yVal": 358
}, {
    "xVal": 411,
    "yVal": 358
}, {
    "xVal": 395,
    "yVal": 327
}, {
    "xVal": 379,
    "yVal": 295
}, {
    "xVal": 364,
    "yVal": 264
}, {
    "xVal": 348,
    "yVal": 232
}, {
    "xVal": 348,
    "yVal": 232
}, {
    "xVal": 338,
    "yVal": 198
}, {
    "xVal": 338,
    "yVal": 198
}, {
    "xVal": 338,
    "yVal": 198
}, {
    "xVal": 338,
    "yVal": 198
}, {
    "xVal": 313,
    "yVal": 174
}, {
    "xVal": 313,
    "yVal": 174
}, {
    "xVal": 313,
    "yVal": 174
}, {
    "xVal": 313,
    "yVal": 174
}, {
    "xVal": 278,
    "yVal": 162
}, {
    "xVal": 244,
    "yVal": 154
}, {
    "xVal": 210,
    "yVal": 145
}, {
    "xVal": 175,
    "yVal": 137
}, {
    "xVal": 141,
    "yVal": 129
}, {
    "xVal": 107,
    "yVal": 120
}]

var x = d3.scaleLinear().range([0, 2154])
var y = d3.scaleLinear().range([1024, 0])

var xAxis = d3.axisBottom()
    .scale(x)
    .ticks(7);

var yAxis = d3.axisLeft()
    .scale(y)
    .ticks(5);

var valueline = d3.line()
    /*
    .defined(function(d) {
       return false;
    })
    */
    
    .defined(function(d) {
        return d.yVal != -1;
    })
    
    .x(function (d) {
        return x(d.xVal);
    })
    .y(function (d) {
        return y(d.yVal);
    })
   .curve(d3.curveMonotoneX)

var svg3 = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g");

    
// Scale the range of the data
x.domain(d3.extent(data,
    function (d) {
        return d.xVal;
    }));
y.domain([
    0, d3.max(data,
        function (d) {
            return d.yVal;
        })
]);

svg3.append("path") // Add the valueline path.
    .attr("d", valueline(data));

svg3.append("g") // Add the X Axis
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

svg3.append("g") // Add the Y Axis
    .attr("class", "y axis")
    .call(yAxis);

// add "dots" (circles) for each "valid" data point
// using same validity function as used above for line
svg3.selectAll('circle')
    .data(data.filter(function(d) {
        return d.yVal != -1;
    }))
    .enter().append('circle')
      .attr('r', 5)
      .attr('cx', function (d) {
        return x(d.xVal);
      })
      .attr('cy', function (d) {
        return y(d.yVal);
      })

      
