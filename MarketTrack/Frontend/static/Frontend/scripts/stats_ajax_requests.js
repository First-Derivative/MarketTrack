user_no_tracked_items_div = "<div class='row py-5 text-center'><p class='color_supp'>Looks like you don't have any tracked items, search for some items to track!</p></div>"

function getTrackedItems() {

  $.ajax({
    type: "GET",
    url: getTracked_api,
    success: function (response) {

      if (response.hasOwnProperty("noItems")) { $("stats_info_display").append(user_no_tracked_items_div); return true; }

      content = response.tracked_items
      if (content) {
        $('#tracked_select_1').empty()
        $('#tracked_select_2').empty()
        console.log
        for (i = 0; i < content.length; i++) {
          item = content[i]
          $('#tracked_select_1').append(`<option name=${item.id}>${item.name}</option>`)
          $('#tracked_select_2').append(`<option name=${item.id}>${item.name}</option>`)
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
  id = $("#tracked_select_1 option:selected").attr("name")
  $.ajax({
    type: "GET",
    url: getItemDataset_api.replace(0, id),
    success: function (response) {

      if (response.error) {
        $("#stats_modal").modal()
        $("#modal_error").empty();
        $("#modal_error").append(`<p class="text-danger">${response.error}</p>`)
        return true;
      }

      content = response.itemSet
      if (content) {
        clearChart(chart1);
        updateChart(chart1, content);
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
})


$("#stats_button_2").click(function () {
  id = $("#tracked_select_2 option:selected").attr("name")
  $.ajax({
    type: "GET",
    url: getItemDataset_api.replace(0, id),
    success: function (response) {

      if (response.error) {
        console.log("STATS GOT ERROR")
        $("#stats_modal").modal()
        $("#modal_error").empty();
        $("#modal_error").append(`<p class="text-danger">${response.error}</p>`)
        return true;
      }

      content = response.itemSet
      if (content) {
        clearChart(chart2);
        updateChart(chart2, content);

      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })
})

if (page == "stats") { getTrackedItems() }
