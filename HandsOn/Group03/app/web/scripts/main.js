metroLines = {
    "Line 1":"",
    "Line 2":"",
    "Line 3":"",
    "Line 4":"",
    "Line 5":"",
    "Line 6":"",
    "Line 7":"",
    "Line 8":"",
    "Line 9":"",
    "Line 10":"",
    "Line 11":"",
    "Line 12":""
}

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
    $("#searchResults").html("")
    metroLine = $("#metroLineSelector").val();
    let searchResults = NaN;
    if(metroLine){
        searchResults = getSparkMetro(schoolName, metroLine);
    }
    else{
        searchResults = getSpark(schoolName);
    }
    //console.log(searchResults);
   	generateCards(searchResults);
    $("#searchResults").show();
}


function getCard(school){
	console.log(school)

	let current = $("#searchResults").html()

	let identifier = school['identifier']
	let schoolName = school['name']
    let neighborhoodName = school['neighborhoodName']
    let streetAddress = school['streetAddress']

    let schedule = school['schedule']
    let telephone = school['telephone']
    let laborday = school['laborday']
    let typeAccesibility = school['typeAccesibility']

	let newHTML = `<div class="schoolItem", id="${identifier}">
          <div class="front cardFace">
            <div class="schoolMap"></div>
            <div class="schoolInfo">
                <br>
                <p class="schoolName">${schoolName}</p>
                <br>
                <p class="schoolLocation">${neighborhoodName}</p>
                <hr>
                <p class="schoolAddress">${streetAddress}</p>
                <br>
            </div>
            <a class="starButton"><i class="fa fa-star"></i></a>
          </div>
          <div class="back cardFace">
            <div class="backMapInfo">
              <p>texto de ejemplo</p>
            </div>
            <div class="schoolInfo">
              <br>
                <p class="schoolName">${schoolName}</p>
                <br>
              <p class="typeAccesibility">${typeAccesibility}</p>
              <hr>
              <p class="schedule">${schedule}</p>
              <p class="laborDay">${laborDay}</p>
              <p class="telephone">${telephone}</p>
            </div>
            <a class="starButton"><i class="fa fa-star"></i></a>
          </div>
        </div>`

	$("#searchResults").html(current + newHTML)

	getMap();
}

function generateCards(results){for(let cardResult of results){getCard(cardResult);}}

$( document ).ready(function() {
    var savedSchools = [];
    $('#SchoolSearchForm').on('submit', (event) => {
        event.preventDefault();
        // handle the form data
        let schoolName = $('#schoolNameSearchBox').val(); //event.currentTarget[0].value;
        search(schoolName)

    });
    $('.schoolInfo').on('click', flipItem);
    $('.starButton').on('click', saveSchool);
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
        async: false,

        url: "http://localhost:8080/sparql?query=PREFIX%20sc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0ASELECT%20%2A%20%20WHERE%7B%0A%0A%20%20%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%20%20%3Fs%20schema%3Aidentifier%20%3Fidentifier.%0A%20%20%20%20%3Fs%20schema%3Aname%20%3Fname.%0A%20%20%20%20%3Fs%20schema%3Alatitude%20%3Flatitude.%0A%20%20%20%20%3Fs%20schema%3Alongitude%20%3Flongitude.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20schema%3Atelephone%20%3Ftelephone%7D.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3AlaborDay%20%3FlaborDay%7D.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3Aschedule%20%3Fschedule%7D.%0A%0A%20%20%20%20%3Fs%20schema%3Aaddress%20%3Faddress.%0A%20%20%20%20%3Faddress%20schema%3AstreetAddress%20%3FstreetAddress.%0A%0A%20%20%20%20%3Faddress%20ont%3AhasNeighborhood%20%3Fneighborhood.%0A%20%20%20%20%3Fneighborhood%20ont%3Aneighborhood%20%3FneighborhoodName%0A%20%20%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3AhasAccessibility%20%3Faccessibility%7D.%0A%09OPTIONAL%20%7B%20%3Faccessibility%20ont%3AtypeAccesibility%20%3FtypeAccesibility%7D.%0A%0A%20%20%20%20%20%20%20filter%20contains%28%3Fname%20%2C%22" + nameSearch + "%22%29%0A%0A%7D",
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
            console.log(result);
            p = preprocess(result)
            
            
        },
        error: function () {
            console.log("error");
        }
    });
    return p
}

function getSparkMetro(schoolName, metroLine){}

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


function saveSchool(){
    console.log(this);
}