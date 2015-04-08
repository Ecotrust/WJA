// POPUPS ///////////////////////////////////////////////////////////////////////

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

//Features ///////////////////////////////////////////////////////////////////////

var features = [];

for (var i = 0; i < sites.length; i++) {
  var geo = JSON.parse(sites[i].point);
  features.push({
    'type': 'Feature',
    'id': sites[i].id,
    'geometry': geo,
    'properties': sites[i]
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

// Layers ///////////////////////////////////////////////////////////////////////

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
  title: 'Base Map',
  source: new ol.source.OSM(),
  type: 'base',
  visible: true
});

var attribution = new ol.Attribution({
  html: 'Tiles &copy; <a href="http://services.arcgisonline.com/ArcGIS/' +
      'rest/services/World_Terrain_Base/MapServer">ArcGIS</a>'
});

var terrain = new ol.layer.Tile({
  title: "Terrain Base Map",
  source: new ol.source.XYZ({
    attributions: [attribution],
    url: "http://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}"
  }),
  type: 'base',
  visible: false
});

var natGeoAttribution = new ol.Attribution({
  html: 'Tiles &copy; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'
});

var natGeo = new ol.layer.Tile({
  title: "National Geographic Base Map",
  source: new ol.source.XYZ({
    attributions: [natGeoAttribution],
    url: "http://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}"
  }),
  type: 'base',
  visible: false
});

var baseMaps = new ol.layer.Group({
  'title': 'Base maps',
  layers: [baseLayer, terrain, natGeo]
});

var treatmentLayer = new ol.layer.Vector({
  title: 'Juniper Treatments',
  source: vectorSource,
  style: styleFunction
});

var acecLayer = new ol.layer.Tile({
  title:'Areas of Critical <br />Environmental Concern',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/acec/{z}/{x}/{y}.png'
  }),
  visible: false
});

var BLMMechTreatLayer = new ol.layer.Tile({
  title:'BLM Mechanical Treatment',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/blm_mech_treat/{z}/{x}/{y}.png'
  }),
  visible: false
});

var BLMGrazingAllotmentLayer = new ol.layer.Tile({
  title:'BLM Grazing Allotments',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/blm_grazing_allot/{z}/{x}/{y}.png'
  }),
  visible: false
});

var BLMLandsLayer = new ol.layer.Tile({
  title:'BLM Lands',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/blm_lands/{z}/{x}/{y}.png'
  }),
  visible: false
});


var overlays = new ol.layer.Group({
  'title': 'Overlays',
  layers: [BLMGrazingAllotmentLayer, BLMLandsLayer, acecLayer, BLMMechTreatLayer, treatmentLayer]
});

// SELECTION  ///////////////////////////////////////////////////////////////////////

// var center = ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857');
var center = [-13446448.706997469, 5479654.361694783];

var selectFeature = new ol.interaction.Select({
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
});

selectFeature.on('select', function(e) {
  if (e.selected.length > 0) {
    var feat = e.selected[0];
    var properties = feat.getProperties();
    var coordinate = [parseFloat(properties.longitude), parseFloat(properties.latitude)];
    var hdms = ol.coordinate.toStringHDMS(coordinate);

    popup_fields = [['date', 'Date'], ['treated_acres', 'Treated Acres'], ['juniper_phase', 'Phase']];

    table_html = '<table class="popup-table">';
    for (var i = 0; i < popup_fields.length; i++) {
      table_html = table_html + '<tr><td>' + popup_fields[i][1] +
        '</td><td> ' + properties[popup_fields[i][0]] + '</td></tr>';
    }
    table_html = table_html + '</table>';

    content.innerHTML = '<h3 class="popup-title">' + properties.name + ':</h3>' +
        '<div class="well">' + table_html +
        '</div><a href="/treatment/' + properties.id +
        '">More Info</a>';

    overlay.setPosition(ol.proj.transform(coordinate, 'EPSG:4326', 'EPSG:3857'));
  } else {
     overlay.setPosition(undefined);
  }
});

// MAP  ///////////////////////////////////////////////////////////////////////

var map = new ol.Map({
  interactions: ol.interaction.defaults().extend([
    selectFeature
  ]),
  layers: [baseMaps, overlays],
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

var layerSwitcher = new ol.control.LayerSwitcher({
        // tipLabel: 'Legend' // Optional label for button
});
map.addControl(layerSwitcher);

// map.getView().setCenter(ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857'));
