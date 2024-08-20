var API_ENDPOINT = "https://fwicm4kq8b.execute-api.us-east-1.amazonaws.com/prod/students";

document.getElementById("savestudent").onclick = function() {
    var inputData = {
        "studentid": $('#studentid').val(),
        "name": $('#name').val(),
        "class": $('#class').val(),
        "age": $('#age').val()
    };
    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data: JSON.stringify(inputData),
        contentType: 'application/json; charset=utf-8',
        success: function(response) {
            alert("Student data saved successfully!");
        },
        error: function() {
            alert("Error saving student data.");
        }
    });
}

document.getElementById("getstudents").onclick = function() {
    $.ajax({
        url: API_ENDPOINT,
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        success: function(response) {
            $('#studentTable tr').slice(1).remove();
            $.each(response, function(i, data) {
                $("#studentTable").append("<tr> \
                    <td>" + data['studentid'] + "</td> \
                    <td>" + data['name'] + "</td> \
                    <td>" + data['class'] + "</td> \
                    <td>" + data['age'] + "</td> \
                    </tr>");
            });
        },
        error: function() {
            alert("Error retrieving student data.");
        }
    });
}
