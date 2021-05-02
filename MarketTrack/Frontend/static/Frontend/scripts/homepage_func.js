// Assignment of functionality to DOM


// Requests on homepage load
$(document).ready(getTrackedItems($("#tracked_display")))

// Switch Tracked/Collection Tabs
$("#tracked_display").click(function() {
  
  if(!$(this).hasClass("active"))
  {
    // 
    $("#tracked_content").removeClass("hidden")
    $("#collections_display").removeClass("active")
    $("#collections_content").empty()
    
    
    $("#collections_content").addClass("hidden")
    $(this).addClass("active")
  }
  getTrackedItems($(this))
})

$("#collections_display").click(function() {

  if(!$(this).hasClass("active"))
  {
    // 
    $("#collections_content").removeClass("hidden")
    $("#tracked_display").removeClass("active")
    $("#tracked_content").empty()
    
    // 
    $("#tracked_content").addClass("hidden")
    $(this).addClass("active")

    
  }
  
  getCollections($(this))
}) 

