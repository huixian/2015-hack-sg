/* Add here all your JS customizations */

/*function initialize() {

var mapOptions =  {
    center: new google.maps.LatLng(1.340021, 103.825583),
    zoom: 12,
    zoomControl: true,
    zoomControlOptions: {
        style: google.maps.ZoomControlStyle.DEFAULT
    },
    disableDoubleClickZoom: false,
    mapTypeControl: true,
    mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
    },
    scaleControl: false,
    scrollwheel: true,
    panControl: false,
    streetViewControl: false,
    draggable : true,
    overviewMapControl: false,
    
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    styles: [{"featureType": "water","elementType": "geometry","stylers": [{ "color": "#193341" }]},{"featureType": "landscape","elementType": "geometry","stylers": [{ "color": "#2c5a71" }]},{"featureType": "road","elementType": "geometry","stylers": [{ "color": "#29768a" },{ "lightness": -37 }]},{"featureType": "poi","elementType": "geometry","stylers": [{ "color": "#406d80" }]},{"featureType": "transit","elementType": "geometry","stylers": [{ "color": "#406d80" }]},{"elementType": "labels.text.stroke","stylers": [{ "visibility": "on" },{ "color": "#3e606f" },{ "weight": 2 },{ "gamma": 0.84 }]},{"elementType": "labels.text.fill","stylers": [{ "color": "#ffffff" }]},{"featureType": "administrative","elementType": "geometry","stylers": [{ "weight": 0.6 },{ "color": "#1a3541" }]},{"elementType": "labels.icon","stylers": [{ "visibility": "off" }]},{"featureType": "poi.park","elementType": "geometry","stylers": [{ "color": "#2c5a71" }]}]
};

  var map = new google.maps.Map(document.getElementById('gmap'), mapOptions);

  var ctaLayer = new google.maps.KmlLayer({
    url: 'http://accessibility.place/static/SG_SUBZONE.kml'
  });
  ctaLayer.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);*/

console.log("loading...");

var findButton = document.getElementById('BtnSubmit');
var tagInput = document.getElementById('tagid');
var dateInput = document.getElementById('startdate');
var timeInput = document.getElementById('starttime');

JSONTest = function() {
    console.log("click on findButton");
    console.log(tagInput.value);
    console.log(dateInput.value);
    console.log(starttime.value);

    $.ajax({
        url: "http://localhost:8000/beacon/api/search/",
        type: "GET",
        data: { tag_id: tagInput.value, missing_ts: 12345 },
        dataType: "json",
        success: function (obj) {
            console.log("Success result");
            console.log(obj);

            var map = new google.maps.Map(document.getElementById('gmap'), {
                zoom: 10,
                center: new google.maps.LatLng(1.31474,103.86709),
                mapTypeId: google.maps.MapTypeId.ROADMAP 
            });

            var marker, i;

            for (var p in obj) {
                if( obj.hasOwnProperty(p) ) {
                    result = p + " , " + obj[p] + "\n";
                    console.log("> " + result);
                    var res = obj[p].split(",");
                    var lat = parseFloat(res[0]);
                    var lon = parseFloat(res[1]);
                    console.log(">> " + lat);
                    console.log(">> " + lon);

                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(lat, lon), map: map
                    });
                } 
            }       
        },

        error: function (xhr, ajaxOptions, thrownError) {
            console.log("Error result");
        // alert(xhr.status);
        // alert(thrownError);
        }
    });
};

findButton.addEventListener('click', JSONTest, false);

