$(document).ready(function(){
  console.log(' ready');

  $("form").on("submit", function(){
    console.log("The form has been submitted");

    var valueOne = $('input[name="number-one"]').val()
    var valueTwo = $('input[name="number-two"]').val()
    console.log(valueOne,valueTwo);

    $.ajax({
      type: "POST",
      url: "/",
      data: {first: valueOne, second: valueTwo},
      success: function(results){
        console.log(results);
        $("#results").html(results.total)
        $("input").val("")
      },
      error: function(error){
        console.log(error);
      }
    });
  });
}); //this is the end