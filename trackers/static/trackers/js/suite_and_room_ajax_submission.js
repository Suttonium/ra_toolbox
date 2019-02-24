{
    let unlock_button = $("#unlock_button");
    let room_assignment = $("#suite_and_room");
    let lock_button = $("#lock_button");
    let room_assignment_validation = $("#room_assignment_validation");

    unlock_button.click(function () {
        room_assignment.removeAttr('disabled');
        room_assignment.css('background-color', 'white');
        unlock_button.animate({
            display: ""
        }, 50, function () {
            lock_button.removeAttr('hidden');
            unlock_button.prop('hidden', true);
            if (room_assignment.val() === "") {
                room_assignment_validation.html("");
                lock_button.css('pointer-events', 'none');
                lock_button.removeClass('btn-success');
                lock_button.addClass('btn-secondary');
                room_assignment.css('border-color', '');
            } else if (room_assignment.val().length < 4 || room_assignment.val().length > 5) {
                room_assignment_validation.html(" Room assignment must be 4 or 5 characters long.");
                lock_button.css('pointer-events', 'none');
                lock_button.removeClass('btn-success');
                lock_button.addClass('btn-secondary');
                room_assignment.css('border-color', 'red');
            } else {
                room_assignment_validation.html("");
                lock_button.css('pointer-events', 'auto');
                lock_button.removeClass('btn-secondary');
                lock_button.addClass('btn-success');
                room_assignment.css('border-color', 'green');
            }
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
        room_assignment.css('border-color', '');
        room_assignment_validation.html('');

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
        });
    });

    room_assignment.change(function () {
        if (room_assignment.val() === "") {
            room_assignment_validation.html("");
            lock_button.css('pointer-events', 'none');
            lock_button.removeClass('btn-success');
            lock_button.addClass('btn-secondary');
            room_assignment.css('border-color', '');
        } else if (room_assignment.val().length < 4 || room_assignment.val().length > 5) {
            room_assignment_validation.html(" Room assignment must be 4 or 5 characters long.");
            lock_button.css('pointer-events', 'none');
            lock_button.removeClass('btn-success');
            lock_button.addClass('btn-secondary');
            room_assignment.css('border-color', 'red');
        } else {
            room_assignment_validation.html("");
            lock_button.css('pointer-events', 'auto');
            lock_button.removeClass('btn-secondary');
            lock_button.addClass('btn-success');
            room_assignment.css('border-color', 'green');
        }
    });
}