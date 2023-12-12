$(document).ready(function() {
    $('#empleados-table').DataTable({
        buttons: ['copy', 'excel', 'pdf'],
        responsive: true
    });
});