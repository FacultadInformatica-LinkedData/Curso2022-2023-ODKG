
async function request() {
    var district = document.getElementById("format");
    var district_value = district.options[district.selectedIndex].value;
    var element = document.getElementById("container");
    var mode = "";

    element.innerHTML="<p>Searching....</p>"

    if(document.getElementById("fountains").checked || document.getElementById("restrooms").checked){
        if (document.getElementById("fountains").checked){
            mode = "fountains";
            if(document.getElementById("restrooms").checked){
                mode = "all";
                }
        }else{
            mode = "restrooms";
        }
        let response = await fetch("http://localhost:8000/"+mode+"/"+district_value);
        let data = await response.text();
        element.innerHTML = data;

        // Getting the table
        var tble = element.childNodes[0]; 
  
        // Getting the rows in table.
        var row = tble.rows;  
  
        // Removing the column at index(1).  
        var i = 0; 
        for (var j = 0; j < row.length; j++) {
  
            // Deleting the ith cell of each row.
            row[j].deleteCell(i);
        }
    }else{
        element.innerHTML = "<p>Please select at least one of the available elements</p>"
    }
}

async function linked_request() {
    
    var neighborhood = document.getElementById("linked_search");
    var element = document.getElementById("linked_container");
    var neighborhood_value = neighborhood.value;

    if(neighborhood_value===""){
        element.innerHTML="<p>Type the name of the neighborhood in the search box</p>"
    }else{
        element.innerHTML="<p>Searching....</p>"

        if(document.getElementById("linked_fountains").checked || document.getElementById("linked_restrooms").checked){
            if (document.getElementById("linked_fountains").checked){
                mode = "fountains";
                if(document.getElementById("linked_restrooms").checked){
                    mode = "all";
                    }
            }else{
                mode = "restrooms";
            }
            let response = await fetch("http://localhost:8000/nh/"+mode+"/"+neighborhood_value);
            let data = await response.text();
            element.innerHTML = data;

            // Getting the table
            var tble = element.childNodes[0]; 
            
            // Getting the rows in table.
            var row = tble.rows;

            if(row.length==1){
                element.innerHTML = "<p>Neighborhood not found</p>";
            }else{
                // Removing the column at index(1).  
                var i = 0; 
                for (var j = 0; j < row.length; j++) {
        
                    // Deleting the ith cell of each row.
                    row[j].deleteCell(i);
                }
            }
    
        }else{
            element.innerHTML = "<p>Please select at least one of the available elements</p>"
        }
    }
}
