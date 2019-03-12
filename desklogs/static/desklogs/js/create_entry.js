{
    let create_button = $("#create_entry_button");

    create_button.click(function () {
        let entry_div = $("#entry_div");
        let url = entry_div.attr('data-create-entry-url');
        let guestlog_pk = entry_div.attr('data-guestlog-pk');
        $.ajax({
            url: url,
            data: {
                'guestlog_pk': guestlog_pk
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });
}