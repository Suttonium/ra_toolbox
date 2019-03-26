{
    let checkin = $('.checkin');
    let entry_div = $("#entry_div");
    let url = entry_div.attr('data-checkin-entry-url');

    checkin.click(function () {
        let pk = checkin.attr('data-obj-pk');
        let equipmentlog_pk = entry_div.attr('data-equipmentlog-pk');
        let closest_final_condition = checkin.closest('tr').find('.final_condition').val();


        $.ajax({
            url: url,
            data: {
                'current_entry_being_updated_pk': pk,
                'equipmentlog_pk': equipmentlog_pk,
                'final_condition': closest_final_condition
            }, success(data) {
                $("#everything").html(data)
            }
        })
    });
}