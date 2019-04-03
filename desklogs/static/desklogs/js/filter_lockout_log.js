{
    let filter_search = $("#filter_search");
    let search_button = $("#search_button");
    search_button.click(function () {

        if (filter_search.val().length === 0) {
            filter_search.css('border-color', 'red');
        } else {
            let url = search_button.attr('data-filter-lockoutlog-entries');
            let lockoutlog_pk = $("#entry_div").attr('data-lockout-pk');
            $.ajax({
                url: url,
                data: {
                    'lockoutlog_pk': lockoutlog_pk,
                    'query': filter_search.val(),
                }, success(data) {
                    $("#everything").html(data);
                }
            })
        }
    });
}