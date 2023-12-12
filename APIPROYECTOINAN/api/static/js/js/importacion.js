$(document).ready(function() {
    $('#empleados-table').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    } );

    // ESTILOS DE BOTONES //

    $(".dt-button").css("background-color","#10445c");
    $(".dt-button").css("width","100px");
    $(".dt-button").css("height","50px");
    $(".dt-button").css("border-radius","5px");
    $(".dt-button").css("color","white");
    $(".dt-button").css("font-weight","bold");    
} );