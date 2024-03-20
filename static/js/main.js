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
                $('#winnerTitle').show();
                $('#winnerTeam').text(response.winner);
            }
        });
    });
});