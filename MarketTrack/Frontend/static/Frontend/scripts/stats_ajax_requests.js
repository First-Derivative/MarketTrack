user_no_tracked_items_div = "<div class='row py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"

var dataset_1 = [1, 3, 5, 6, 10]
var labels = ["A", "B", "C", "D", "E"]

function getTrackedItems() {

  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function (response) {

      if (response.hasOwnProperty("noItems")) { $("stats_info_display").append(user_no_tracked_items_div); }

      content = response.tracked_items
      if (content) {
        $('#tracked_select_1').empty()
        $('#tracked_select_2').empty()
        console.log
        for (i = 0; i < content.length; i++) {
          item = content[i]
          $('#tracked_select_1').append(`<option value=${item.id}>${item.name}</option>`)
          $('#tracked_select_2').append(`<option value=${item.id}>${item.name}</option>`)
        }
      }

    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
}

function buildChart() {
  data_set = [0, 2, 3, 5, 7, 10, 8, 11, 15]
}

$("#stats_button_1").click(function () {
  buildChart()
})

if (page == "stats") { getTrackedItems() }