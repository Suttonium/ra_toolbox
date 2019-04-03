{
    let create_button = $("#create_entry_button");

    create_button.click(function () {
        let entry_div = $("#entry_div");
        let url = entry_div.attr('data-create-lockout-code');
        let lockoutlog_entry_pk = entry_div.attr('data-entry-pk');
        $.ajax({
            url: url,
            data: {
                'lockoutlog_entry_pk': lockoutlog_entry_pk
            }, success(data) {
                $("#everything").html(data);
            }
        })
    });
}