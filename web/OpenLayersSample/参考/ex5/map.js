window.onload = function () {

  var projection = new OpenLayers.Projection("EPSG:900913");      // データソース、内部演算はWeb Mercator
  var displayProjection = new OpenLayers.Projection("EPSG:4326"); // 表示はWGS1984(経緯度)

  // 適当な区画
  var maxExtent = new OpenLayers.Bounds(141.300000, 43.030000, 141.440000, 43.100000)
    .transform(displayProjection, projection);

  var controls = [
    new OpenLayers.Control.Navigation(),
    new OpenLayers.Control.KeyboardDefaults(),
    new OpenLayers.Control.ArgParser(),
    new OpenLayers.Control.Permalink({
      div: OpenLayers.Util.getElement("ext_permalink")
    }),
    new OpenLayers.Control.PanZoomBar(),
    new OpenLayers.Control.LayerSwitcher(),
    new OpenLayers.Control.MousePosition(),
    new OpenLayers.Control.Attribution(),
    new OpenLayers.Control.Scale(),
    new OpenLayers.Control.ScaleLine()
  ];

  var map = new OpenLayers.Map(
    "map", // 地図を表示するdivのID
    { // 地図全般のオプション
      allOverlays: true,
      projection: projection,
      displayProjection: displayProjection,
      units: "m", // 座標単位はメートル
      maxExtent: maxExtent,
      numZoomLevels: 5,
      controls: controls
    }
  );

  loadPointLayer(map);
  loadLineLayer(map);
  loadPolygonLayer(map);

  createControlSelectFeature(map, ['Layer of Point', 'Layer of Line', 'Layer of Polygon']);

  if (!map.getCenter()) {
    map.setCenter(new OpenLayers.LonLat(141.350864, 43.068640).transform(displayProjection, projection), 2);
  }
};

function loadPointLayer(map)
{
  var style = new OpenLayers.StyleMap({
    'default': new OpenLayers.Style ({
      graphicName:"circle",
      strokeColor: "#ff0000",
      fillColor: "#ff00ff",
      strokeOpacity: 1.0,
      fillOpacity: 0.5,
      pointRadius: 15 // pixel
    })
  });

  var layer = new OpenLayers.Layer.Vector(
    'Layer of Point',
    { styleMap: style, attribution: 'Layer of Point' }
  );
  map.addLayer(layer);

  var geojson_format = new OpenLayers.Format.GeoJSON({
    externalProjection: new OpenLayers.Projection('EPSG:4326'),
    internalProjection: new OpenLayers.Projection('EPSG:900913')
  });

  loaded_data = geojson_format.read(input_geojson_point);
  layer.addFeatures(loaded_data);
  return;
}

function loadLineLayer(map)
{
  var style = new OpenLayers.StyleMap({
    'default': new OpenLayers.Style ({
      strokeColor: "${color}",
      strokeOpacity: 1.0,
      strokeWidth: 3
    })
  });

  var layer = new OpenLayers.Layer.Vector(
    'Layer of Line',
    { styleMap: style, attribution: 'Layer of Line' }
  );
  map.addLayer(layer);

  var geojson_format = new OpenLayers.Format.GeoJSON({
    externalProjection: new OpenLayers.Projection('EPSG:4326'),
    internalProjection: new OpenLayers.Projection('EPSG:900913')
  });

  loaded_data = geojson_format.read(input_geojson_line);
  layer.addFeatures(loaded_data);
  return;
}

function loadPolygonLayer(map)
{
  var style = new OpenLayers.StyleMap({
    'default': new OpenLayers.Style ({
      strokeColor: "#909090",
      fillColor: "#f0f0f0",
      strokeOpacity: 0.5,
      fillOpacity: 0.9,
    })
  });

  var layer = new OpenLayers.Layer.Vector(
    'Layer of Polygon',
    { styleMap: style, attribution: 'Layer of Polygon' }
  );
  map.addLayer(layer);

  var geojson_format = new OpenLayers.Format.GeoJSON({
    externalProjection: new OpenLayers.Projection('EPSG:4326'),
    internalProjection: new OpenLayers.Projection('EPSG:900913')
  });

  loaded_data = geojson_format.read(input_geojson_polygon);
  layer.addFeatures(loaded_data);
  return;
}

function createControlSelectFeature(map, layerNames)
{
  var targetLayers = [];
  for (var i = 0; i < layerNames.length; i++) {
    var layers = map.getLayersByName(layerNames[i]);
    targetLayers.push(layers[0]);
  }

  var control = new OpenLayers.Control.SelectFeature(
    targetLayers,
    {
      onSelect: onFeatureSelect, 
      onUnselect: onFeatureUnselect
    });
  map.addControl(control);
  control.activate();
}

function onFeatureSelect(feature) {
  var selectedFeature = feature;
  var selectControl = this;

  var onPopupClose = function (evt) {
    selectControl.unselect(selectedFeature);
  };

  var html = "<div>";
  for (var key in feature.attributes) {
    html += key + ":" + feature.attributes[key] + "<br>";
  }
  html += "</div>";

  var popup = new OpenLayers.Popup.FramedCloud("popup", 
    feature.geometry.getBounds().getCenterLonLat(),
    null, html, null, true, onPopupClose);

  feature.popup = popup;
  this.map.addPopup(popup);
  return;
}

function onFeatureUnselect(feature) {
  this.map.removePopup(feature.popup);
  feature.popup.destroy();
  feature.popup = null;
  return null;
}

