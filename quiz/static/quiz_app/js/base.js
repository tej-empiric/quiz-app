
$(document).ready(function() {
    var endTime = $('#timer').data('end-time');

    var timerInterval = setInterval(function() {
        var now = new Date();
        var end = new Date(endTime);
        var remainingTime = end - now;

        var minutes = Math.floor(remainingTime / (1000 * 60));
        var seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        $('#timer').text('Time remaining: ' + minutes + ' minutes ' + seconds + ' seconds');

        if (remainingTime <= 0) {
            clearInterval(timerInterval);
            submitForm();
        }
    }, 1000);

    function submitForm() {
        $.ajax({
            type: 'POST',
            url: $('#quiz-form').attr('action'),
            data: $('#quiz-form').serialize(),
            success: function(response) {
                window.location.href = "/score/"; 
            },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    }
});
