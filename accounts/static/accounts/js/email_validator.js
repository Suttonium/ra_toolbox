$("#id_email").change(function () {
    let url = $("#resident_assistant_form").attr("data-email-url");
    let email_input = $(this).val();
    $.ajax({
        url: url,
        data: {
            'email_input': email_input
        },
        success: function (data) {
            if (data === 'True') {
                $("#validate_email").html(" This email has already been registered.");
                $("#id_email").css('border-color', 'red');
            } else if (email_input === "") {
                $("#validate_email").html("");
                $("#id_email").css('border-color', '');
            }
            else {
                $("#validate_email").html("");
                $("#id_email").css('border-color', 'green');
            }
        }
    });
});