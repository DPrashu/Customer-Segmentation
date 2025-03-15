document.addEventListener("DOMContentLoaded", function () {
    console.log("🚀 Welcome to the Customer Segmentation Project!");

    // Open modal
    document.getElementById("loginButton").addEventListener("click", function () {
        document.getElementById("loginModal").style.display = "block";
    });

    // Close modal
    document.querySelector(".close-btn").addEventListener("click", function () {
        document.getElementById("loginModal").style.display = "none";
    });

    // Toggle between Login & Signup
    document.getElementById("toggle-form").addEventListener("click", function (event) {
        event.preventDefault();
        let title = document.getElementById("modal-title");
        let button = document.querySelector(".submit-btn");

        if (title.innerText === "Login") {
            title.innerText = "Sign Up";
            button.innerText = "Sign Up";
            document.getElementById("toggle-form").innerHTML = `Already have an account? <a href="#">Login</a>`;
        } else {
            title.innerText = "Login";
            button.innerText = "Login";
            document.getElementById("toggle-form").innerHTML = `Don't have an account? <a href="#">Sign up</a>`;
        }
    });

    // Handle form submission
    document.getElementById("auth-form").addEventListener("submit", function (event) {
        event.preventDefault();
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;
        let action = document.querySelector(".submit-btn").innerText;

        fetch(`/${action.toLowerCase()}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        }).then(res => res.json()).then(data => {
            alert(data.message);
            if (data.success) {
                document.getElementById("loginModal").style.display = "none";
            }
        });
    });
});
