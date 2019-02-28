$("#id_student_id").change(function () {
    let url = $("#resident_assistant_form").attr("data-studentid-url");
    let student_id_val = $(this).val();
    let student_id_input = $("#id_student_id");
    if (student_id_val.length === 6 && student_id_val.substring(0, 2) !== "00") {
        student_id_input.val("00" + student_id_val);
        student_id_val = $(this).val();
    }
    if (student_id_val.length === 8) {
        $.ajax({
            url: url,
            data: {
                'student_id_val': student_id_val
            },
            success: function (data) {
                if (data === 'True') {
                    $("#validate_studentid").html(" This Student ID has already been registered.");
                    $("#id_student_id").css('border-color', 'red');
                } else { // data === 'False'
                    $("#validate_studentid").html("");
                    $("#id_student_id").css('border-color', 'green');
                }
            }
        });
    }
    else {
        student_id_input.css('border-color', '');
        $("#validate_studentid").html("");
    }
});