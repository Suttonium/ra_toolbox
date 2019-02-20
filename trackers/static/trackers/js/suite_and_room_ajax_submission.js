{
    let unlock_button = $("#unlock_button");
    let room_assignment = $("#suite_and_room");
    let lock_button = $("#lock_button");

    unlock_button.click(function () {
        room_assignment.removeAttr('disabled');
        room_assignment.css('background-color', 'white');
        unlock_button.animate({
            display: ""
        }, 50, function () {
            lock_button.removeAttr('hidden');
            unlock_button.prop('hidden', true);
        });
    });

    lock_button.click(function () {
        room_assignment.prop('disabled', true);
        room_assignment.css('background-color', '#e9ecef');
        lock_button.animate({
            display: ""
        }, 50, function () {
            unlock_button.removeAttr('hidden');
            lock_button.prop('hidden', true);
        });

        let url = lock_button.attr('data-submit-room-assignment');
        let site_url = $(location).attr("href");
        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_room_assignment': room_assignment.val()
            }, success(data) {
                $("#everything").html(data)
            }
        })
    })
}