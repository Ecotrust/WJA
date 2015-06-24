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

var icon = new ol.style.Icon(
  ({
      anchor:[0.5, 1],
      anchorOrigin: 'top-left',
      src: '/static/ui/images/marker.png',
      opacity: 1,
      scale: 0.5
  })
);

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

// BASE LAYERS -----------------------------------------------------

var osmLayer = new ol.layer.Tile({
  title: 'Open Street Map',
  source: new ol.source.OSM(),
  type: 'base',
  visible: false
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
  title: "National Geographic",
  source: new ol.source.XYZ({
    attributions: [natGeoAttribution],
    url: "http://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}"
  }),
  type: 'base',
  visible: false
});

var topoAttribution = new ol.Attribution({
  html: 'Tiles &copy; <a href="http://services.arcgisonline.com/ArcGIS/' +
      'rest/services/World_Topo_Map/MapServer">ArcGIS, USGS</a>'
});

var topoMapDigital = new ol.layer.Tile({
  title: "Topo Map",
  source: new ol.source.XYZ({
    attributions: [topoAttribution],
    url: "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"
  }),
  type: 'base',
  visible: false
});

// var topoQuadResolutions = [
//   156543.03392804097,
//   78271.51696402048,
//   39135.75848201024,
//   19567.87924100512,
//   9783.93962050256,
//   4891.96981025128,
//   2445.98490512564,
//   1222.99245256282,
//   611.49622628141,
//   305.748113140705,
//   152.8740565703525,
//   76.43702828517625,
//   38.21851414258813,
//   19.109257071294063,
//   9.554628535647032,
//   4.777314267823516
// ];

// var topoMapQuads = new ol.layer.Tile({
//   title: "Topo Map (Quads)",
//   source: new ol.source.XYZ({
//     attributions: [topoAttribution],
//     // tileGrid: new ol.tilegrid.TileGrid({
//     //   resolutions: topoQuadResolutions
//     // }),
//     url: "http://server.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{z}/{y}/{x}"
//   }),
//   minResolution: 4.777314267823516,
//   type: 'base',
//   visible: false
// });

var mapquestAttribution = new ol.Attribution({
  html: '<p>Tiles Courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png"></p>'
});

var mapquestHybridBaseLayer = new ol.layer.Tile({
  title: 'Hybrid',
  visible: true,
  type: 'base',
  source: new ol.source.MapQuest({layer: 'sat'})
});

var mapquestHybridLabelLayer = new ol.layer.Tile({
  visible: true,
  source: new ol.source.MapQuest({layer: 'hyb'})
});

var mapquestHybrid = new ol.layer.Group({
  title: 'Hybrid-Header',
  style: 'AerialWithLabels',
  layers: [
    mapquestHybridBaseLayer,
    mapquestHybridLabelLayer
  ]
});

var baseMaps = new ol.layer.Group({
  'title': 'Base maps',
  layers: [topoMapDigital, natGeo, osmLayer, mapquestHybrid]
});

 // OVERLAYS -----------------------------------------------------

var treatmentLayer = new ol.layer.Vector({
  // title: 'Juniper Treatments',
  source: vectorSource,
  style: styleFunction
});

var SageGrouseGenHabitat = new ol.layer.Tile({
  title:'Sage Grouse General Hab.',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/sage_grouse_lowden/{z}/{x}/{y}.png'
  }),
  visible: false
});

var SageGrousePriorityHabitat = new ol.layer.Tile({
  title:'Sage Grouse Priority Hab.',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/sage_grouse_core/{z}/{x}/{y}.png'
  }),
  visible: false
});

var USFWSLands = new ol.layer.Tile({
  title:'USFWS Lands',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/USFWS_lands/{z}/{x}/{y}.png'
  }),
  visible: false
});

var Slope20 = new ol.layer.Tile({
  title:'Slope > 20%',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/slope_gt_20/{z}/{x}/{y}.png'
  }),
  visible: false
});

var HwyAttribution = new ol.Attribution({
  html: 'Source: ESRI, Tele Atlas North America'
});

var ESRIHighways = new ol.layer.Tile({
  title:'Major USA Highways',
  source: new ol.source.XYZ({
    attributions: [HwyAttribution],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/ESRI_highways/{z}/{x}/{y}.png'
  }),
  visible: false
});

var acecLayer = new ol.layer.Tile({
  title:'Areas of Critical Env. Concern',
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

var landOwnership = new ol.layer.Tile({
  title:'Ownership',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://tiles.ecotrust.org/tiles/LOT_protareas/{z}/{x}/{y}.png'
  }),
  visible: false
});

var counties = new ol.layer.Tile({
  title:'County Boundaries',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://tiles.ecotrust.org/tiles/LOT_counties/{z}/{x}/{y}.png'
  }),
  visible: false
});

var publicRoads = new ol.layer.Tile({
  title:'Public Roads',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/public_rds/{z}/{x}/{y}.png'
  }),
  visible: false
});

var juniperPhase1 = new ol.layer.Tile({
  title:'Juniper Phase 1 (INR)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/pngs/JUNP1/{z}/{x}/{y}.png'
  }),
  visible: false
});

var juniperPhase2 = new ol.layer.Tile({
  title:'Juniper Phase 2 (INR)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/pngs/JUNP2/{z}/{x}/{y}.png'
  }),
  visible: false
});

var juniperPhase3 = new ol.layer.Tile({
  title:'Juniper Phase 3 (INR)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/pngs/JUNP3/{z}/{x}/{y}.png'
  }),
  visible: false
});

var juniperPhase50 = new ol.layer.Tile({
  title:'Juniper 50%+ (INR)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/pngs/INR_GTR50/{z}/{x}/{y}.png'
  }),
  visible: false
});

var ILAPJunP1 = new ol.layer.Tile({
  title:'Juniper Phase 1 (ILAP)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/jun_p1/{z}/{x}/{y}.png'
  }),
  visible: false
});

var ILAPJunP2 = new ol.layer.Tile({
  title:'Juniper Phase 2 (ILAP)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/jun_p2/{z}/{x}/{y}.png'
  }),
  visible: false
});

var ILAPJunP3 = new ol.layer.Tile({
  title:'Juniper Phase 3 (ILAP)',
  source: new ol.source.XYZ({
    attributions: [],
    url: 'http://apps.ecotrust.org/tiles/juniper/arc2earth/jun_p3/{z}/{x}/{y}.png'
  }),
  visible: false
});

var ILAPLayers = new ol.layer.Group({
  'title': 'ILAP Data',
  layers: [
    ILAPJunP3,
    ILAPJunP2,
    ILAPJunP1
  ]
});

var INRLayers = new ol.layer.Group({
  'title': 'INR Data',
  layers: [
    juniperPhase50,
    juniperPhase3,
    juniperPhase2,
    juniperPhase1
  ]
});

var juniperLayers = new ol.layer.Group({
  'title': 'Juniper',
  layers: [
    ILAPLayers,
    INRLayers
  ]
});

var treatmentLayers = new ol.layer.Group({
  layers: [treatmentLayer]
});

var overlays = new ol.layer.Group({
  'title': 'Overlays',
  layers: [
    // BLMGrazingAllotmentLayer,
    // acecLayer,
    // BLMMechTreatLayer,
    publicRoads,
    ESRIHighways,
    Slope20,
    counties,
    // USFWSLands,
    // BLMLandsLayer,
    landOwnership,
    SageGrousePriorityHabitat,
    SageGrouseGenHabitat
  ]
});

// SELECTION  ///////////////////////////////////////////////////////////////////////

// var center = ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857');
var center = [-13446448.706997469, 5479654.361694783];

var selectFeature = new ol.interaction.Select({
  style: new ol.style.Style({
    image: new ol.style.Icon(
      ({
          anchor:[0.5, 1],
          anchorOrigin: 'top-left',
          src: '/static/ui/images/marker-selected.png',
          opacity: 1,
          scale: 0.5
      })
    )
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

var viewResolutions = [
  // 156543.03392804097,
  // 78271.51696402048,
  // 39135.75848201024,
  // 19567.87924100512,
  // 9783.93962050256,
  // 4891.96981025128,
  2445.98490512564,       //6
  1222.99245256282,
  611.49622628141,
  305.748113140705,
  152.8740565703525,
  76.43702828517625,
  38.21851414258813       //12
  // 19.109257071294063,
  // 9.554628535647032,
  // 4.777314267823516,
  // 2.388657133911758,
  // 1.194328566955879,
  // 0.5971642834779395,
  // 0.29858214173896974,
  // 0.14929107086948487
];

var map = new ol.Map({
  interactions: ol.interaction.defaults().extend([
    selectFeature
  ]),
  layers: [baseMaps, overlays, juniperLayers, treatmentLayers],
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
    zoom: 7,
    minZoom: 6,
    maxZoom: 15,
    resolutions: viewResolutions
  })
});

var layerSwitcher = new ol.control.LayerSwitcher({
        // tipLabel: 'Legend' // Optional label for button
});
map.addControl(layerSwitcher);

$('.layer-switcher').mouseenter(function() {
  $('.layer-switcher').find('.group').find('.group').find( ":contains('Hybrid-Header')" ).css('visibility', 'hidden');
  $('.layer-switcher').find('.group').find('.group').find('li').find(":contains('Hybrid')").parent().css('margin-left', '-10px');
  $('.layer-switcher').find('.group').find('.group').find('li').find(":contains('Hybrid')").parent().css('margin-top', '-30px');
});

// hybridInput = $('input[id^="Hybrid"]'); //jquery retains entire state - this will never change
$('.layer-switcher').click(function() {
  if($('input[id^="Hybrid"]').is(':checked')) {
    mapquestHybridLabelLayer.setVisible(true);
  } else {
    mapquestHybridLabelLayer.setVisible(false);
  }
});

// map.getView().setCenter(ol.proj.transform([-122, 45], 'EPSG:4326', 'EPSG:3857'));
