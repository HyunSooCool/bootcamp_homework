// @TODO: YOUR CODE HERE!
(async function(){
    const
        svgWidth = 960,
        svgHeight = 500;
    
    const margin ={
        top : 20,
        right : 40,
        bottom : 60,
        left : 100
    };

    
    const width = svgWidth - margin.left - margin.right;
    const height = svgHeight - margin.top - margin.bottom;

    const svg = d3.select(".chart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

    const chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

    //import data
    const healthData = await d3.csv("../assets/data/data.csv");

    //step 1: Parse Data/Cast as numbers
    healthData.forEach(function(data){
        data.poverty= +data.poverty;
        data.healthcare= +data.healthcare;
    });

    //step 2 : create scale functions
    const xLinearScale = d3.scaleLinear()

        .domain([8,d3.max(healthData, d => d.poverty)])
        .range([0, width]);
    
    const yLinearScale = d3.scaleLinear()
        .domain([4,d3.max(healthData, d => d.healthcare)])
        .range([height, 0]);

    //step 3 : create axis functions
    const bottomAxis = d3.axisBottom(xLinearScale);
    const leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

    chartGroup.append("g")
    .call(leftAxis);    

    // Step 5: Create Circles


    const circlesGroup = chartGroup.selectAll("circle")
    .data(healthData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "10")
    .attr("fill", "blue")
    .attr("opacity", ".5");

    
    const text = chartGroup.selectAll("text")
                .data(healthData)
                .enter()
                .append("text")
                .attr("x", d => xLinearScale(d.poverty))
                .attr("y", d => yLinearScale(d.healthcare))
                .text( function (d) { return d.id; });

    const textLabels = text
                    // .attr("x", function(d){return xLinearScale(d.poverty);})
                    // .attr("y", function(d){return yLinearScale(d.healthcare);})
                    // .attr("x", d => xLinearScale(d.poverty))
                    // .attr("y", d => yLinearScale(d.healthcare))
                    // .text( function (d) { return d.id; })
              
                //  .attr("font-family", "sans-serif")
                //  .attr("font-size", "10px")
                //  .attr("fill", "red");

    

    // chartGroup.selectAll("text")
    // .data(healthData)
    // .enter()
    // .append("text")
    // // .attr("dx", function(d){return dx})
    // // .attr("dy", function(d){return dy})
    // .text(function(d){return(d.abbr)})
    // .attr("font-size", "15px")
    // .attr("fill", "white");


    
    //Create axes labels
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare(%)");

    chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
        .attr("class", "axisText")
        .text("In Poverty (%)");

})()