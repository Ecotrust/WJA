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
  layers: [baseLayer, treatmentLayer],
  controls: ol.control.defaults({
    attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
      collapsible: false
    })
  }),
  // renderer: exampleNS.getRendererFromQueryString(),
  target: 'map',
  view: new ol.View({
    center: center,
    zoom: 6
  })
});

// map.getView().setCenter(ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857'));