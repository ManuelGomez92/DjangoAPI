// Obtén el contexto del lienzo
var ctx = document.getElementById('anillo11').getContext('2d');

// Datos para el gráfico
var data = {
    labels: ['SI','NO'],
    datasets: [{
        data: [9, 0], // Valores para cada sección
        backgroundColor: ['rgba(0, 114, 240)',
        'rgba(241, 0, 150)'], // Colores de las secciones
    }]
};

// Opciones del gráfico
var options = {
    responsive: true,
    maintainAspectRatio: false
};

// Crea el gráfico de anillo
var myRingChart = new Chart(ctx, {
    type: 'doughnut', // Tipo de gráfico de anillo
    data: data,
    options: options
});