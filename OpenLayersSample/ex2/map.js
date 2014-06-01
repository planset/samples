window.onload = function () {

  var projection = new OpenLayers.Projection("EPSG:900913");      // データソース、内部演算はWeb Mercator
  var displayProjection = new OpenLayers.Projection("EPSG:4326"); // 表示はWGS1984(経緯度)
    
  // Web Mercatorの最大領域[m]
  var googleMaxExtent = new OpenLayers.Bounds(-20037508.34, -20037508.34, 20037508.34, 20037508.34);

  // データ(画像)の最大領域 [degree]から[m]に投影変換
  var dataMaxExtent = new OpenLayers.Bounds(141.358820994, 42.585746919, 143.129487418, 43.688164196)
    .transform(displayProjection, projection);

  var map = new OpenLayers.Map(
    "map", // 地図を表示するdivのID
    { // 地図全般のオプション
      projection: projection,
      displayProjection: displayProjection,
      units: "m", // 座標単位はメートル
      maxResolution: 156543.0339,
      maxExtent: googleMaxExtent,
      controls: []
    }
  );

  // 画像パスを計算する関数
  // OpenLayers.Layer.TMSのgetURLメソッドをオーバーライドする
  // MapTilerが生成するソースを参考にしている
  var getTileURL = function (bounds) {
    // ----------------- ソースを追加する ---------------------- //
  };

  // ----------------- ソース(OpenLayers.Layer.TMS)を追加する ---------------------- //

  map.addLayers([layer]);
  map.zoomToExtent(dataMaxExtent);

  map.addControl(new OpenLayers.Control.Navigation());
  map.addControl(new OpenLayers.Control.PanZoomBar());
  map.addControl(new OpenLayers.Control.MousePosition());
  map.addControl(new OpenLayers.Control.KeyboardDefaults());
};
