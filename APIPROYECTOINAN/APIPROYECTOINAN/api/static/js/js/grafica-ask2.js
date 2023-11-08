// Obtén el contexto del lienzo
var ctx = document.getElementById('anillo2').getContext('2d');

// Datos para el gráfico
var data = {
    labels: ['Material de escritura', 'Papelería y suministros de oficina', 'Material de arte y manualidades', 'Material escolar'],
    datasets: [{
        data: [5, 2, 1, 1], // Valores para cada sección
        backgroundColor: ['rgba(0, 114, 240)',
        'rgba(0, 182, 203)',
        'rgba(241, 0, 150)',        
        'rgba(246, 109, 0)'], // Colores de las secciones
    }]
};

// Opciones del gráfico
var options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        datalabels: {
            color: 'white', // Color del texto
            anchor: 'end', // Posición del texto (puedes ajustarlo según tus preferencias)
            align: 'end',  // Alineación del texto (puedes ajustarlo según tus preferencias)
            font: {
                size: 14  // Tamaño de la fuente del texto
            }
        }
    }
};

// Crea el gráfico de anillo
var myRingChart = new Chart(ctx, {
    type: 'doughnut', // Tipo de gráfico de anillo
    data: data,
    options: options
});