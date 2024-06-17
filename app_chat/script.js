document.addEventListener('DOMContentLoaded', function () {
    fetch('/mensajes/')
        .then(response => response.json())
        .then(data => {
            const mensajesContainer = document.getElementById('mensajes-container');
            data.mensajes.forEach(mensaje => {
                const mensajeElement = document.createElement('p');

                // Crear elementos para el nombre y la carrera
                const nombreElement = document.createElement('h1'); // Usamos <h1> aquí
                nombreElement.textContent = mensaje.nombre_completo;

                const carreraElement = document.createElement('span');
                carreraElement.textContent = mensaje.carrera;
                carreraElement.style.color = 'blue';

                // Agregar los elementos al mensajeElement
                mensajeElement.textContent = mensaje.txt_mensaje + ' ';
                mensajeElement.appendChild(nombreElement);
                mensajeElement.appendChild(document.createElement('br'));
                mensajeElement.appendChild(carreraElement);

                mensajesContainer.appendChild(mensajeElement);
            });
        });
});

