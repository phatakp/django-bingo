$(document).ready(function() {
  $('table td').click(function() {
    if ($(this)[0].innerText != '') {
      $(this).toggleClass('crossed');
    }
  });
});
