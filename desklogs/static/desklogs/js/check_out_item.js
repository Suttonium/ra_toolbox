{
    let checkout = $(".checkout");
    let entry_div = $("#entry_div");
    let url = entry_div.attr('data-update-entry-url');

    checkout.click(function () {
        let closest_item_host = checkout.closest('tr').find('.item_host').val();
        let closest_initial_condition = checkout.closest('tr').find('.initial_item_condition').val();
        let closest_item = checkout.closest('tr').find('.item').val();

        if (closest_item_host.length === 0 || closest_item.length === 0) {
            checkout.closest('tr').find('.item_host').css('border-color', 'red');
            checkout.closest('tr').find('.item').css('border-color', 'red');
        } else {
            checkout.closest('tr').find('.item_host').css('border-color', 'green');
            checkout.closest('tr').find('.item').css('border-color', 'green');

            let pk = checkout.attr('data-obj-pk');
            let equipmentlog_pk = entry_div.attr('data-equipmentlog-pk');

            $.ajax({
                url: url,
                data: {
                    'equipmentlog_pk': equipmentlog_pk,
                    'item_host': closest_item_host,
                    'initial_condition': closest_initial_condition,
                    'item': closest_item,
                    'current_entry_being_updated_pk': pk
                }, success(data) {
                    $("#everything").html(data);
                }
            })
        }
    });
}