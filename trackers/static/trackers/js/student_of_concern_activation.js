{
    let soc_button = $("#student_of_concern");
    let remove_soc_button = $("#remove_soc_button");

    soc_button.click(function () {
        $(this).animate({
            display: ""
        }, 50, function () {
            remove_soc_button.removeAttr('hidden');
            soc_button.prop('hidden', true);
        });

        let url = soc_button.attr('data-soc-decision');
        let site_url = $(location).attr("href");

        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'activate': true
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });


    remove_soc_button.click(function () {
        $(this).animate({
            display: ""
        }, 50, function () {
            soc_button.removeAttr('hidden');
            remove_soc_button.prop('hidden', true);
        });

        let url = soc_button.attr('data-soc-decision');
        let site_url = $(location).attr("href");

        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'deactivate': true
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });
}
