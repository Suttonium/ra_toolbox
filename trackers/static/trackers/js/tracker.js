setTimeout(function () {
    $("#information_for_tracker").css('visibility', 'visible')
}, 500);

$(document).ready(function () {
    $('.list-group-item').click(function (e) {
        e.preventDefault();
        $('.list-group-item').removeClass('active');
        $(this).addClass('active');
    });
});

$(document).ready(function () {
    gen_info_func();
    $("#general_information_list_item").click(function () {
        gen_info_func();
    })
});


function gen_info_func() {
    $("#general_information_list_item").addClass('active');
    let decision_list = $("#decision_list");
    let url = decision_list.attr("data-general-information-url");
    let pk = decision_list.attr("data-obj-pk");
    let data_container = $("#data_location");
    data_container.empty();
    $.ajax({
        url: url,
        data: {
            'pk_being_sent': pk
        },
        success(data) {
            data_container.html(data);
        }
    });
}


function kat_func() {
    let decision_list = $("#decision_list");
    let url = decision_list.attr("data-knock-and-talk-url");
    let pk = decision_list.attr("data-obj-pk");
    let data_container = $("#data_location");
    data_container.empty();
    $.ajax({
        url: url,
        data: {
            'pk_being_sent': pk
        },
        success(data) {
            data_container.html(data)
        }
    });
}


