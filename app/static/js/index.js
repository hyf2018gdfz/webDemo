setTimeout(function () {
    var flashMessages = document.getElementById('flash_messages');
    if (flashMessages) {
        flashMessages.style.display = 'none';
    }
}, 3000);

function showAlert() {
    alert('logout');
}