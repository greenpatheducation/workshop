$(document).ready(function () {
  var max_fields = 10;
  var wrapper = $(".container1");
  var wrapper2 = $(".container2");
  var add_button = $(".add_more_trim");
  console.log(wrapper["length"], wrapper2);
  var x = 2;
  var y = 2;
  $(add_button).click(function (e) {
    e.preventDefault();
    if (wrapper["length"] != 0) {
      if (x < max_fields) {
        filename = "file" + x;
        startname = "start" + x;
        endname = "end" + x;
        x++;
        $(wrapper).prepend(
          '<div class="form-span-group"><span>File Name :&nbsp;&nbsp;&nbsp;</span>   <input id="h1" name="' +
            filename +
            '" style="width:18ch;" placeholder="Filename" class="form-controll"> &nbsp;&nbsp;</input><span>Start Time : &nbsp;&nbsp;</span> <input id="h1" name="' +
            startname +
            '" style="width:10ch;" placeholder="hh:mm:ss" class="form-controll"> &nbsp;&nbsp;&nbsp;</input><span>End Time : &nbsp;&nbsp;</span>  <input id="h1" name="' +
            endname +
            '" style="width:10ch;" placeholder="hh:mm:ss" class="form-controll"> &nbsp;&nbsp;</input><a href="#" class="delete">Delete</a></div>'
        ); //add input box
      } else {
        alert("You Reached the limits");
      }
    } else {
      if (y < max_fields) {
        spanname = "span" + y;
        startname = "start" + y;
        endname = "end" + y;
        y++;
        $(wrapper2).prepend(
          '<div class="form-span-group"><span>Start Time : &nbsp;&nbsp;</span> <input id="h1" name="' +
            startname +
            '" style="width:10ch;" placeholder="hh:mm:ss" class="form-controll"> &nbsp;&nbsp;&nbsp;</input><span>End Time : &nbsp;&nbsp;</span>  <input id="h1" name="' +
            endname +
            '" style="width:10ch;" placeholder="hh:mm:ss" class="form-controll"> &nbsp;&nbsp;</input><span>Span : &nbsp;&nbsp;&nbsp;</span><input id="h1" name="' +
            spanname +
            '" style="width:10ch;" placeholder="Span" class="form-controll"> &nbsp;&nbsp;</input><a href="#" class="delete">Delete</a></div>'
        ); //add input box
      } else {
        alert("You Reached the limits");
      }
    }
  });
  if (wrapper["length"] != 0) {
    $(wrapper).on("click", ".delete", function (e) {
      e.preventDefault();
      $(this).parent("div").remove();
      x--;
    });
  } else {
    $(wrapper2).on("click", ".delete", function (e) {
      e.preventDefault();
      $(this).parent("div").remove();
      x--;
    });
  }
});
