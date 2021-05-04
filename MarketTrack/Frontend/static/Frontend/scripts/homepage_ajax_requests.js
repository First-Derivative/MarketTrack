// Ajax Requsts

user_no_tracked_items_div = "<div class='py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"
user_no_collection_div = "<div class='py-5 text-center'> <p class='color_supp'>Looks like you don't have any collections, create a collection at the collections page</p> </div>"

unlogged_user_content_div = "<div class='p-5 text-center'><p class='color_supp'>Looks like you're not logged in, log in or create an account to track your items and view stats</p></div>"

// <p class="card-text pl-1 text-left" id="item_stock_avail">Item Source: ${item.abstract_source}</p>
function buildItemCard(item) {
  item_card = `<div class="card results_card text-center ml-5">
  <div class="card-body" id="item_card_wrapper">
  <h5 class="card-title" id="item_title">${item.name}</h5>
  <p class="card-text pl-1 text-left" id="item_price_${item.id}">Price: &pound;${item.price}</p>
  <p class="card-text pl-1 text-left" id="item_stock_avail_${item.id}">Stock Availability: ${item.stock_bool}</p>
  <p class="card-text pl-1 text-left" id="item_source_abstract_${item.id}">Platform: ${item.abstract_source}</p>
  <p class="card-text pl-1 text-left small" id="item_timestamp_${item.id}">Last Checked: ${item.timestamp}</p>
  <a href="${item.source}" class="btn std_button mt-2 w-100" id="item_source_${item.id}">View on their site</a>
  </div>
  </div>`

  return item_card
}

// Homepage: tracked_display requests 
function getTrackedItems(obj) {

  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function (response) {
      if (response.hasOwnProperty("noItems")) { $("#tracked_content").append(user_no_tracked_items_div) }
      if (response.hasOwnProperty("noUser")) { $("#tracked_content").append(unlogged_user_content_div) }

      content = response.tracked_items
      if (content) {
        content.reverse()
        num_of_items = content.length
        num_of_rows = Math.ceil(num_of_items / 3)

        for (i = 0; i < num_of_rows; i++) {
          $("#tracked_content").append(`<div class="row mt-5" id="tracked_row_${i}"></div>`)
          row_identifier = "#tracked_row_" + i
          max = 0
          item_list = []
          loopCond = true
          console.log("loop no" + i)
          while (loopCond) {
            console.log("max is " + max)
            item_wireframe = content.pop()
            item = buildItemCard(item_wireframe)
            item_list.push(item)
            max += 1
            if (content.length == 0) { loopCond = false; }
            if (max == 3) { loopCond = false; }

          }
          for (j = 0; j < item_list.length; j++) {
            $(row_identifier).append(item_list[j])
          }
        }
      }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

// Homepage: collection_display request
function getCollections(obj) {

  $.ajax({
    type: "GET",
    url: getCollections_api,
    success: function (response) {

      if (response.hasOwnProperty("noCollections")) { $("#collections_content").append(user_no_collection_div) }
      if (response.hasOwnProperty("noUser")) { $("#collections_content").append(unlogged_user_content_div) }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}