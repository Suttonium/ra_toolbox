$("#id_password_confirmation").change(function () {
    let confirmed_password = $(this);
    let password = $("#id_password");
    let password_span = $("#validate_password");
    let password_confirmation_span = $("#validate_password_confirmation");
    if (confirmed_password.val() === password.val() && (password.val() !== "" && confirmed_password.val() !== "")) {
        password.css('border-color', 'green');
        password_span.html("");
        confirmed_password.css('border-color', 'green');
        password_confirmation_span.html("");
    } else if (password.val() === "" && confirmed_password.val() === "") {
        password.css('border-color', '');
        password_span.html("");
        confirmed_password.css('border-color', '');
        password_confirmation_span.html("");
    } else {
        password.css('border-color', 'red');
        password_span.html(' Passwords do not match.');
        confirmed_password.css('border-color', 'red');
        password_confirmation_span.html(' Passwords do not match.');
    }

});

$("#id_password").change(function () {
    let password = $(this);
    let confirmed_password = $("#id_password_confirmation");
    let password_span = $("#validate_password");
    let password_confirmation_span = $("#validate_password_confirmation");

    if ((password.val() === confirmed_password.val()) && (password.val() !== "" && confirmed_password.val() !== "")) {
        password.css('border-color', 'green');
        password_span.html("");
        confirmed_password.css('border-color', 'green');
        password_confirmation_span.html("");
    }
    else if (password.val() === "" && confirmed_password.val() === "") {
        password.css('border-color', '');
        password_span.html("");
        confirmed_password.css('border-color', '');
        password_confirmation_span.html("");
    }
    else {
        password.css('border-color', 'red');
        password_span.html(' Passwords do not match.');
        confirmed_password.css('border-color', 'red');
        password_confirmation_span.html(' Passwords do not match.');
    }
});