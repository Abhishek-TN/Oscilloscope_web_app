function toggleWindow() {
    var window = document.getElementById("window");
    if (window.style.display === "none") {
        window.style.display = "block";
    } else {
        window.style.display = "none";
    }
}

function closeWindow() {
    var window = document.getElementById("window");
    window.style.display = "none";
}
