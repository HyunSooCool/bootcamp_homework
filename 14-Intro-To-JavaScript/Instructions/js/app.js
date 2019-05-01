const ufo = data;

let tbody = d3.select("tbody");

ufo.forEach((ufo_data)=>{
    const row = tbody.append("tr");
    for (key in ufo_data){
        const cell = tbody.append("td");
        cell.text(ufo_data[key]);
    }
    
});


const submit = d3.select("#filter-btn");

submit.on("click", function(){
    
    d3.event.preventDefault();
    

    console.log(ufo);
    const inputElement = d3.select("#datetime");

    const inputValue = inputElement.property("value");

    console.log(inputValue);

    const filteredData = ufo.filter(data => data.datetime === inputValue);

    console.log(filteredData);

    var Table = document.getElementById("ufo-contents");
    Table.innerHTML = "";

    let tbody = d3.select("tbody");
  
    filteredData.forEach((filter_data)=>{
       
        const row = tbody.append("tr");
        for (key in filter_data){
            const cell = tbody.append("td");
            cell.text(filter_data[key]);
       }
    });


 
    });