document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("/save_details", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Your account has been successfully created....");
            window.location.href = "/user_in"; // Change this to your actual dashboard URL
        } else {
            alert("Invalid username or password. Please try again.");
        }
    })
    .catch(error => console.error("Error:", error));
});
