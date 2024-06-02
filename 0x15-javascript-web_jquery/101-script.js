$(function () {
  const list = $('ul.my_list');

  $('div#add_item').bind('click', function () {
    list.append('<li>Item</li>');
  });

  $('div#remove_item').bind('click', function () {
    list.find(':last-child').remove();
  });

  $('div#clear_list').bind('click', function () {
    list.empty();
  });
});
