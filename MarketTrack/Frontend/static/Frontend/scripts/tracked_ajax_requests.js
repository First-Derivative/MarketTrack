// Ajax Requests

user_no_tracked_items_div = "<div class='d-flex justify-content-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"

unlogged_user_content_div = "<div class='row p-5 d-flex justify-content-center'><p class='color_supp'>Looks like you're not logged in, log in or create an account to track your items and view stats</p></div>"

// <p class="card-text pl-1 text-left" id="item_stock_avail">Item Source: ${item.abstract_source}</p>
function buildItemCard(item, id) {
  item_card = `<div class="card item_card text-center ml-5" id="item_card_${item.id}">
  <div class="card-body" id="item_card_wrapper">
  <h5 class="card-title" id="item_title">${item.name}</h5>
  <p class="card-text pl-1 text-left" id="item_price_${item.id}">Price: &pound;${item.price}</p>
  <p class="card-text pl-1 text-left" id="item_stock_avail_${item.id}">Stock Availability: ${item.stock_bool}</p>
  <p class="card-text pl-1 text-left" id="item_source_abstract_${item.id}">Platform: ${item.abstract_source}</p>
  <p class="card-text pl-1 text-left small" id="item_timestamp_${item.id}">Last Checked: ${item.timestamp}</p>
  
  <div>
  <a href="${item.source}" class="btn std_button mt-2 w-100" id="item_source">View on their site</a>
  </div>
  <a data-toggle="modal" data-target="#delete_modal_${item.id}" class="btn mt-2 w-100 item_delete_button btn-danger" id="delete_button_${item.id}">Delete</a>
  </div>
  </div>`

  return item_card
}
function buildDeleteFunc(item) {
  delete_button_modal = `<div class="modal fade text-center" id="delete_modal_${item.id}" tabindex="-1" aria-labelledby="modal_label_${item.id}" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content modal_delete">
      <div class="modal-header text-center">
        <h5 class="modal-title color_supp text-center pl-2" id="modal_label_${item.id}">Are you sure?</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body text-left p-4 pb-0">
        <span class="text-danger">Deleting:  ${item.name} </span> 
        <br>
        <br>
        You will no longer be tracking this item and it will no longer show under your
        'Tracked Items' display 
      </div>

      <div class="modal-footer pb-3 pt-0" style="border: none">
        <button type="button" class="btn btn-danger" id="confirm_delete_${item.id}">Delete</button>
      </div>
    </div>
  </div>
</div>`
  return delete_button_modal
}

// Tracked: tracked_display requests 
function getTrackedItems() {

  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function (response) {

      if (response.hasOwnProperty("noItems")) { $(".container").append(user_no_tracked_items_div); }
      if (response.hasOwnProperty("noUser")) { $(".container").append(unlogged_user_content_div); }

      content = response.tracked_items
      if (content) {
        content.reverse()
        num_of_items = content.length
        num_of_rows = Math.ceil(num_of_items / 3)

        for (i = 0; i < num_of_rows; i++) {
          $("#item_display").append(`<div class="row mt-5" id="tracked_row_${i}"></div>`)
          row_identifier = "#tracked_row_" + i
          max = 0
          item_list = []
          modal_list = []
          id_list = []
          loopCond = true
          $('#deleteForm').empty()
          while (loopCond) {
            item_wireframe = content.pop()

            item = buildItemCard(item_wireframe)
            modal = buildDeleteFunc(item_wireframe)

            $('#deleteForm').append(`<option name=${item_wireframe.id}>${item_wireframe.name}</option>`)
            item_list.push(item)
            modal_list.push(modal)
            id_list.push(item_wireframe.id)

            max += 1

            if (content.length == 0) { loopCond = false; }
            if (max == 3) { loopCond = false; }

          }
          for (j = 0; j < item_list.length; j++) {
            $(row_identifier).append(item_list[j])
            $(row_identifier).append(modal_list[j])
            $(`#confirm_delete_${id_list[j]}`).on("click", function () {
              id = $(this).attr('id')
              id = id.slice(15)
              modal_identifier = `#delete_modal_${id}`
              $(modal_identifier).modal('toggle')
              deleteItem(id)
            })
          }
        }
      }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

$("#deleteList_button").click(function () {
  id = $("#deleteForm option:selected").attr("name")
  deleteItem(id)

  $("#tracked_deleteList_Modal").modal('toggle')
})

// Tracked: delete_item requests
function deleteItem(item_id) {
  $.ajax({
    method: 'DELETE',
    headers: { "X-CSRFToken": token },
    url: deleteTrackedItem_api.replace(0, item_id),
    success: function () {
      base_identifier = `#item_card_${item_id}`
      parent = $(base_identifier).parent()

      $(base_identifier).remove()
      if (parent.children().length == 0) {
        parent.remove()
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

// Tracked: collection_display request
function getCollections() {

  $.ajax({
    type: "GET",
    url: getCollections_api,
    success: function (response) {
      if (response.hasOwnProperty("noCollections")) { $("#collection_display").append(user_no_collection_div) }
      if (response.hasOwnProperty("noUser")) { $("#collection_display").append(unlogged_user_content_div) }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })

}

// Activation for Ajax Request
if (page == "tracked") { getTrackedItems() }