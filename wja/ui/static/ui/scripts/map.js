// POPUPS

/**
 * Elements that make up the popup.
 */
var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');


/**
 * Add a click handler to hide the popup.
 * @return {boolean} Don't follow the href.
 */
closer.onclick = function() {
  overlay.setPosition(undefined);
  closer.blur();
  return false;
};


/**
 * Create an overlay to anchor the popup to the map.
 */
var overlay = new ol.Overlay(/** @type {olx.OverlayOptions} */ ({
  element: container,
  autoPan: true,
  autoPanAnimation: {
    duration: 250
  }
}));

//Features

var features = [];

for (var i = 0; i < sites.length; i++) {
  var geo = JSON.parse(sites[i].point);
  features.push({
    'type': 'Feature',
    'geometry': geo
  });
}

var icon = new ol.style.Circle({
  radius: 5,
  fill: null,
  stroke: new ol.style.Stroke({color: 'red', width: 1})
});

var styles = {
  'Point': [new ol.style.Style({
    image: icon
  })]
};

var styleFunction = function(feature, resolution) {
  return styles[feature.getGeometry().getType()];
};

var vectorSource = new ol.source.GeoJSON(
    /** @type {olx.source.GeoJSONOptions} */ ({
      object: {
        'type': 'FeatureCollection',
        'crs': {
          'type': 'name',
          'properties': {
            'name': 'EPSG:3857'
          }
        },
        'features': features
      }
    })
);

var treatmentStyle = new ol.style.Style({
  'pointRadius': 4,
  'strokeWidth': 2,
  'strokeColor': '#DDAA00',
  'fillColor': '#DDAA00',
  'fillOpacity': 0.2
});

var baseLayer = new ol.layer.Tile({
  source: new ol.source.OSM()
});

var treatmentLayer = new ol.layer.Vector({
  source: vectorSource,
  style: styleFunction
});

// var center = ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857');
var center = [-13446448.706997469, 5479654.361694783];

var map = new ol.Map({
  interactions: ol.interaction.defaults().extend([
    new ol.interaction.Select({
      style: new ol.style.Style({
        image: new ol.style.Circle({
          radius: 5,
          fill: new ol.style.Fill({
            color: '#FF0000'
          }),
          stroke: new ol.style.Stroke({
            color: '#000000'
          })
        })
      })
    })
  ]),
  layers: [baseLayer, treatmentLayer],
  controls: ol.control.defaults({
    attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
      collapsible: false
    })
  }),
  // renderer: exampleNS.getRendererFromQueryString(),
  target: 'map',
  overlays: [overlay],
  view: new ol.View({
    center: center,
    zoom: 6
  })
});

// map.getView().setCenter(ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857'));


/**
 * Add a click handler to the map to render the popup.
 */
map.on('singleclick', function(evt) {
  var coordinate = evt.coordinate;
  var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
      coordinate, 'EPSG:3857', 'EPSG:4326'));

  content.innerHTML = '<p>You clicked here:</p><code>' + hdms +
      '</code>';
  overlay.setPosition(coordinate);
});
