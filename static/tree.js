//d3 template to generate a radial tree diagram
//see original at http://mbostock.github.com/d3/ex/tree.html

var generate_tree = function(){
	console.log("entering generate tree")
	var radius = 960 / 2;
	
	var tree = d3.layout.tree()
	    .size([360, radius - 120])
	    .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });
	
	var diagonal = d3.svg.diagonal.radial()
	    .projection(function(d) { return [d.y, d.x / 180 * Math.PI]; });
	
	//clear chart before re-drawing for new submits
	document.getElementById("chart").innerHTML = "";

	var vis = d3.select("#chart").append("svg")
	    .attr("width", radius * 2 + 100)
	    .attr("height", radius * 2 + 100)
	  .append("g")
	    .attr("transform", "translate(" + (radius + 50) + "," + radius + ")");
	
	//grab input name
	var name = document.getElementById('name').value

	d3.json('/' + name, function(json) {
	  var nodes = tree.nodes(json);
	
	  var link = vis.selectAll("path.link")
	      .data(tree.links(nodes))
	    .enter().append("path")
	      .attr("class", "link")
	      .attr("d", diagonal)
	      .attr("stroke", "#eee")
	      .attr("fill", "none");
	
	  var node = vis.selectAll("g.node")
	      .data(nodes)
	    .enter().append("g")
	      .attr("class", "node")
	      .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; });
	
	  node.append("circle")
	      .attr("r", 4.5);
	
	  node.append("text")
	      .attr("dy", ".31em")
	      .attr("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
	      .attr("transform", function(d) { return d.x < 180 ? "translate(8)" : "rotate(180)translate(-8)"; })
	      .text(function(d) { return d.name; });
	});
};

// $('#name').keypress(generate_tree());


// name_input = document.getElementById('name');
// name_input.addEventListener('keypress', function(e){
//   if (e.keyCode == 13) {
//     console.log('Enter pressed')
//     generate_tree();
//   }
// });