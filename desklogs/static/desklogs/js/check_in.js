{
    let checkin = $(".checkin");
    let entry_div = $("#entry_div");
    let url = entry_div.attr('data-update-entry-url');

    checkin.click(function () {
        let closest_host_name = $(this).closest('tr').find('.host_name').val();
        let closest_guest_name = $(this).closest('tr').find('.guest_name').val();

        if (closest_host_name.length === 0 || closest_guest_name.length === 0) {
            $(this).closest('tr').find('.host_name').css('border-color', 'red');
            $(this).closest('tr').find('.guest_name').css('border-color', 'red');
        } else {
            $(this).closest('tr').find('.host_name').css('border-color', 'green');
            $(this).closest('tr').find('.guest_name').css('border-color', 'green');
            let pk = $(this).attr('data-obj-pk');
            let guestlog_pk = entry_div.attr('data-guestlog-pk');

            $.ajax({
                url: url,
                data: {
                    'current_entry_being_updated_pk': pk,
                    'host_name': closest_host_name,
                    'guest_name': closest_guest_name,
                    'guestlog_pk': guestlog_pk
                }, success(data) {
                    $("#everything").html(data)
                }
            })
        }
    });
}