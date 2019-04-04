{
    let create_button = $("#create_entry_button");

    create_button.click(function () {
        let entry_div = $("#entry_div");
        let url = entry_div.attr('data-create-entry-url');
        let passdownlog_pk = entry_div.attr('data-passdown-log-pk');
        create_button.removeClass('btn-success');
        create_button.addClass('btn-secondary');
        create_button.css('pointer-events', 'none');
        $.ajax({
            url: url,
            data: {
                'passdownlog_pk': passdownlog_pk
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });
}