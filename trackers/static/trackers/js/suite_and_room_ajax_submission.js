{
    let unlock_button = $("#unlock_button");
    let room_assignment = $("#suite_and_room");
    let lock_button = $("#lock_button");
    let room_assignment_validation = $("#room_assignment_validation");
    let everything = $("#everything");

    everything.on('click', '#unlock_button', function () {
        unlock_button.prop('hidden', true);
        lock_button.removeAttr('hidden');
        room_assignment.removeAttr('disabled');
        room_assignment.css('background-color', 'white');
        if (!(room_assignment.val() === "")) {
            if (!(room_assignment.val().length < 4 || room_assignment.val().length > 5)) {
                // if final char is a letter, needed for room assignment
                if (room_assignment.val().slice(-1).toLowerCase() !== room_assignment.val().slice(-1).toUpperCase()) {
                    unlock_submission(lock_button, room_assignment_validation, room_assignment);
                } else {
                    lock_submission(lock_button, room_assignment_validation, room_assignment,
                        " Final character must be a letter to fulfill room assignment.")
                }
            } else {
                lock_submission(lock_button, room_assignment_validation, room_assignment,
                    " Room assignment must be 4 or 5 characters long.");
            }
        } else {
            room_assignment_validation.html("");
            lock_button.css('pointer-events', 'none');
            lock_button.removeClass('btn-success');
            lock_button.addClass('btn-secondary');
            room_assignment.css('border-color', '');
        }
    });

    everything.on('click', '#lock_button', function () {
        room_assignment.prop('disabled', true);
        room_assignment.css('background-color', '#e9ecef');
        room_assignment.css('border-color', '');
        room_assignment_validation.html('');
        lock_button.prop('hidden', true);
        unlock_button.removeAttr('hidden');
        let url = lock_button.attr('data-submit-room-assignment');
        let site_url = $(location).attr("href");
        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_room_assignment': room_assignment.val()
            }, success(data) {
                $("#suite_and_room").val(data.room_assignment);
            }
        });
    });

    room_assignment.change(function () {
        // if final char is a letter, needed for room assignment
        if (!(room_assignment.val() === "")) {
            if (!(room_assignment.val().length < 4 || room_assignment.val().length > 5)) {
                if (room_assignment.val().slice(-1).toLowerCase() !== room_assignment.val().slice(-1).toUpperCase()) {
                    unlock_submission(lock_button, room_assignment_validation, room_assignment);
                } else {
                    lock_submission(lock_button, room_assignment_validation, room_assignment,
                        " Final character must be a letter to fulfill room assignment.")
                }
            } else {
                lock_submission(lock_button, room_assignment_validation, room_assignment,
                    " Room assignment must be 4 or 5 characters long.");
            }
        } else {
            room_assignment_validation.html("");
            lock_button.css('pointer-events', 'none');
            lock_button.removeClass('btn-success');
            lock_button.addClass('btn-secondary');
            room_assignment.css('border-color', '');
        }
    });

    function lock_submission(button_locked, assignment_span, assignment, message) {
        assignment_span.html(message);
        button_locked.css('pointer-events', 'none');
        button_locked.removeClass('btn-success');
        button_locked.addClass('btn-secondary');
        assignment.css('border-color', 'red');
    }

    function unlock_submission(button_unlocked, assignment_span, assignment, message = "") {
        assignment_span.html(message);
        button_unlocked.css('pointer-events', 'auto');
        button_unlocked.removeClass('btn-secondary');
        button_unlocked.addClass('btn-success');
        assignment.css('border-color', 'green');
    }

}