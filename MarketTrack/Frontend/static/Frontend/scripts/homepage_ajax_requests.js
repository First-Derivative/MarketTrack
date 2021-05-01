// Ajax Requsts

// Homepage: tracked_display requests 
function getTrackedItems(obj) {

  $.ajax({
    type: 'GET',
    url: "",
    success: function(response){
      // content = response.content
      
    },
    error: function(jqXHR, textStatus, errorThrown){
      alert("textStatus: " + textStatus + " " + errorThrown)
    }
  })

}
