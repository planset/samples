window.onload = function () {

  var projection = new OpenLayers.Projection("EPSG:900913");      // データソース、内部演算はWeb Mercator
  var displayProjection = new OpenLayers.Projection("EPSG:4326"); // 表示はWGS1984(経緯度)

  // 適当な区画
  var maxExtent = new OpenLayers.Bounds(141.300000, 43.030000, 141.440000, 43.100000)
    .transform(displayProjection, projection);

  var map = new OpenLayers.Map(
    "map", // 地図を表示するdivのID
    { // 地図全般のオプション
      allOverlays: true,
      projection: projection,
      displayProjection: displayProjection,
      units: "m", // 座標単位はメートル
      maxExtent: maxExtent,
      numZoomLevels: 5,
      controls: []
    }
  );

  loadPointLayer(map);
  loadLineLayer(map);
  loadPolygonLayer(map);

  
  if (!map.getCenter()) {
    map.setCenter(new OpenLayers.LonLat(141.350864, 43.068640).transform(displayProjection, projection), 2);
  }

  map.addControl(new OpenLayers.Control.LayerSwitcher());
  map.addControl(new OpenLayers.Control.Navigation());
  map.addControl(new OpenLayers.Control.PanZoomBar());
  map.addControl(new OpenLayers.Control.MousePosition());
  map.addControl(new OpenLayers.Control.KeyboardDefaults());

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
    { styleMap: style }
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
    { styleMap: style }
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
    { styleMap: style }
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
