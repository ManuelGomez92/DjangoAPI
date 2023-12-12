fetch("/categorias/")
  .then((response) => response.json())
  .then((data) => {
    const select = document.getElementById("idcategoria_id");
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id;
      option.text = item.descripcion; // Puedes cambiar esto dependiendo de tus necesidades
      select.appendChild(option);
    });
  })
  .catch((error) => console.error("Error al obtener datos:", error));
