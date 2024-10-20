// Initialize and add the map
let map;

async function initMap() {
  // The location of govenors island
  const position = { lat: 40.688811, lng: -74.019286 };
  //@ts-ignore
  const restaurant = { lat: 40.689209789619426, lng: -74.01699168814008};
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at govenors island
  map = new Map(document.getElementById("map"), {
    zoom: 17,
    center: position,
    mapId: "DEMO_MAP_ID",
    disableDefaultUI: true,
    
  });

  // The marker, positioned at insertRestaurant
  const marker = new AdvancedMarkerElement({
    map: map,
    position: restaurant,
    title: "exampleRestaurant",
  });
}

initMap();