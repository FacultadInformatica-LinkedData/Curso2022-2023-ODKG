metroLines = {
    "Line1":"Q1826675",
    "Line2":"Q1826679",
    "Line3":"Q1826673",
    "Line4":"Q1826677",
    "Line5":"Q1568028",
    "Line6":"Q514227",
    "Line7":"Q1826683",
    "Line8":"Q1475527",
    "Line9":"Q1759707",
    "Line10":"Q1760090",
    "Line11":"Q608251",
    "Line12":"Q1558864"
}

districts_options = ['Hortaleza', 'Villa de Vallecas', 'Puente de Vallecas', 'San Blas',
       'Latina', 'Vicalvaro', 'Fuencarral-El Pardo', 'Salamanca',
       'Villaverde', 'Carabanchel', 'Centro', 'Moncloa-Aravaca',
       'Chamartin', 'Barajas', 'Ciudad Lineal', 'Chamberi', 'Usera',
       'Retiro', 'Moratalaz', 'Tetuan', 'Arganzuela']

accesibilityDict = {
    "0":"Not Accessible",
    "1":"Accessible",
    "2":"Partially accessible"
}

function flipItem() {
    $(this).parent().parent().shake(100,10,3);
    $(this).parent().parent().find('.front').toggleClass("invisibleFront");
    $(this).parent().parent().find('.back').toggleClass("visibleBack");
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
    let metro_filter= ""
    if(metroLine){
        let w_station = getWiki(metroLines[metroLine])
        let ws = []
        for (var w of w_station){
            ws.push(w.replace("http://www.", "https://").replace(":", "%3A").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F").replace("/", "%2F"))
        }
        //searchResults = getSparkMetro(schoolName, "%22" + ws.join("%22%2C%20%22") + "%22");
        //console.log(searchResults)

        metro_filter = "%22" + ws.join("%22%2C%20%22") + "%22"

        //searchResults = getSpark(schoolName, "%22" + ws.join("%22%2C%20%22") + "%22")
        //console.log(searchResults)
    }

    console.log($("#districtSelector").val())
    district_filter = $("#districtSelector").val().replace(" ", "%20").replace(" ", "%20").replace(" ", "%20");
    access_filter = $("#typeAccessibilitySelector").val();

    console.log(metro_filter,district_filter,access_filter)
   
    searchResults = getSpark(schoolName, metro_filter, district_filter, access_filter);
    
    //console.log(searchResults);
   	generateCards(searchResults);

    $('.schoolInfo').on('click', flipItem);
    $('.starButton').on('click', saveSchool);

    $("#searchResults").show();
}


function getCard(school){
	console.log(school)

	let current = $("#searchResults").html()

	let identifier = school['identifier']
	let schoolName = school['name']
    let districtName = school['districtName']
    let neighborhoodName = school['neighborhoodName']
    let streetAddress = school['streetAddress']

    let schedule = school['schedule']
    let telephone = school['telephone']
    let laborDay = school['laborDay']
    let typeAccessibility = school['typeAccessibility']
    
    var utm = "+proj=utm +zone=30";
    var wgs84 = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs";
    coords = proj4(utm,wgs84,[school['latitude'], school['longitude']]);
    //console.log(coords)

    /*<iframe class="schoolMap" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
            src="https://www.openstreetmap.org/export/embed.html?bbox=-3.8222%2C40.4882%2C-3.5029%2C40.3539&amp;layer=mapnik&amp;marker=${coords[0]}2C-${coords[1]}" 
            style="border: 1px solid black">
            </iframe>
*/
    let zoom = 14.5;
	let newHTML = `<div class="schoolItem", id="${identifier}">
          <div class="front cardFace">
          <iframe class="schoolMap" width="500" height="300" src="https://api.maptiler.com/maps/basic-v2/?key=T0cx4SaMZWSM2Gq2mAgG#${zoom}/${coords[1]}/${coords[0]}/"></iframe>
            <div class="schoolInfo">
                <br>
                <p class="schoolName">${schoolName}</p>
                <br>
                <p class="schoolLocation">District: ${districtName}</p>
                <p class="schoolLocation">Neighborhood: ${neighborhoodName}</p>
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
              <p class="typeAccesibility">Tipo de accesibilidad: ${accesibilityDict[typeAccessibility]}</p>
              <hr>
              <p class="schedule">${schedule}</p>
              <p class="laborDay">${laborDay}</p>
              <p class="telephone">${telephone}</p>
            </div>
            <a class="starButton"><i class="fa fa-star"></i></a>
          </div>
        </div>`

	$("#searchResults").html(current + newHTML)

	//getMap(`schoolMap${identifier}`, coords[1], coords[0]);
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




function getMap(id, lon, lat){
    // Where you want to render the map.
    var element = $(`#${id}`);
    element = element[0]
    // Height has to be set. You can do this in CSS too.
    element.style = 'height:300px;';
    // Create Leaflet map on map element.
    var map = L.map(element, {
    crs: L.CRS.EPSG32630
    });
    // Add OSM tile layer to the Leaflet map.
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    // Target's GPS coordinates.

}

function getSparkMetro(nameSearch, lines){

    var p;
    $.ajax({
        //url: "http://localhost:8080/sparql?query=PREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0A%0ASELECT%20%3Fs%20%3Fname%20WHERE%20%7B%0A%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%3Fs%20ont%3Aname%20%3Fname%0A%7D%20%0ALIMIT%2010",
        async: false,


        url: `http://localhost:8080/sparql?query=PREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20sc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0ASELECT%20%3Fs%20%3Fname%20%3Fwiki%20%20WHERE%7B%0A%0A%20%20%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%20%20%3Fs%20schema%3Aidentifier%20%3Fidentifier.%0A%20%20%20%20%3Fs%20schema%3Aname%20%3Fname.%0A%0A%20%20%20%20%3Fs%20ont%3AhasAccessibility%20%3Faccessibility.%0A%20%20%20%20%3Faccessibility%20ont%3AhasMetro%20%3Fmetro.%0A%20%20%3Fmetro%20owl%3AsameAs%20%3Fwiki%0A%20%20%0A%09%20%20%20FILTER%28%3Fwiki%20IN%20%28${lines}%29%29.%0A%20%20%20FILTER%20%28Contains%28%3Fname%2C%20%22${nameSearch}%22%29%29%0A%0A%0A%0A%7D`,
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
            p = preprocessHelios(result)
            
            
        },
        error: function () {
            console.log("error");
        }
    });
    return p
}

function getSpark(nameSearch, line_filter = "", district_filter="", access_filter=""){
	var p;

    let url = "http://localhost:8080/sparql?query=PREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20sc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0ASELECT%20%2A%20%20WHERE%7B%0A%0A%20%20%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%20%20%3Fs%20schema%3Aidentifier%20%3Fidentifier.%0A%20%20%20%20%3Fs%20schema%3Aname%20%3Fname.%0A%20%20%20%20%3Fs%20schema%3Alatitude%20%3Flatitude.%0A%20%20%20%20%3Fs%20schema%3Alongitude%20%3Flongitude.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20schema%3Atelephone%20%3Ftelephone%7D.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3AlaborDay%20%3FlaborDay%7D.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3Aschedule%20%3Fschedule%7D.%0A%0A%20%20%20%20%3Fs%20schema%3Aaddress%20%3Faddress.%0A%20%20%20%20%3Faddress%20schema%3AstreetAddress%20%3FstreetAddress.%0A%0A%09%3Faddress%20ont%3AhasDistrict%20%3Fdistrict.%0A%09%3Fdistrict%20ont%3Adistrict%20%3FdistrictName.%0A%0A%0A%20%20%20%20%3Faddress%20ont%3AhasNeighborhood%20%3Fneighborhood.%0A%20%20%20%20%3Fneighborhood%20ont%3Aneighborhood%20%3FneighborhoodName.%0A%20%20%0A%20%20%20%20OPTIONAL%20%7B%20%3Fs%20ont%3AhasAccessibility%20%3Faccessibility%7D.%0A%09OPTIONAL%20%7B%20%3Faccessibility%20ont%3AtypeAccessibility%20%3FtypeAccessibility%7D.%0A%20%20%20%20%0A%20%20%20%20%3Faccessibility%20ont%3AhasMetro%20%3Fmetro.%0A%20%20%20%20%3Fmetro%20owl%3AsameAs%20%3Fwiki.%0A%20%20"

    url += `%20%20%20filter%20%28contains%28%3Fname%20%2C%22${nameSearch}%22%29%29.%0A`

    if (line_filter != "") {
        url += `%20%20%20FILTER%28%3Fwiki%20IN%20%28${line_filter}%29%29.%0A%20`
    }
    if (district_filter != "") {
        url += `%20%20%20filter%20%28contains%28%3FdistrictName%20%2C%22${district_filter}%22%29%29.%0A`
    }
    if (access_filter != "") {
        url += `%20%20%20filter%20%28%3FtypeAccessibility%20%3D%20%22${access_filter}%22%20%29.%0A`
    }


    url += "%7D" 

    console.log(url)
    $.ajax({
        //url: "http://localhost:8080/sparql?query=PREFIX%20ont%3A%20%3Chttp%3A%2F%2Fsmartcity.linkeddata.es%2Fschoolfinder%2Fontology%2F%3E%0A%0ASELECT%20%3Fs%20%3Fname%20WHERE%20%7B%0A%20%20%3Fs%20a%20ont%3ASchool.%0A%20%20%3Fs%20ont%3Aname%20%3Fname%0A%7D%20%0ALIMIT%2010",
        async: false,

        url: url
        ,
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
            p = preprocessHelios(result)
            
            
        },
        error: function () {
            console.log("error");
        }
    });
    return p
}


function getWiki(line){

    console.log(line)
    var p;
    $.ajax({
        url: `https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=SELECT%20DISTINCT%20%3Fitem%20WHERE%20%7B%0A%20%20%3Fitem%20%28wdt%3AP31%2F%28wdt%3AP279%2A%29%29%20wd%3AQ928830%3B%0A%20%20%20%20wdt%3AP81%20wd%3A${line}.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20_%3Ab0%20ps%3AP197%20%3Fadjacent%3B%0A%20%20%20%20%20%20pq%3AP81%20wd%3A${line}.%0A%20%20%7D%0A%0A%7D%0AORDER%20BY%20%28%3FitemLabel%29`,
        async: false,

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
            p = preprocessWiki(result)
            
            
        },
        error: function () {
            console.log("error");
        }
    });
    return p
}


function preprocessHelios(json){
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

function preprocessWiki(json){
    var values = json['results']['bindings']


    let results = []


    for (var r of values){
        results.push(r['item']['value'])
    }


    return results
}


function addSchool(schoolCode){
    console.log(schoolCode);
}
function removeSchool(schoolCode){
    console.log(schoolCode);
}

function saveSchool(){
   schoolCode = ($(this).parent().parent()).html(); //se trae lo que está dentro de <div class="schoolItem">ESTO</div>
   state = $(this).children().css('color');
   if(state == 'rgb(121, 125, 237)'){
    //guardando...
    $(this).children().css('color','#00ff84');
    addSchool(schoolCode);
   }
   else{
    //eliminando...
    $(this).children().css('color','rgb(121, 125, 237)');
    removeSchool(schoolCode);
   }
}