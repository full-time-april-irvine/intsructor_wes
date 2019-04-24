// $('h1').click(function() {
//   console.log('clicked');
// })

// $.ajax({
//   url: '/partial',
//   method: 'GET',
//   success: function(data) {
//     setTimeout(function() {
//       $('#insert-here').html(data);
//     }, 3000)
//   }
// })

$.ajax({
  url: '/json',
  method: 'GET',
  success: function(data) {
    data = JSON.parse(data);
    console.log(data.favorite_food);
  }
})