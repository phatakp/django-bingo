$(document).ready(function () {
  $('#player-table td').click(function () {
    var num = $(this)[0].innerText;
    var player = $('#username').text();


    if (($(this)[0].classList.contains('player')) & (num != '')) {
      $(this).toggleClass('crossed');
      if ($(this)[0].classList.contains('crossed')) {
        save_player_num(player, num, 'add');
      } else {
        save_player_num(player, num, 'delete');
      }
    }
  });
});

function getRandomInt(max) {
  return Math.floor(Math.random() * max) + 1;
}

$('#random_btn').on('click', function () {
  var done = "";
  while (done == "") {
    var val = getRandomInt(90);

    $('#random-table td').each(function () {
      if ($(this).attr('id') == val) {
        if (!$(this)[0].classList.contains('.crossed')) {
          $(this).toggleClass('crossed');
          $('#random').val(val);
          done = 'Done';
          save_number(val);
        }
      }
    })
  }
});

function save_number(num) {
  var token = $('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    type: "POST",
    headers: {
      'X-CSRFToken': token
    },
    url: '/num/create/',
    data: {
      'num': num
    },
    success: function (data) {

    },
    error: function (error) {
      console.log(error);
    }
  })

}

function save_player_num(player, num, action) {
  var token = $('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    type: "POST",
    headers: {
      'X-CSRFToken': token
    },
    url: '/num/create/',
    data: {
      'player': player,
      'num': num,
      'action': action,
    },
    success: function (data) {

    },
    error: function (error) {
      console.log(error);
    }
  })

}