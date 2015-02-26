$( document ).ready(function() {
    var request_form = $("#request");
    var request_url = "/request_submit"
    request_form.submit(function(event) {
        console.log("Sending request...");
        event.preventDefault();
        $("#status").text("Submitting Request...");
        $.ajax({
            type: "POST",
            url: request_url,
            data: request_form.serialize(),
            success: function(data)
            {
                console.log("success");
                console.log(data);
                $("#status").text(data);
                $("#status").css("color", "green");
            },
            error: function(data)
            {
                console.log("error");
                console.log(data);
                $("#status").text("An error occurred...sorry");
                $("#status").css("color", "red");
            }
        });
    });

});
