// Map your choices to your option value
var lookup = {
  Arganzuela: [
    'Acacias',
    'Atocha',
    'Chopera',
    'Delicias',
    'Imperial',
    'Legazpi',
    'Palos De Moguer',
  ],
  Barajas: [
    'Aeropuerto',
    'Alameda De Osuna',
    'Casco H.Barajas',
    'Corralejos',
    'Timon',
  ],
  Carabanchel: [
    'Abrantes',
    'Buenavista',
    'Comillas',
    'Opañel',
    'Puerta Bonita',
    'San Isidro',
    'Vista Alegre',
  ],
  Centro: [
    'Cortes',
    'Embajadores',
    'Justicia',
    'Palacio',
    'Sol',
    'Universidad',
  ],
  Chamartin: [
    'Castilla',
    'Ciudad Jardin',
    'El Viso',
    'Hispanoamerica',
    'Nueva España',
    'Prosperidad',
  ],
  Chamberi: [
    'Almagro',
    'Arapiles',
    'Gaztambide',
    'Rios Rosas',
    'Trafalgar',
    'Vallehermoso',
  ],
  'Ciudad Lineal': [
    'Colina',
    'Concepcion',
    'Costillares',
    'Pueblo Nuevo',
    'Quintana',
    'San Juan Bautista',
    'San Pascual',
    'Ventas',
  ],
  'Fuencarral-El Pardo': [
    'El Goloso',
    'El Pardo',
    'El Pilar',
    'Fuentelarreina',
    'La Paz',
    'Mirasierra',
    'Peñagrande',
    'Valverde',
  ],
  Hortaleza: [
    'Apostol Santiago',
    'Canillas',
    'Palomas',
    'Pinar Del Rey',
    'Piovera',
    'Valdefuentes',
  ],
  Latina: [
    'Aluche',
    'Campamento',
    'Cuatro Vientos',
    'Las Aguilas',
    'Los Carmenes',
    'Lucero',
    'Puerta Del Angel',
  ],
  'Moncloa-Aravaca': [
    'Aravaca',
    'Arguelles',
    'Casa De Campo',
    'Ciudad Universitaria',
    'El Plantio',
    'Valdemarin',
    'Valdezarza',
  ],
  Moratalaz: [
    'Fontarron',
    'Horcajo',
    'Marroquina',
    'Media Legua',
    'Pavones',
    'Vinateros',
  ],
  'Puente de Vallecas': [
    'Entrevias',
    'Numancia',
    'Palomeras Bajas',
    'Palomeras Sureste',
    'Portazgo',
    'San Diego',
  ],
  Retiro: [
    'Adelfas',
    'Estrella',
    'Ibiza',
    'Jeronimos',
    'Niño Jesus',
    'Pacifico',
  ],
  Salamanca: [
    'Castellana',
    'Fuente Del Berro',
    'Goya',
    'Guindalera',
    'Lista',
    'Recoletos',
  ],
  'San Blas-Canillejas': [
    'Amposta',
    'Arcos',
    'Canillejas',
    'El Salvador',
    'Hellin',
    'Rejas',
    'Rosas',
    'Simancas',
  ],
  Tetuan: [
    'Almenara',
    'Bellas Vistas',
    'Berruguete',
    'Castillejos',
    'Cuatro Caminos',
    'Valdeacederas',
    'Ventilla',
  ],
  Usera: [
    'Almendrales',
    'Moscardo',
    'Orcasitas',
    'Orcasur',
    'Pradolongo',
    'San Fermin',
    'Zofio',
  ],
  Vicalvaro: ['Ambroz', 'Casco H.Vicalvaro', 'Valdebernardo', 'Valderrivas'],
  'Villa Vallecas': [
    'Casco H.Vallecas',
    'Ensanche De Vallecas',
    'Santa Eugenia',
  ],
  Villaverde: [
    'Butarque',
    'Los Angeles',
    'Los Rosales',
    'San Andres',
    'San Cristobal',
    'Villaverde Alto C.H.',
  ],
};

let map, infoWindow;
let markers = [];

function myChange() {
  var selectValue = $('#district').val();
  $('#subdistrict option').not(':first').remove();

  if (selectValue == '') {
    $('#subdistrict').attr('hidden', true);
  } else {
    for (const place of lookup[selectValue]) {
      $('#subdistrict').attr('hidden', false);
      $('#subdistrict').append(`<option value='${place}'>${place}</option>`);
    }
  }
}

const encodeForAjax = (data) => {
  return Object.keys(data)
    .map(function (k) {
      return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]);
    })
    .join('&');
};

const ajaxGet = (whereTo, responseHandler, data = null) => {
  httpRequest = new XMLHttpRequest();
  httpRequest.addEventListener('load', responseHandler);
  const url = data ? `${whereTo}?${encodeForAjax(data)}` : whereTo;
  httpRequest.open('get', url, true);
  httpRequest.send();
};

function initMap() {
  infoWindow = new google.maps.InfoWindow();
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: { lat: 40.41, lng: -3.7 },
  });
}

function addMarker(org, responseItem) {
  const marker = new google.maps.Marker({
    position: { lat: responseItem.latitude, lng: responseItem.longitude },
    map: map,
    title: responseItem.name,
    icon: {
      url: `http://maps.google.com/mapfiles/ms/icons/${orgToColor(
        org
      )}-dot.png`,
    },
  });

  marker.addListener('click', () => {
    const contentString = `
    <h5>${responseItem.name}</h5>
    <div style="text-align: left; ">
      <ul style="display: inline-block; text-align: left; ">
        <li><b>Number of affiliates:</b>  ${responseItem.num_affiliates}</li>
        <li><b>Telephone:</b> ${responseItem.telephone}</li>
        <li><b>Email:</b> ${responseItem.email}</li>
        <li><b>Website:</b> <a href="${responseItem.uri}">${responseItem.uri}</a></li>
        <li><b>Founding date:</b> ${responseItem.founding_date}</li>
      </ul>
    </div>`;

    infoWindow.close();
    infoWindow.setContent(contentString);
    infoWindow.open({
      anchor: marker,
      map,
    });
  });

  markers.push(marker);
}

function addResultsToMap(response) {
  Object.keys(response).forEach((org) => {
    response[org].forEach((responseItem) => addMarker(org, responseItem));
  });
}

function deleteMarkers() {
  markers.forEach((marker) => marker.setMap(null));
  markers = [];
}

function orgToColor(org) {
  if (org == 'Association') return 'red';
  else if (org == 'Collective') return 'orange';
  else if (org == 'Federation') return 'yellow';
  else if (org == 'Foundation') return 'blue';
  else print(`Unexpected org: ${org}`);
}

function search() {
  deleteMarkers();
  ajaxGet(
    '/search/',
    (r) => addResultsToMap(JSON.parse(r.target.responseText)),
    {
      district: $('#district').val(),
      subdistrict: $('#subdistrict').val(),
      purpose: $('#purpose').val(),
      organization: $('#organization').val(),
    }
  );
}

window.initMap = initMap;
