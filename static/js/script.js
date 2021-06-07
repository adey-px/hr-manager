// Table search functionality for employee directory
$(document).ready(function(){
    $("#tableSearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
// Search functionality for employee directory ends

// Set focus for table search in employees directory
document.getElementById("tableSearch").focus();
// Focus for table search ends
