$( document ).ready(function() {

    var signup_form = $("#signup");
    var signup_url = "/signup"
    signup_form.submit(function(event) {
        console.log("signup");
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: signup_url,
            data: signup_form.serialize(),
            success: function(data)
            {
                console.log("success");
                console.log(data);
                $("#status").text("Successfully Added");
            },
            error: function(data)
            {
                console.log("error");
                console.log(data);
                $("#status").text("An error occurred");
            }
        });
    });

});
