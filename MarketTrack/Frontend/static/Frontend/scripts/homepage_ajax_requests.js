// Ajax Requsts

user_no_tracked_items_div = "<div class='py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"

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

function buildCarouselItem(item, index) {
  carousel_item = `<div class="carousel-item ${index==0 ? 'active' : ''}">
  <div class="carousel_item_wrapper text-center">
  <h3 id="results_card_name">${item.name}</h3>
  <p>&pound;${item.price}</p>
  <p>${item.stock_bool}</p>
  <p>${item.abstract_source}</p>
  <div class="d-flex flex-row justify-content-center">
    <a href="${item.source}"
      class="btn std_button mr-3 search_result_button"> View on their
      website</a>
    <a class="btn std_button btn-secondary ml-3 search_result_button track_btn"
      id="track_button_${index==0? '1' : '2'}">Track</a>
  </div>
  </div>
  </div>`

  return carousel_item
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

          // Make Sure no more than 3 items get appended per row
          while (loopCond) {
            item_wireframe = content.pop()
            item = buildItemCard(item_wireframe)
            item_list.push(item)
            max += 1
            if (content.length == 0) { loopCond = false; }
            if (max == 3) { loopCond = false; }

          }
          // Remaining items get appended on rows
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

function hideResults() {
  row = "#search_results_row"
  if ($(row).hasClass("hidden")) {
    return true;
  }
  $(row).addClass("hidden")
}

function showResults() {
  row = "#search_results_row"
  if ($(row).hasClass("hidden")) {
    $(row).removeClass("hidden")
    return true;
  }
}

function toggleGettingResults(){
  row = "#gettingResults"
  if($(row).hasClass("hidden")){
    $(row).removeClass("hidden")
    return true;
  }
  $(row).addClass("hidden")
}

function searchForItem(query) {
  url_search = searchItem_api.replace("0", query)
  $.ajax({
    type: "GET",
    url: url_search,
    success: function (response) {
      if (response.error) {
        $("#search_modal").modal()
        $("#modal_error").empty();
        $("#modal_error").append(`<p class="text-danger p4 h5">${response.error}</p>`)
        return true;
      }

      if(response.items){
        $()
        content = response.items
        for(i = 0; i < content.length; i++){
          item_wireframe = content[i]
          if(i == 0){
            item = buildCarouselItem(item_wireframe, 0)
          }
          else{
            item = buildCarouselItem(item_wireframe, 1)
          }
          $(".carousel-inner").append(item)
          $("#track_button_1").on("click", function () {
            // e.preventDefault()
            new_item = { "name": null, "price": null, "stock": false, "source": null, "link": null }
            // Get Data
            parent = $(this).parent()
            children = $(parent).children()
            base_parent = $(parent).parent()
            data = $(base_parent).children().slice(0, 4)
            price = $(data[1]).text()
            priceLen = price.length
            price_edit = price.slice(1, priceLen)
            
            // Assign Data
            new_item.name = $(data[0]).text()
            new_item.price = price_edit
            new_item.stock = $(data[2]).text() == "Stock Available" ? true : false
            new_item.source = $(data[3]).text()
            new_item.link = $(children[0]).attr("href")
            
            console.log(`calling on ${this} for item`, new_item)
            // Call AJAX Request
            $.ajax({
              type: 'POST',
              headers: { "X-CSRFToken": token },
              url: postTracked_api,
              data: {
                'content': new_item
              },
              success: function (response) {
          
                if (response.error) {
                  $("#search_modal").modal()
                  $("#modal_error").empty();
                  $("#modal_error").append(`<p class="text-danger p4 h5">${response.error}</p>`)
                  return true;
                }
                item = buildItemCard(response.item)
                entry = $("#tracked_content").children()
                entryLen = entry.length
                entry = entry.slice(entryLen - 1, entryLen)
          
                // Check if row is full
                if ($(entry).children().length < 3) {
                  $(entry).append(item)
                }
                else {
                  $("#tracked_content").append(`<div class="row mt-5" id="tracked_row"></div>`)
                  $("#tracked_row").append(item)
                }
              },
              error: function (jqXHR, textStatus, errorThrown) {
                alert("textStatus: " + textStatus + " " + errorThrown)
              }
            })
          
          })
          $("#track_button_2").on("click", function() {
            new_item = { "name": null, "price": null, "stock": false, "source": null, "link": null }
            // Get Data
            parent = $(this).parent()
            children = $(parent).children()
            base_parent = $(parent).parent()
            data = $(base_parent).children().slice(0, 4)
            price = $(data[1]).text()
            priceLen = price.length
            price_edit = price.slice(1, priceLen)
          
            // Assign Data
            new_item.name = $(data[0]).text()
            new_item.price = price_edit
            new_item.stock = $(data[2]).text() == "Stock Available" ? true : false
            new_item.source = $(data[3]).text()
            new_item.link = $(children[0]).attr("href")
            
            console.log(`calling on ${this} for item`, new_item)
            console.log(`data[2].text is`, $(data[2]).text())
            // Call AJAX Request
            $.ajax({
              type: 'POST',
              headers: { "X-CSRFToken": token },
              url: postTracked_api,
              data: {
                'content': new_item
              },
              success: function (response) {
          
                if (response.error) {
                  $("#search_modal").modal()
                  $("#modal_error").empty();
                  $("#modal_error").append(`<p class="text-danger p4 h5">${response.error}</p>`)
                  return true;
                }
                item = buildItemCard(response.item)
                entry = $("#tracked_content").children()
                entryLen = entry.length
                entry = entry.slice(entryLen - 1, entryLen)
          
                // Check if row is full
                if ($(entry).children().length < 3) {
                  $(entry).append(item)
                }
                else {
                  $("#tracked_content").append(`<div class="row mt-5" id="tracked_row"></div>`)
                  $("#tracked_row").append(item)
                }
              },
              error: function (jqXHR, textStatus, errorThrown) {
                alert("textStatus: " + textStatus + " " + errorThrown)
              }
            })
          })
        }

        toggleGettingResults()
        showResults()
      }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

$("#search_button").click(function () {
  query = $("#search_bar").val()
  if(query == ""){
    $("#search_modal").modal()
    $("#modal_error").empty();
    $("#modal_error").append(`<p class="text-danger p4 h5">Can't search for empty input</p>`)
  }
  else{
    toggleGettingResults()
    $(".carousel-inner").empty()
    searchForItem(query)
  }
})

$("#searchClose").click(function () {
  hideResults()
  $(".carousel-inner").empty()
})
