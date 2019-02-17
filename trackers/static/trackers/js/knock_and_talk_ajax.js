{
    let knock_and_talk_one = $("#knock_and_talk_one");
    let update_kat_one_button = $("#kat_one");
    let submit_button_one = $("#submit_button_one");


    if (knock_and_talk_one) {
        let kat_one = knock_and_talk_one.attr("data-kat-one");
        knock_and_talk_one.val(kat_one);
    } else {
        let kat_one = knock_and_talk_one.attr("data-kat-one");
        knock_and_talk_one.val(kat_one);
    }

    update_kat_one_button.click(function () {
        knock_and_talk_one.removeAttr('disabled');
        knock_and_talk_one.css('background-color', 'white');
        $(this).animate({
            display: ""
        }, 50, function () {
            update_kat_one_button.fadeOut();
        });
    });

    submit_button_one.click(function (event) {
        let url = submit_button_one.attr('data-submit-knock-and-talk');
        let site_url = $(location).attr("href");
        submit_button_one.animate({
            display: ""
        }, 100, function () {
            update_kat_one_button.fadeIn();
        });
        knock_and_talk_one.attr('disabled', 'disabled');
        knock_and_talk_one.css('background-color', '#e9ecef');
        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_textarea_data': knock_and_talk_one.val(),
                'which_kat': 1
            },
            success(data) {
                $('#everything').html(data)
            }
        });
    });


    let knock_and_talk_two = $("#knock_and_talk_two");
    let update_kat_two_button = $("#kat_two");
    let submit_button_two = $("#submit_button_two");

    if (knock_and_talk_two) {
        let kat_two = knock_and_talk_two.attr("data-kat-two");
        knock_and_talk_two.val(kat_two);
    } else {
        let kat_two = knock_and_talk_two.attr("data-kat-two");
        knock_and_talk_two.val(kat_two);
    }

    update_kat_two_button.click(function () {
        knock_and_talk_two.removeAttr('disabled');
        knock_and_talk_two.css('background-color', 'white');
        $(this).animate({
            display: ""
        }, 50, function () {
            update_kat_two_button.fadeOut();
        });
    });


    submit_button_two.click(function (event) {
        let url = submit_button_two.attr('data-submit-knock-and-talk');
        let site_url = $(location).attr("href");
        submit_button_two.animate({
            display: ""
        }, 50, function () {
            update_kat_two_button.fadeIn();
        });
        knock_and_talk_two.attr('disabled', 'disabled');
        knock_and_talk_two.css('background-color', '#e9ecef');
        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_textarea_data': knock_and_talk_two.val(),
                'which_kat': 2
            },
            success(data) {
                $('#everything').html(data)
            }
        });
    });

    let knock_and_talk_three = $("#knock_and_talk_three");
    let update_kat_three_button = $("#kat_three");
    let submit_button_three = $("#submit_button_three");

    if (knock_and_talk_three) {
        let kat_three = knock_and_talk_three.attr("data-kat-three");
        knock_and_talk_three.val(kat_three);
    } else {
        let kat_three = knock_and_talk_three.attr("data-kat-three");
        knock_and_talk_three.val(kat_three);
    }

    update_kat_three_button.click(function () {
        knock_and_talk_three.removeAttr('disabled');
        knock_and_talk_three.css('background-color', 'white');
        $(this).animate({
            display: ""
        }, 100, function () {
            update_kat_three_button.fadeOut();
        });
    });


    submit_button_three.click(function (event) {
        let url = submit_button_three.attr('data-submit-knock-and-talk');
        let site_url = $(location).attr("href");
        submit_button_three.animate({
            display: ""
        }, 100, function () {
            update_kat_three_button.fadeIn();
        });
        knock_and_talk_three.attr('disabled', 'disabled');
        knock_and_talk_three.css('background-color', '#e9ecef');
        $.ajax({
            url: url,
            data: {
                'current_site_url_with_pk': site_url,
                'current_textarea_data': knock_and_talk_three.val(),
                'which_kat': 3
            },
            success(data) {
                $('#everything').html(data)
            }
        });
    });
}
