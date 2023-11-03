// Obtén el contexto del lienzo
var ctx = document.getElementById('anillo').getContext('2d');

// Datos para el gráfico
var data = {
    labels: ['Diariamente', 'Semanalmente', 'Mensualmente', 'Ocasionalmente', 'Nunca'],
    datasets: [{
        data: [1, 2, 2, 2, 2], // Valores para cada sección
        backgroundColor: ['rgba(255, 168, 0)',
        'rgba(0, 114, 240)',
        'rgba(246, 109, 0)',
        'rgba(241, 0, 150)',
        'rgba(0, 182, 203)'], 
        // Colores de las secciones
    }]
};

// Opciones del gráfico
var options = {
    responsive: true,
    maintainAspectRatio: false,
    annotation: {
        annotations: [
            {
                type: 'text',
                text: '30%',
                fontSize: 20,
                x: 50,
                y: 50,
                backgroundColor: 'transparent',
            },
            {
                type: 'text',
                text: '40%',
                fontSize: 20,
                x: 150,
                y: 150,
                backgroundColor: 'transparent'
            },
            {
                type: 'text',
                text: '30%',
                fontSize: 20,
                x: 250,
                y: 250,
                backgroundColor: 'transparent'
            },
            {
                type: 'text',
                text: '40%',
                fontSize: 20,
                x: 150,
                y: 150,
                backgroundColor: 'transparent'
            },
            {
                type: 'text',
                text: '30%',
                fontSize: 20,
                x: 250,
                y: 250,
                backgroundColor: 'transparent'
            }
        ]
    }
};

// Crea el gráfico de anillo
var myRingChart = new Chart(ctx, {
    type: 'doughnut', // Tipo de gráfico de anillo
    data: data,
    options: options
});