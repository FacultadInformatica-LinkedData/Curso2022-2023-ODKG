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

$( document ).ready(function() {
    var savedSchools = [];
    $('#SchoolSearchForm').on('submit', (event) => {
        event.preventDefault();
        // handle the form data
        let schoolName = $('#schoolNameSearchBox').val(); //event.currentTarget[0].value;
        if(schoolName == null || schoolName == "" ) return null; 
        alert(schoolName);
        
        // Example on how to add a map dinamically

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
        $("#searchResults").show();

    });
    $('.schoolItem').on('click', flipItem);
});

function flipItem() {
    $(this).shake(100,10,3);
    $(this).find('.front').toggleClass("invisibleFront");
    $(this).find('.back').toggleClass("visibleBack");
}

