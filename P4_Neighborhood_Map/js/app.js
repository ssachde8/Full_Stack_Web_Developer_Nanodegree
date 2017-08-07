//'use strict';

var map;
var clientID;
var clientSecret;

/* Declare Model */
var model = [
	{
		name: 'Space Needle',
		lat: 47.620422,
		long: -122.349358
	},
	{
		name: 'Paramount Theatres',
		lat: 47.6134776,
		long: -122.3339499
	},
	{
		name: 'Klondike Gold Rush',
		lat: 47.6015297,
		long: -122.3344186
	},
	{
		name: 'Panama',
		lat: 47.6014549,
		long:-122.3343511
	},
	{
		name: 'Uwajimaya',
		lat: 47.6004565,
		long: -122.3319907
	},
	{
		name: 'BMW Seattle',
		lat: 47.596926,
		long: -122.3298664
	},
	{
		name: 'Big Picture',
		lat: 47.6232677,
		long: -122.3668976
	}
];

// Class for locations
var Location = function(data) {
	var self = this;
	this.name = data.name;
	this.lat = data.lat;
	this.long = data.long;
	this.url = "";
	this.street = "";
	this.city = "";
	this.visible = ko.observable(true); // set true to observe visible property

	// Use api to get info
	var foursquareURL = 'https://api.foursquare.com/v2/venues/search?ll='+ this.lat + ',' + this.long + '&client_id=' + clientID + '&client_secret=' + clientSecret + '&v=20160118' + '&query=' + this.name;

	// make ajax request to get venue data
	$.getJSON(foursquareURL).done(function(data) {
		var results = data.response.venues[0];
		// formattedAddress contains proper address string( conatins additional info sometimes )
		self.street = results.location.formattedAddress[0];
    self.city = results.location.formattedAddress[1];
		self.url = results.url;
		if (typeof self.url === 'undefined'){ // if url is not provided by foursquare
			self.url = ""; // leave blank
		}
	}).fail(function() {
		alert("Eror with the Foursquare API call. Try again.");
	});

	// infowindow data
	this.infoWindowContent = '<div><div><b>' + data.name + "</b></div>" +
        '<div><a href="' + self.url +'">' + self.url + "</a></div>" +
        '<div>' + self.street + "</div>" +
        '<div>' + self.city + "</div></div>";

	this.infoWindow = new google.maps.InfoWindow({content: self.infoWindowContent});

	this.marker = new google.maps.Marker({
			position: new google.maps.LatLng(data.lat, data.long),
			map: map,
			title: data.name
	});

	// set or unset marker
	this.showMarker = ko.computed(function() {
		if(this.visible() === true) {
			this.marker.setMap(map);
		} else {
			this.marker.setMap(null);
		}
		return true;
	}, this);


	this.marker.addListener('click', function(){
		self.contentString = '<div><div><b>' + data.name + "</b></div>" +
				'<div><a href="' + self.url +'">' + self.url + "</a></div>" +
        '<div>' + self.street + "</div>" +
        '<div>' + self.city + "</div></div>";
    self.infoWindow.setContent(self.contentString);
		self.infoWindow.open(map, this);
		self.marker.setAnimation(google.maps.Animation.DROP);
      	setTimeout(function() {
      		self.marker.setAnimation(null);
     	}, 1000);
	});

	this.activate = function(place) {
		google.maps.event.trigger(self.marker, 'click');
	};
};

/* Create ViewModel */
function ViewModel() {
	var self = this; // set local context
	this.locations = ko.observableArray([]); // locations array
	this.searchFor = ko.observable(""); // search box term
	map = new google.maps.Map(document.getElementById('map'), {
			zoom: 14,
			center: {lat: 47.6144342, lng: -122.3526924}
	});

	// Foursquare API settings
	clientID = "INUEKFIX5OBH3THBSCWVAYIV3RDUP34WBDMXNCQJE2BLBD3G";
	clientSecret = "LTGYIICPHUZQMLSWQLSYOE53MEHXGEPZ0IQJPXRGIJGN4BKB";

	model.forEach(function(loc){
		self.locations.push(new Location(loc));
	});

	// make markers visible on site load
	// logic for term
	this.places = ko.computed(function() {
		  var term = self.searchFor();
			if(!term){
				self.locations().forEach(function(loc){
					loc.visible(true);
				});
				return self.locations();
			} else{
				return ko.utils.arrayFilter(self.locations(), function(loc) {
				var searchTerm = loc.name.toLowerCase();
				var result = (searchTerm.search(term) >= 0);
				loc.visible(result);
				return result;
			});
		}
	}, self);
}

// make knockout active on ViewModel
function initApp() {
	ko.applyBindings(new ViewModel());
}

// handle any error
function error() {
	alert("Google Maps has failed to load. Please try again.");
}
