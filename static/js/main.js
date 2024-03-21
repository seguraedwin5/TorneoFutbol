$(document).ready(function() {
    $('#matchForm').submit(function(e) {
        e.preventDefault();
        var resultados = [];
        $('select[name="winner"]').each(function() {
            resultados.push($(this).val());
        });
        $.ajax({
            url: '/get_winner',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({resultados: resultados}),
            success: function(response) {
                Swal.fire({
                    background: '#000',
                    title: '<h1 style="color:white">Equipo Ganador<h1>',
                    text: response.winner,
                    icon: 'success',
                    confirmButtonText: 'Aceptar',
                    color : '#fff'
                  })
                
            }
        });
    });
});


function mostrardialogo(){

    Swal.fire({
        background: '#000',
        title: 'Nuevo Equipo',
        text: 'digite el nombre del nuevo equipo',
        icon: 'info',
        confirmButtonText: 'Aceptar',
        color : '#fff',
        input : 'text',
        
      }).then((result) => {
        if(result.isConfirmed){
            fetch(`/add_equipo/${result.value}`,{
                method : 'POST',
                body : {},
                headers : {
                    'Content-Type' : 'application/json'
                }
            }).then(response => response.json()).then(data => {
                Swal.fire({
                    background: '#000',
                    title: '<h1 style="color:white">Equipo Agregado<h1>',
                    text: data.mensaje,
                    icon: 'success',
                    confirmButtonText: 'Aceptar',
                    color : '#fff'
                  }).then(result => {
                    if (result.isConfirmed){
                        window.location.href ="/";
                    }
                  })
            });
        }
      })
}