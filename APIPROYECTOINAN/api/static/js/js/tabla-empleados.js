// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  // Llamada a la API para obtener datos
  fetch("/empleados-data/")
    .then((response) => response.json())
    .then((data) => {
      // Verificar que los datos se han recibido correctamente
      console.log("Datos recibidos:", data);

      // Actualizar el cuerpo de la tabla con los datos recibidos
      const tableBody = document.querySelector("#empleados-table tbody");

      if (tableBody) {
        // Limpiar contenido existente
        console.log("Antes de limpiar:", tableBody.innerHTML); // Depuración
        tableBody.innerHTML = "";
        console.log("Después de limpiar:", tableBody.innerHTML); // Depuración

        // Añadir filas de datos al cuerpo de la tabla
        data.forEach((item) => {
          const row = document.createElement("tr");

          // Añadir celdas de datos
          Object.keys(item).forEach((key) => {
            const cell = document.createElement("td");
            cell.textContent = item[key];
            row.appendChild(cell);
          });

          tableBody.appendChild(row);
        });

        // Destruir la instancia DataTable existente si ya está inicializada
        if ($.fn.DataTable.isDataTable("#empleados-table")) {
          $("#empleados-table").DataTable().destroy();
        }

        // Inicializar DataTable con la nueva configuración y datos
        $("#empleados-table").DataTable({
          data: data,
          columns: [
            { data: 'id' },
            { data: 'nombre' },
            { data: 'paterno' },
            { data: 'materno' },
            { data: 'telefono' },
            { data: 'fecha_ingreso' },
            { data: 'sexo' },
            { data: 'departamento' }
          ],
          // Otras configuraciones 
          buttons: ['copy', 'excel', 'pdf', 'print']
        });
      } else {
        console.error("Error: El cuerpo de la tabla no se encontró.");
      }
    })
    .catch((error) => console.error("Error:", error));
});