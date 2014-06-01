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

  if (!map.getCenter()) {
    map.setCenter(new OpenLayers.LonLat(141.350864, 43.068640).transform(displayProjection, projection), 2);
  }

  map.addControl(new OpenLayers.Control.LayerSwitcher());
  map.addControl(new OpenLayers.Control.Navigation());
  map.addControl(new OpenLayers.Control.PanZoomBar());
  map.addControl(new OpenLayers.Control.MousePosition());
  map.addControl(new OpenLayers.Control.KeyboardDefaults());

};

// これ以降に function load****Layer() を追加する
