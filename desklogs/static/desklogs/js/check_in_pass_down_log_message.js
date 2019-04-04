{
    let passdown = $(".passdown");
    let entry_div = $("#entry_div");
    let url = entry_div.attr('data-update-entry-url');

    passdown.click(function () {
        let closest_message = $(this).closest('tr').find('.message').val();
        let closest_initials = $(this).closest('tr').find('.initials').val();

        if (closest_message.length === 0 || closest_initials.length === 0) {
            $(this).closest('tr').find('.message').css('border-color', 'red');
            $(this).closest('tr').find('.initials').css('border-color', 'red');
        } else {
            $(this).closest('tr').find('.message').css('border-color', 'green');
            $(this).closest('tr').find('.initials').css('border-color', 'green');
            let pk = $(this).attr('data-obj-pk');
            let passdownlog_pk = entry_div.attr('data-passdown-log-pk');

            $.ajax({
                url: url,
                data: {
                    'current_entry_being_updated_pk': pk,
                    'message': closest_message,
                    'initials': closest_initials,
                    'passdownlog_pk': passdownlog_pk
                }, success(data) {
                    $("#everything").html(data)
                }
            })
        }
    });
}