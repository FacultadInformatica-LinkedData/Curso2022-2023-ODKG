jQuery.fn.shake = function(interval,distance,times){
  interval = typeof interval == "undefined" ? 100 : interval;
  distance = typeof distance == "undefined" ? 10 : distance;
  times = typeof times == "undefined" ? 3 : times;
  var jTarget = $(this);
  jTarget.css('position','relative');
  for(var iter=0;iter<(times+1);iter++){
     jTarget.animate({ left: ((iter%2==0 ? distance : distance*-1))}, interval);
  }
  return jTarget.animate({ left: 0},interval);
}

$("#schoolNameSearchBox").val("")

function search(schoolName = ""){
    let searchResults = getSpark(schoolName);

    console.log(searchResults);

   	generateCards(searchResults);

    getMap();
    $("#searchResults").show();
}

function generateCards(results){for(let cardResult of results){getCard(cardResult);}}

function getcard(school){
	console.log('d')
	$("#searchResults").html('hola')
}

$( document ).ready(function() {
    var savedSchools = [];
    $('#SchoolSearchForm').on('submit', (event) => {
        event.preventDefault();
        // handle the form data
        let schoolName = $('#schoolNameSearchBox').val(); //event.currentTarget[0].value;
        search(schoolName)

    });
    $('.schoolInfo').on('click', flipItem);
});

function flipItem() {
    $(this).parent().parent().shake(100,10,3);
    $(this).parent().parent().find('.front').toggleClass("invisibleFront");
    $(this).parent().parent().find('.back').toggleClass("visibleBack");
}


function getMap(){
    // Where you want to render the map.
    var element = $('.schoolMap');
    element = element[0]
    // Height has to be set. You can do this in CSS too.
    element.style = 'height:300px;';
    // Create Leaflet map on map element.
    var map = L.map(element);
    // Add OSM tile layer to the Leaflet map.
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    // Target's GPS coordinates.
    var target = L.latLng('47.50737', '19.04611');
    // Set map's center to target with zoom 14.
    map.setView(target, 14);
    // Place a marker on the same location.
    L.marker(target).addTo(map);
}

function getSpark(nameSearch){

	var p;

    $.ajax({
    //url: "http://localhost:8080/sparql?query=PREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0A%0ASELECT%20%3Fs%20%3Fname%20WHERE%20%7B%0A%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%3Fs%20ont%3Aname%20%3Fname%0A%7D%20%0ALIMIT%2010",


    url: "http://localhost:8080/sparql?query=PREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0A%0ASELECT%20%3Fs%20%3Fn%20WHERE%20%7B%0A%20%20%3Fs%20a%20ont%3ASchool%20.%0A%20%20%3Fs%20ont%3Aname%20%3Fn.%0A%20%20%0A%20%20filter%20contains%28%3Fn%2C%22"+nameSearch+"%22%29%0A%0A%7D%20%0A",
    headers: {
              'accept': 'application/json',
              'Access-Control-Allow-Origin':'*'
            },
    type: "GET", /* or type:"GET" or type:"PUT" */
    dataType: "json",
    data: {
    },
    ContentType : false,
    success: function (result) {
    	//console.log(result);
    	p = preprocess(result)
    	console.log(p)

    	
        
    },
    error: function () {
        console.log("error");
    }
});

    return p
}

function preprocess(json){
	var columnName = json['head']['vars']

	var values = json['results']['bindings']


	let results = []


	for (var r of values){

		var dictionary = {}

		for (var c of columnName){
			dictionary[c] = r[c].value
		}
		results.push(dictionary)
	}


	return results
}


