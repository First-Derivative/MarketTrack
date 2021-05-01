

// Switch Tracked/Collection Tabs
$("#tracked_display").click(function() {
  $(this).toggleClass("active")
  $("#collections_display").toggleClass("active")
})

$("#collections_display").click(function() {
  $(this).toggleClass("active")
  $("#tracked_display").toggleClass("active")
}) 