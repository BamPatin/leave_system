document.addEventListener('DOMContentLoaded', function() {
    var alerts = document.getElementsByClassName('alert');
    Array.prototype.forEach.call(alerts, function(alert) {
    setTimeout(function() {
        alert.style.display = 'none';
    }, 5000);
    });
});


document.getElementById('cancelAlert').addEventListener('click', function () {
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Something went wrong!',
        footer: '<a href>Why do I have this issue?</a>'
    })
});
