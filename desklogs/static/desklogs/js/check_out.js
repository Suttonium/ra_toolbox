{
    let checkout = $('.checkout');
    let entry_div = $("#entry_div");
    let url = entry_div.attr('data-checkout-entry-url');

    checkout.click(function () {
        let pk = checkout.attr('data-obj-pk');
        let guestlog_pk = entry_div.attr('data-guestlog-pk');

        $.ajax({
            url: url,
            data: {
                'current_entry_being_updated_pk': pk,
                'guestlog_pk': guestlog_pk
            }, success(data) {
                $('#everything').html(data);
            }
        })
    });
}
