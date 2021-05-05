user_no_tracked_items_div = "<div class='row py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"

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

function updateChart(chart, updates) {
  chart.data.datasets[0].data = updates.dataset
  chart.data.labels = updates.label
  chart.update()
}

function clearChart(chart) {
  chart.data.labels.pop();
  chart.data.datasets.forEach((dataset) => {
    dataset.data.pop();
  });
  chart.update()
}


$("#stats_button_1").click(function () {
  buildChart()
})

if (page == "stats") { getTrackedItems() }

$(document).ready(function () {

  // id = $("#tracked_select_1 option:selected").attr("value")
  console.log($("#tracked_select_1 option:selected"))
  updates = {}
  $.ajax({
    type: "GET",
    url: getItemDataset_api.replace(0, 1),
    success: function (response) {

      content = response.itemSet
      if (content) {
        clearChart(chart1);
        updateChart(chart1, content);

      } else { console.log("Get Item Dataset error") }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
})