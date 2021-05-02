// Ajax Requsts

user_no_tracked_items_div = "<div class='py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"
user_no_collection_div = "<div class='py-5 text-center'> <p class='color_supp'>Looks like you don't have any collections, create a collection at the collections page</p> </div>"

unlogged_user_content_div = "<div class='p-5 text-center'><p class='color_supp'>Looks like you're not logged in, log in or create an account to track your items and make collections</p></div>"

// Homepage: tracked_display requests 
function getTrackedItems(obj) {

  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function(response){
      if(response.hasOwnProperty("noItems")){$("#tracked_content").append(user_no_tracked_items_div)}
      if(response.hasOwnProperty("noUser")){$("#tracked_content").append(unlogged_user_content_div)}

      console.log(response.tracked_items)
    },
    error: function(jqXHR, textStatus, errorThrown){
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

// Homepage: collection_display request
function getCollections(obj) {

  $.ajax({
    type: "GET",
    url: getCollections_api,
    success: function(response){
      
      if(response.hasOwnProperty("noCollections")){$("#collections_content").append(user_no_collection_div)}
      if(response.hasOwnProperty("noUser")){$("#collections_content").append(unlogged_user_content_div)}
      
    },
    error: function(jqXHR, textStatus, errorThrown){
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}