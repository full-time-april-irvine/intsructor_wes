function addCharactersToPage(characters) {
  let htmlStr = `<ul>`;
  for (let character of characters) {
    htmlStr += `<li>${character.name}</li>`;
  }
  htmlStr += `</ul>`;
  $('#characters').html(htmlStr);
}

$(document).ready(function() {
  // $.get("https://swapi.co/api/people", function(data) {
  //   for(let result of data.results) {
  //     console.log(result.name);
  //   }
  // });
  $('#character-search').keyup(function() {
    const searchText = $('#character-search').val();
    $.ajax({
      url: `https://swapi.co/api/people/?search=${searchText}`,
      method: 'GET',
      success: function (data) {
        addCharactersToPage(data.results)
      },
      error: function(err) {
        console.log(err);
      }
    });
  });
});