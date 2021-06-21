
// custom js

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
  });
}

function removeError(input) {
  input.removeClass('parsley-error');

  if (input.next().hasClass('parsley-errors-list')) {
      input.next().remove();
  }
}

function setError(input, msg) {
  // remove any error already set
  removeError(input);

  input.addClass('parsley-error');

  input.after(`
      <ul class="parsley-errors-list filled">
          <li class="parsley-required">${msg}</li>
      </ul>
  `);
}

function isValueEmpty(value) {
  return (
  value === null ||
  value === undefined ||
  (typeof value === "string" && value.trim() === "") ||
  (Array.isArray(value) && value.length === 0)
  );
};

var t1;
function validateForm(inputNames, isInputValid) {
  let firstErrorInput = null;

  // input loop
  for (let [index, inputName] of Object.entries(inputNames)) {
      const input = $(`[name=${inputName}]`).eq(0);
      const valid = isInputValid(input);

      if (!firstErrorInput && !valid) {
          firstErrorInput = input;
      }
  }
  
  // if any error found
  if (firstErrorInput) {

      clearTimeout(t1);
      t1 = setTimeout(function() {
        // focus on first error
        firstErrorInput.focus();

        // scroll to first error
        $([document.documentElement, document.body]).animate({
            scrollTop: firstErrorInput.offset().top
        }, 100);
      }, 0);

      // return false
      return false;

  } else {
      return true;
  }
}

// for multiple rows with same input name
var t2;
function validateFormMultipleRows(inputNames, isInputValid) {
  let firstErrorInput = null;

  // total number of rows
  const n = $(`[name=${inputNames[0]}]`).length;
  
  // row loop
  for (let i = 0; i < n; i++) {
      // input loop
      for (let [index, inputName] of Object.entries(inputNames)) {
          const input = $(`[name=${inputName}]`).eq(i);
          const valid = isInputValid(input);

          if (!firstErrorInput && !valid) {
              firstErrorInput = input;
          }
      }
  }

  // if any error found
  if (firstErrorInput) {

      clearTimeout(t2);
      t2 = setTimeout(function() {
        // focus on first error
        firstErrorInput.focus();

        // scroll to first error
        $([document.documentElement, document.body]).animate({
            scrollTop: firstErrorInput.offset().top
        }, 100);
      }, 0);

      // return false
      return false;

  } else {
      return true;
  }
}

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

// scroll and focus on an element
function focusElement(el) {
  const y = el.getBoundingClientRect().top + window.pageYOffset - 50;
  window.scrollTo({top: y, behavior: 'smooth'});
  el.focus();
}
