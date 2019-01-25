$("#id_residence_halls").change(function () {
    $("#id_residence_halls").css('border-color', 'green');
    let url = $("#resident_assistant_form").attr("data-hallways-url");
    let residence_hall_id = $(this).val();
    $.ajax({
        url: url,
        data: {
            'residence_hall': residence_hall_id
        },
        success: function (data) {
            $("#id_hallway_selection").html(data);
        }
    });
});

$("#id_hallway_selection").change(function () {
    $("#id_hallway_selection").css('border-color', 'green');
});