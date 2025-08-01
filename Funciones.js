 const AccederSubtitulo = document.querySelector(".subtitulo");

function Changecolor(){
 AccederSubtitulo.style.color = "#2c3e50";
}

function sumar(){
    let numero1 = document.getElementById("numero1").value;
    let numero2 = document.getElementById("numero2").value;

    let resultado = parseInt(numero1)+parseInt(numero2)
    alert(resultado);

    const SeccionRespuesta = document.getElementById("respuesta")
    SeccionRespuesta.innerHTML = resultado;
}