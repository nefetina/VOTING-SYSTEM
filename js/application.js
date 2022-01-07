$(document).ready(function() {

    $('#pindot').click(function() {
        var fname = $('#firstname').val();
        var sname = $('#surname').val();
        var course = $('#cs').val();
        var age = $('#age').val();
        var position = $('#pos').val();
        var parte = $('#party').val();
        var desc = $('#desc');

        //var applications = "<tr><td>" + fname + "</td><td>" + surname + "</td><td>" + course + "</td><td>" + age + "</td><td>" + position + "</td><td>" +
        //position + "</td><td>" + parte + "</td><td>";

        //$('#attendanceTable').append(applications);

        console.log(fname);
        console.log(sname);
        console.log(course);
        console.log(age);
        console.log(position);
        console.log(parte);
        console.log(desc);
        //console.log(applications);

    })

})