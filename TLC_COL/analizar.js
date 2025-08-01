// analizar.js
document.addEventListener("DOMContentLoaded", () => {
    const busquedaInput = document.getElementById("busqueda");
    const resultadoDiv = document.getElementById("resultado");
    const infoDiv = document.getElementById("info");

    let datos = [];

    // Cargar los datos desde el servidor Flask
    fetch('http://127.0.0.1:5000/datos')
        .then(response => response.json())
        .then(jsonData => {
             datos = jsonData;
             busquedaInput.disabled = false; // <-- aquí se habilita
            console.log("Datos cargados correctamente.");

        })
        .catch(error => {
            console.error('Error al cargar los datos:', error);
        });

    busquedaInput.addEventListener("input", () => {
        const valor = busquedaInput.value;
        const soloDigitos = valor.replace(/\D/g, ""); // Solo números

        if (soloDigitos.length >= 4) {
            // Buscar por la columna "codigos"
            const resultado = datos.find(item => String(item.codigos) === soloDigitos);

            if (resultado) {
                resultadoDiv.style.display = "block";
                let html = "";
                for (let key in resultado) {
                    html += `<p><strong>${key}:</strong> ${resultado[key]}</p>`;
                }
                infoDiv.innerHTML = html;
            } else {
                resultadoDiv.style.display = "block";
                infoDiv.innerHTML = `<p style="color:red;">Código no encontrado.</p>`;
            }
        } else {
            resultadoDiv.style.display = "none";
            infoDiv.innerHTML = "";
        }
    });
});
