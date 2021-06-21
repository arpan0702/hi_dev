
// custom js

// allow only whole numbers and one decimal
function allowOnlyAmount(input) {
  input.on('input', function() {
    $(this).val($(this).val().replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1'));
  });
}

// for dynamically created elements
function allowOnlyAmountDynamic(ancestor, selector) {
  ancestor.on('input', selector, function(){
    $(this).val($(this).val().replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1'));
  });
}

// allow only whole numbers
function allowOnlyNumeric(input) {
  input.on('keypress', function(event) {
    return (event.charCode == 8 || event.charCode == 0 || event.charCode == 13) ? null : event.charCode >= 48 && event.charCode <= 57;
  });
}

// for dynamically created elements
function allowOnlyNumericDynamic(ancestor, selector) {
  ancestor.on('keypress', selector, function(event) {
    return (event.charCode == 8 || event.charCode == 0 || event.charCode == 13) ? null : event.charCode >= 48 && event.charCode <= 57;
  });
}
