$("#id_date_of_birth").change(function () {
    let dob = $(this).val();
    if (Date.parse(dob) - Date.parse(new Date()) > 0) {
        $("#id_date_of_birth").css('border-color', 'red');
        $("#dob_span").html(" This date is in the future.");
    }
});