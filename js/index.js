$(document).ready(function() {

    $('#bb').click(function() {
        username = $('#email').val();
        password = $('#pass').val();

        if (username == "admin@gsfe.tupcavite.edu.ph" && password == "admin123") {
            location.href = "homepage.html";
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Username and/or Password is incorrect',
                text: 'Something went wrong!',
                confirmButtonColor: '#A42222',
                confirmButtonText: 'Okay'
            });
        }
    })

})