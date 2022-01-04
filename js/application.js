$(document).ready(function() {

    $('#signup').click(function() {
        var fname = $('#firstname').val();
        var sname = $('#surname').val();
        var course = $('#cs').val();
        var age = $('#age').val();
        var position = $('#pos').val();
        var parte = $('#party').val();

        var applications = [fname, sname, course, age, position, parte];

        console.log(applications)
    })




})