// Obtén el contexto del lienzo
var ctx = document.getElementById('anillo6').getContext('2d');

// Datos para el gráfico
var data = {
    labels: ['Computadora de escritorio','Portatil','Tableta','Smartphone'],
    datasets: [{
        data: [3, 4, 0, 2], // Valores para cada sección
        backgroundColor: ['rgba(255, 168, 0)',
        'rgba(0, 114, 240)',
        'rgba(246, 109, 0)',
        'rgba(0, 182, 203)'], // Colores de las secciones
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