if ($("#current_general_info")) {
    let gen_info = $("#current_general_info").attr("data-current-general-information");
    $("#current_general_info").val(gen_info);
} else {
    let gen_info_area = $("#current_general_info");
    let gen_info = gen_info_area.attr("data-current-general-information");
    gen_info_area.val(gen_info);
}

