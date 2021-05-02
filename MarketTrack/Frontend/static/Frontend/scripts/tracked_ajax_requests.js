// Ajax Requests

user_no_tracked_items_div = "<div class='row py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"
user_no_collection_div = "<div class='row py-5 text-center'> <p class='color_supp'>Looks like you don't have any collections, create a collection at the collections page</p> </div>"

unlogged_user_content_div = "<div class='row p-5 text-center'><p class='color_supp'>Looks like you're not logged in, log in or create an account to track your items and make collections</p></div>"

// <p class="card-text pl-1 text-left" id="item_stock_avail">Item Source: ${item.abstract_source}</p>
function buildItemCard(item)
{
  item_card = `<div class="card item_card text-center ml-5">
  <div class="card-body" id="item_card_wrapper">
  <h5 class="card-title" id="item_title">${item.name}</h5>
  <p class="card-text pl-1 text-left" id="item_price">Price: &pound;${item.price}</p>
  <p class="card-text pl-1 text-left" id="item_stock_avail">Stock Availability: ${item.stock_bool}</p>
  <p class="card-text pl-1 text-left small" id="item_timestamp">Last Checked: ${item.timestamp}</p>
  <a href="${item.source}" class="btn std_button mt-2" id="item_source">View on their site</a>
  </div>
  </div>`

  return item_card
}

// Tracked: tracked_display requests 
function getTrackedItems() {
  
  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function(response){
      
      if(response.hasOwnProperty("noItems")){$(".container").append(user_no_tracked_items_div); return 0;}
      if(response.hasOwnProperty("noUser")){$(".container").append(unlogged_user_content_div); return 0;}
      
      content = response.tracked_items
      content.reverse()
      num_of_items = content.length
      num_of_rows = Math.ceil(num_of_items/3)
      
      for(i = 0; i < num_of_rows; i++)
      {
        $("#item_display").append(`<div class="row mt-5" id="tracked_row_${i}"></div>`)
        row_identifier = "#tracked_row_" + i
        max = 0
        item_list = []
        loopCond = true
        console.log("loop no" + i)
        while(loopCond)
        {
          console.log("max is " + max)
          item_wireframe = content.pop()
          item = buildItemCard(item_wireframe)
          item_list.push(item)
          max += 1
          if(content.length == 0){loopCond = false;}
          if(max == 3){loopCond = false;}

        }
        for(j = 0; j < item_list.length; j++)
        {
          $(row_identifier).append(item_list[j])
        }
      }

    },
    error: function(jqXHR, textStatus, errorThrown){
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

// Tracked: collection_display request
function getCollections() {

  $.ajax({
    type: "GET",
    url: getCollections_api,
    success: function(response){
      if(response.hasOwnProperty("noCollections")){$("#collection_display").append(user_no_collection_div)}
      if(response.hasOwnProperty("noUser")){$("#collection_display").append(unlogged_user_content_div)}
      
    },
    error: function(jqXHR, textStatus, errorThrown){
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })

}

// Activation for Ajax Request
if(page == "tracked"){getTrackedItems()}
if(page == "collections"){getCollections()}