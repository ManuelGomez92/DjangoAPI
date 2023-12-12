fetch("/sexos/")
  .then((response) => response.json())
  .then((data) => {
    const select = document.getElementById("sexo");
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id;
      option.text = item.tipogenero; // Puedes cambiar esto dependiendo de tus necesidades
      select.appendChild(option);
    });
  })
  .catch((error) => console.error("Error al obtener datos:", error));