$(document).ready(function() {
  // $.get("https://swapi.co/api/people", function(data) {
  //   for(let result of data.results) {
  //     console.log(result.name);
  //   }
  // });

  $.ajax({
    url: "https://swapi.co/api/people",
    method: 'GET',
    success: function (data) {
      for(let result of data.results) {
        console.log(result.name);
      }
    },
    error: function(err) {
      console.log(err);
    }
  });
});