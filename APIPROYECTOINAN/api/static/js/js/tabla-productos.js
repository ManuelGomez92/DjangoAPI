// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  // Llamada a la API para obtener datos
  fetch("/products-data/")
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

            // Formatear el campo de precio
            if (key === 'precio') {
              const formattedPrice = formatCurrency(item[key]);
              cell.textContent = formattedPrice;
            } else {
              cell.textContent = item[key];
            }

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
            { data: 'descripcion' },
            { data: 'stock' },
            { data: 'departamento' },
            { data: 'precio' }
          ],
          columnDefs: [
            {
              targets: 4, // Índice de la columna 'precio'
              render: function (data, type, row, meta) {
                // Formatear el valor como moneda
                if (type === 'display') {
                  return formatCurrency(data);
                }
                return data;
              }
            }
          ],
          buttons: ['copy', 'csv', 'excel', 'pdf', 'print']
        });
      } else {
        console.error("Error: El cuerpo de la tabla no se encontró.");
      }
    })
    .catch((error) => console.error("Error:", error));

  // Función para formatear el campo de precio como moneda
  function formatCurrency(value) {
    const formattedValue = new Intl.NumberFormat('es-MX', {
      style: 'currency',
      currency: 'MXN',
      minimumFractionDigits: 2
    }).format(value);

    return formattedValue;
  }
});
