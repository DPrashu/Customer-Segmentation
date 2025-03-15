document.addEventListener("DOMContentLoaded", function () {
    // Get form elements
    const customerIdInput = document.getElementById("customer_id");
    const transactionAmountInput = document.getElementById("transaction_amount");
    const lastVisitInput = document.getElementById("last_visit");
    const visitsInput = document.getElementById("total_visits");
    const countrySelect = document.getElementById("country");
    const charCounter = document.getElementById("char-counter");
    const submitButton = document.getElementById("submit-btn");
    const form = document.getElementById("customer-form");

    // 1️⃣ **Customer ID Character Counter**
    customerIdInput.addEventListener("input", function () {
        const maxLength = 10;
        const currentLength = customerIdInput.value.length;
        charCounter.textContent = `${currentLength}/${maxLength}`;
        charCounter.style.color = currentLength > maxLength ? "red" : "lightgreen";
    });

    // 2️⃣ **Restrict Future Dates in Last Visit**
    let today = new Date().toISOString().split("T")[0];
    lastVisitInput.setAttribute("max", today);

    // 3️⃣ **Auto-format Transaction Amount (₹ currency)**
    transactionAmountInput.addEventListener("input", function (event) {
        let value = event.target.value.replace(/[^0-9.]/g, ""); // Allow only numbers & dot
        if (value) {
            event.target.value = `₹${parseFloat(value).toFixed(2)}`; // Format as currency
        }
    });

    // 4️⃣ **Real-time Validation (Fixed multiple ticks issue)**
    function validateInput(input, condition, errorMessage) {
        let errorElement = input.parentNode.querySelector(".error-message");

        if (!errorElement) {
            errorElement = document.createElement("small");
            errorElement.classList.add("error-message");
            input.parentNode.appendChild(errorElement);
        }

        if (condition) {
            errorElement.textContent = errorMessage;
            errorElement.style.color = "red";
            input.style.border = "2px solid red";
            return false;
        } else {
            errorElement.textContent = "";  // Remove previous error message
            input.style.border = "2px solid lightgreen";
            return true;
        }
    }

    function validateForm() {
        let isCustomerIdValid = validateInput(customerIdInput, customerIdInput.value.length > 10, "Max 10 characters allowed!");
        let isTransactionValid = validateInput(transactionAmountInput, isNaN(parseFloat(transactionAmountInput.value.replace("₹", ""))), "Enter a valid amount!");
        let isVisitsValid = validateInput(visitsInput, isNaN(visitsInput.value) || visitsInput.value < 1, "Must be a positive number!");
        let isDateValid = validateInput(lastVisitInput, !lastVisitInput.value, "Date is required!");
        let isCountryValid = validateInput(countrySelect, countrySelect.value === "", "Please select a country!");

        // Enable submit button only if all fields are valid
        submitButton.disabled = !(isCustomerIdValid && isTransactionValid && isVisitsValid && isDateValid && isCountryValid);
    }

    form.addEventListener("input", validateForm);

    // 5️⃣ **Smooth Animations on Focus**
    document.querySelectorAll("input, select").forEach((input) => {
        input.addEventListener("focus", function () {
            this.style.transition = "0.3s";
            this.style.transform = "scale(1.05)";
            this.style.boxShadow = "0px 0px 8px rgba(255, 255, 255, 0.4)";
        });

        input.addEventListener("blur", function () {
            this.style.transform = "scale(1)";
            this.style.boxShadow = "none";
        });
    });
});
