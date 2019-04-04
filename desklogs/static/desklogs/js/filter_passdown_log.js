{
    let filter_search = $("#filter_search");
    let search_button = $("#search_button");
    search_button.click(function () {

        if (filter_search.val().length === 0) {
            filter_search.css('border-color', 'red');
        } else {
            let url = search_button.attr('data-filter-lockoutlog-entries');
            let passdownlog_pk = $("#entry_div").attr('data-passdown-log-pk');
            $.ajax({
                url: url,
                data: {
                    'passdown_log': passdownlog_pk,
                    'query': filter_search.val(),
                }, success(data) {
                    $("#everything").html(data);
                }
            })
        }
    });
}