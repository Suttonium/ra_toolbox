{
    let current_general_info = $("#current_general_info");


    if (current_general_info) {
        let gen_info = current_general_info.attr("data-current-general-information");
        current_general_info.val(gen_info);
    } else {
        let gen_info = current_general_info.attr("data-current-general-information");
        current_general_info.val(gen_info);
    }


    let update_general_information_button = $("#update_gen_info");
    let submit_general_information_button = $("#submit_gen_info");
    update_general_information_button.click(function () {
        current_general_info.removeAttr('disabled');
        current_general_info.css('background-color', 'white');
        $(this).animate({
            display: ""
        }, 50, function () {
            submit_general_information_button.removeAttr('hidden');
            update_general_information_button.prop('hidden', true);
        });
    });

    submit_general_information_button.click(function () {
        current_general_info.prop('disabled', true);
        current_general_info.css('background-color', '#e9ecef');
        submit_general_information_button.prop('hidden', true);
        $(this).animate({
            display: ""
        }, 50, function () {
            update_general_information_button.removeAttr('hidden');
            submit_general_information_button.prop('hidden', true);
        });

        let url = submit_general_information_button.attr('data-submit-general-information');
        let site_url = $(location).attr("href");

        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_textarea_data': current_general_info.val()
            }, success(data) {
                $("#general_info_div").html(data)
            }
        });
    });
}

