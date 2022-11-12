// Map your choices to your option value
var lookup = {
    '1': ['Acacias','Atocha','Chopera','Delicias','Imperial','Legazpi','Palos de Moguer'],
 };
 
 // When an option is changed, search the above for matching choices
function myChange() {
    // Set selected option as variable
    var selectValue = $('#district').val();
    console.log('boas');
    // Empty the target field
    $('#subdistrict').empty();
    console.log(lookup[selectValue]);
    // For each chocie in the selected option
    for (i = 0; i < lookup[selectValue].length; i++) {
       // Output choice in the target field
       $('#subdistrict').append("<option value='" + lookup[selectValue][i] + "'>" + lookup[selectValue][i] + "</option>");
    }
 };