window.onload = function () {
  var map = new OpenLayers.Map(
    "map", // 地図を表示するdivのID
    {
      numZoomLevels: 4
      // resolutions: [0.25, 0.5, 1.0, 2.0] // 地図の表示解像度
    }
  );
  var layer = new OpenLayers.Layer.Image(
    "Image Layer", // レイヤ名
    "map.png",  // 画像のURL
    new OpenLayers.Bounds(0,0,1280,720), // 画像を投影する矩形の左下・右上座標
    new OpenLayers.Size(1280,720) // 画像サイズ
  );
  map.addLayers([layer]);
  map.setCenter(new OpenLayers.LonLat(640,360));
};
