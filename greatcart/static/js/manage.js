$(document).ready(function(){
    // Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Select/Deselect checkboxes
    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function(){
        checkbox.prop('checked', this.checked);
    }).on('click', function(){
        if(!this.checked){
            $("#selectAll").prop("checked", false);
        }
    });
});
