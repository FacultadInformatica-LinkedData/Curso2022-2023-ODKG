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
    });
    $('.schoolItem').on('click', flipItem);
});

function flipItem() {
    $(this).shake(100,10,3);
    $(this).find('.front').toggleClass("invisibleFront");
    $(this).find('.back').toggleClass("visibleBack");
}

