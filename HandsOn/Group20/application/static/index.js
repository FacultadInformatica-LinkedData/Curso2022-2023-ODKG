// Map your choices to your option value
var lookup = {
    '1': ['Acacias','Atocha','Chopera','Delicias','Imperial','Legazpi','Palos De Moguer'],
    '2': ['Aeropuerto','Alameda De Osuna','Casco H.Barajas','Corralejos','Timon'],
    '3': ['Abrantes','Buenavista','Comillas','Opañel','Puerta Bonita','San Isidro','Vista Alegre'],
    '4': ['Cortes','Embajadores','Justicia','Palacio','Sol','Universidad'],
    '5': ['Castilla','Ciudad Jardin','El Viso','Hispanoamerica','Nueva España','Prosperidad'],
    '6': ['Almagro','Arapiles','Gaztambide','Rios Rosas','Trafalgar','Vallehermoso'],
    '7': ['Colina','Concepcion','Costillares','Pueblo Nuevo','Quintana','San Juan Bautista','San Pascual','Ventas'],
    '8': ['El Goloso','El Pardo','El Pilar','Fuentelarreina','La Paz','Mirasierra','Peñagrande','Valverde'],
    '9': ['Apostol Santiago','Canillas','Palomas','Pinar Del Rey','Piovera','Valdefuentes'],
    '10': ['Aluche','Campamento','Cuatro Vientos','Las Aguilas','Los Carmenes','Lucero','Puerta Del Angel'],
    '11': ['Aravaca','Arguelles','Casa De Campo','Ciudad Universitaria','El Plantio','Valdemarin','Valdezarza'],
    '12': ['Fontarron','Horcajo','Marroquina','Media Legua','Pavones','Vinateros'],
    '13': ['Entrevias','Numancia','Palomeras Bajas','Palomeras Sureste','Portazgo','San Diego'],
    '14': ['Adelfas','Estrella','Ibiza','Jeronimos','Niño Jesus','Pacifico'],
    '15': ['Castellana','Fuente Del Berro','Goya','Guindalera','Lista','Recoletos'],
    '16': ['Amposta','Arcos','Canillejas','El Salvador','Hellin','Rejas','Rosas','Simancas'],
    '17': ['Almenara','Bellas Vistas','Berruguete','Castillejos','Cuatro Caminos','Valdeacederas','Ventilla'],
    '18': ['Almendrales','Moscardo','Orcasitas','Orcasur','Pradolongo','San Fermin','Zofio'],
    '19': ['Ambroz','Casco H.Vicalvaro','Valdebernardo','Valderrivas'],
    '20': ['Casco H.Vallecas','Ensanche De Vallecas','Santa Eugenia'],
    '21': ['Butarque','Los Angeles','Los Rosales','San Andres','San Cristobal','Villaverde Alto C.H.'],
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
       $('#subdistrict').append("<option value='" + lookup[selectValue][i] + "'>" + lookup[selectValue][i] + "</option>");
    }
 };