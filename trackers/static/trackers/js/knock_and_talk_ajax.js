if ($("#knock_and_talk_one")) {
    let kat_one = $("#knock_and_talk_one").attr("data-kat-one");
    $("#knock_and_talk_one").val(kat_one);
} else {
    let kat_one_area = $("#knock_and_talk_one");
    let kat_one = kat_one_area.attr("data-kat-one");
    kat_one_area.val(kat_one);
}

if ($("#knock_and_talk_two")) {
    let kat_two = $("#knock_and_talk_two").attr("data-kat-two");
    $("#knock_and_talk_two").val(kat_two);
} else {
    let kat_two_area = $("#knock_and_talk_two");
    let kat_two = kat_two_area.attr("data-kat-two");
    kat_two_area.val(kat_two);
}

if ($("#knock_and_talk_three")) {
    let kat_three = $("#knock_and_talk_three").attr("data-kat-three");
    $("#knock_and_talk_three").val(kat_three);
} else {
    let kat_three_area = $("#knock_and_talk_three");
    let kat_three = kat_three_area.attr("data-kat-three");
    kat_three_area.val(kat_three);
}

$("#kat_one").click(function () {
    $("#knock_and_talk_one").removeAttr('disabled');
    let update_kat_one_button = $("#kat_one");
    update_kat_one_button.hide('fast');
});

$("#submit_button_one").click(function (event) {
    let url = $("#submit_button_one").attr('data-submit-knock-and-talk');
    let site_url = $(location).attr("href");
    $.ajax({
        url: url,
        data: {
            'current_site_url_with_pk': site_url,
            'current_textarea_data': $("#knock_and_talk_one").val(),
            'which_kat': 1
        },
        success(data) {
            $("#kat_one").show('fast');
            $("#knock_and_talk_one").attr('disabled', 'disabled');
            $("#knock_and_talk_one").css('background-color', '#e9ecef');
        }
    });
});

$("#kat_two").click(function () {
    $("#knock_and_talk_two").removeAttr('disabled');
    let update_kat_two_button = $("#kat_two");
    update_kat_two_button.hide('fast');
});

$("#submit_button_two").click(function (event) {
    let url = $("#submit_button_two").attr('data-submit-knock-and-talk');
    let site_url = $(location).attr("href");
    $.ajax({
        url: url,
        data: {
            'current_site_url_with_pk': site_url,
            'current_textarea_data': $("#knock_and_talk_two").val(),
            'which_kat': 2
        },
        success(data) {
            $("#kat_two").show('fast');
            $("#knock_and_talk_two").attr('disabled', 'disabled');
            $("#knock_and_talk_two").css('background-color', '#e9ecef');
        }
    });
});

$("#kat_three").click(function () {
    $("#knock_and_talk_three").removeAttr('disabled');
    let update_kat_three_button = $("#kat_three");
    update_kat_three_button.hide('fast');
});

$("#submit_button_three").click(function (event) {
    let url = $("#submit_button_three").attr('data-submit-knock-and-talk');
    let site_url = $(location).attr("href");
    $.ajax({
        url: url,
        data: {
            'current_site_url_with_pk': site_url,
            'current_textarea_data': $("#knock_and_talk_three").val(),
            'which_kat': 3
        },
        success(data) {
            $("#kat_three").show('fast');
            $("#knock_and_talk_three").attr('disabled', 'disabled');
            $("#knock_and_talk_three").css('background-color', '#e9ecef');
        }
    });
});
