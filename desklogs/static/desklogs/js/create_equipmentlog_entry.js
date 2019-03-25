{
    let create_button = $("#create_entry_button");

    create_button.click(function () {
        let entry_div = $("#entry_div");
        let url = entry_div.attr('data-create-entry-url');
        let equipmentlog_pk = entry_div.attr('data-equipmentlog-pk');
        create_button.removeClass('btn-success');
        create_button.addClass('btn-secondary');
        create_button.css('pointer-events', 'none');
        $.ajax({
            url: url,
            data: {
                'equipmentlog_pk': equipmentlog_pk
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });
}