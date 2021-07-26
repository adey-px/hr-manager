$(document).ready(function(){
  // Live search functionality for employee directory
    $("#tableSearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
// Search functionality for employee directory ends

// New employee form inputs validation
    (function() {
      'use strict';
      window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
      if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
      }
      form.classList.add('was-validated');
      }, false);
      });
      }, false);
      })();
  // New employee form inputs validation ends

  // Flash message close x button
  document.getElementById("closeButton").addEventListener("click", function(e) {
    e.preventDefault();
    this.parentNode.style.display = "none";
  }, false);
  // Flash message close x button ends
});

// Set focus for Live search in employees directory
document.getElementById("tableSearch").focus();
// Focus for table search ends

// Alert to confirm delete of messages in message.html
function ConfirmDelete()
    {
      var x = confirm("Are you sure you want to delete this message?");
      if (x)
          return true;
      else
        return false;
    }
// Alert to confirm delete of messages in message.html ends
