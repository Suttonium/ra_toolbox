{
    let catch_up_one = $("#cu_one");
    let update_catch_up_one = $("#update_button_one");
    let submit_catch_up_one = $("#submit_button_one");

    if (catch_up_one) {
        let cu_one = catch_up_one.attr("data-cu-one");
        catch_up_one.val(cu_one);
    } else {
        let cu_one = catch_up_one.attr("data-cu-one");
        catch_up_one.val(cu_one);
    }

    update_catch_up_one.click(function () {
        catch_up_one.removeAttr('disabled');
        catch_up_one.css('background-color', 'white');
        $(this).animate({
            display: ''
        }, 50, function () {
            submit_catch_up_one.removeAttr('hidden');
            update_catch_up_one.prop('hidden', true);
        });
    });

    submit_catch_up_one.click(function () {
        catch_up_one.prop('disabled', true);
        catch_up_one.css('background-color', '#e9ecef');
        $(this).animate({
            display: ''
        }, 50, function () {
            update_catch_up_one.removeAttr('hidden');
            submit_catch_up_one.prop('hidden', true);
        });
        let url = submit_catch_up_one.attr('data-submit-catch-up');
        let site_url = $(location).attr("href");

        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_textarea_data': catch_up_one.val(),
            }, success(data) {
                catch_up_one.val(data.catch_up_one)
            }
        })
    });
}