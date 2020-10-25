$(document).ready(function () {
  var selectTarget = $(".selectbox select");

  selectTarget.on("blur", function () {
    $(this).parent().removeClass("focus");
  });

  selectTarget.change(function () {
    var select_name = $(this).children("option:selected").text();

    $(this).siblings("label").text(select_name);
  });

  var shopList = [];
  for (key in floor1) {
    shopList.push(`<li data=${key}>${floor1[key]}</li>`);
  }
  $('.shop-list').html(shopList);
});

$("html").on("change", ".selectbox select", function (e) {
  console.log(e.target.value);
  var shopList = [];
  if (e.target.value == "1층") {
    for (key in floor1) {
      shopList.push(`<li data=${key}>${floor1[key]}</li>`);
    }
  } else if (e.target.value == "2층") {
    for (key in floor2) {
      shopList.push(`<li data=${key}>${floor2[key]}</li>`);
    }
  } else if (e.target.value == "3층") {
    for (key in floor3) {
      shopList.push(`<li data=${key}>${floor3[key]}</li>`);
    }
  }
  $('.shop-list').html(shopList);

});

$("html").on("click", ".shop-list li", function (e) {
  let data = $(e.target).attr('data');
  let text = $(e.target).text();
  
  $('#'+modalFlag+'Code').val(data);
  $('#'+modalFlag).val(text);
  
  modal.style.display = 'none';
});

$("html").on("click", ".exchange-btn .fa", function (e) {
  console.log(e.target);

  let startCode = $('#startCode');
  let startName = $('#start');
  let endCode = $('#endCode');
  let endName = $('#end');

  let tempCode = '';
  let tempName = '';
  tempCode = startCode.val()
  tempName = startName.val();

  startCode.val(endCode.val());
  startName.val(endName.val());

  endCode.val(tempCode);
  endName.val(tempName);
});

