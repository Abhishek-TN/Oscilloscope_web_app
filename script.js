// JavaScript code to show modal when HORIZONTAL button is clicked
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#horizontal-btn").addEventListener("click", function() {
        var myModal = new bootstrap.Modal(document.getElementById('waveModal'), {
            keyboard: false
        });
        myModal.show();
    });
});
