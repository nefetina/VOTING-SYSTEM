$(document).ready(function() {

    $('#bb').click(function() {
        username = $('#email').val();
        password = $('#pass').val();

        if (username == "comelec" && password == "comtupc") {
            location.href = "comelec.html";
        } else if (username == "student" && password == "student123") {
            location.href = "homepage.html";
        } else {
            window.alert("WRONG DETAILS")
        }
    })

})