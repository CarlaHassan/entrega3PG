document.getElementById('email').addEventListener('input', function(event) {
    var emailInput = event.target;
    var email = emailInput.value;
    
    if(validateEmail(email)) {
      emailInput.setCustomValidity(''); // Clear any previous validation message
    } else {
      emailInput.setCustomValidity('Invalid email'); // Set custom validation message
    }
  });
  
  function validateEmail(email) {
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }