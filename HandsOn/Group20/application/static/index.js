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

// When an option is changed, search the above for matching choices
function myChange() {
  // Set selected option as variable
  var selectValue = $('#district').val();
  console.log(selectValue);
  // Empty the target field
  $('#subdistrict').empty();
  console.log(lookup[selectValue]);
  // For each choice in the selected option
  for (i = 0; i < lookup[selectValue].length; i++) {
    // Output choice in the target field
    $('#subdistrict').append(
      "<option value='" +
        lookup[selectValue][i] +
        "'>" +
        lookup[selectValue][i] +
        '</option>'
    );
  }
}

function initMap() {
  new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: { lat: 40.35, lng: -3.7 },
  });
}

function addMarker(lat, lng) {
  const pos = { lat: lat, lng: lng };
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: pos,
  });
  new google.maps.Marker({
    position: pos,
    map: map,
  });
}

function search() {
   
}

window.initMap = initMap;
