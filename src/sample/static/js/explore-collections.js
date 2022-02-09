$(document).ready(function() {
  $(".sidebarCollapse").on("click", function() {
    $("#sidebar").toggleClass("active");
    $(this).toggleClass("active");
  });
});

// Sidebar
$(document).ready(function() {
  $('.sidebar-filter-btn').click(function() {
    $('.sidebar-btn-left').toggle();
    $('.sidebar-btn-right').toggle();
  });  
});

// $(document).ready(function() {
//   $('.sidebar-filter-btn').on('click', function() {
//     $('.sidebar-btn-right').hide(4500);
//     $('.sidebar-btn-left').show(4500);
//   });  
// });

// Sidebar Filter
$(document).ready(function() {
  $('.filter-status').on('click', function() {
    $('.filter-status-child').toggle();
});
});

$(document).ready(function() {
  $('.filter-price').on('click', function() {
    $('.filter-price-child').toggle();
});
});

$(document).ready(function() {
  $('.filter-chains').on('click', function() {
    $('.filter-chains-child').toggle();
});
});

$(document).ready(function() {
  $('.filter-on-sale').on('click', function() {
    $('.filter-on-sale-child').toggle();
});
});
