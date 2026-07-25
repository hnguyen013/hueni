/**
 * Digital map demo (Task 3.6) — khởi tạo Leaflet cho DigitalMap kiểu 'geojson'.
 * Chỉ chạy khi trang có nhúng Leaflet CDN (xem templates/showcase/_map.html,
 * chỉ nhúng khi lesson có ít nhất 1 map kiểu geojson).
 *
 * Cấu trúc DOM mong đợi:
 *   <div class="digital-map-leaflet" id="map-leaflet-<id>" data-geojson-url="...">
 *   <script type="application/json" id="map-markers-<id>">[{lat,lng,label,note}, ...]</script>
 */
(function () {
  'use strict';

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str || '';
    return div.innerHTML;
  }

  function initDigitalMap(container) {
    if (!window.L) return;

    var mapId = container.id.replace('map-leaflet-', '');
    var geojsonUrl = container.dataset.geojsonUrl;
    var markersScript = document.getElementById('map-markers-' + mapId);

    var markers = [];
    if (markersScript) {
      try {
        markers = JSON.parse(markersScript.textContent) || [];
      } catch (e) {
        markers = [];
      }
    }

    var map = L.map(container, { scrollWheelZoom: false });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors',
      maxZoom: 19
    }).addTo(map);

    var bounds = [];
    markers.forEach(function (m) {
      if (typeof m.lat !== 'number' || typeof m.lng !== 'number') return;
      var popupHtml = '<strong>' + escapeHtml(m.label) + '</strong>';
      if (m.note) popupHtml += '<br>' + escapeHtml(m.note);
      L.marker([m.lat, m.lng]).addTo(map).bindPopup(popupHtml);
      bounds.push([m.lat, m.lng]);
    });

    if (bounds.length) {
      map.fitBounds(bounds, { padding: [24, 24] });
    } else {
      // Fallback: trung tâm Việt Nam khi chưa có marker/geojson nào tải xong.
      map.setView([16.047079, 108.206230], 5);
    }

    if (geojsonUrl) {
      fetch(geojsonUrl)
        .then(function (res) { return res.json(); })
        .then(function (data) {
          var layer = L.geoJSON(data).addTo(map);
          var layerBounds = layer.getBounds();
          if (layerBounds.isValid()) {
            map.fitBounds(layerBounds, { padding: [24, 24] });
          }
        })
        .catch(function () {
          // Không tải được geojson (file lỗi/thiếu) — vẫn giữ marker đã vẽ, không chặn trang.
        });
    }
  }

  function init() {
    document.querySelectorAll('.digital-map-leaflet').forEach(initDigitalMap);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
