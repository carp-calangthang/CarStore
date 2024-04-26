$("#view").click(function() {
    $(".products").toggleClass("products-table");
  });
  
  $(function() { 
    $("#search").keyup(function () { 
      var value = this.value.toLowerCase().trim(); 
      $(".product-grid tr").each(function (index) { 
        if (!index) return; 
        $(this).find("td").each(function () { 
          var id = $(this).text().toLowerCase().trim(); 
          var not_found = (id.indexOf(value) == -1); 
          $(this).closest('tr').toggle(!not_found); 
          return not_found; 
        }); 
      });
    }); 
  });