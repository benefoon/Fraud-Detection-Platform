// dashboard.js

// Function to display fraud status in the dashboard
function displayFraudStatus(transaction) {
    let fraudStatus = transaction.fraudStatus;
    let statusElement = document.getElementById("fraudStatus");
    
    // Highlight fraudulent transactions
    if (fraudStatus === "Fraudulent") {
        statusElement.style.color = "red";
    } else {
        statusElement.style.color = "green";
    }

    statusElement.textContent = "Fraud Status: " + fraudStatus;
}

// Example transaction object
let transaction = {
    id: 12345,
    amount: 12000,
    location: "Suspicious Country",
    fraudStatus: "Fraudulent"
};

// Display the fraud status
displayFraudStatus(transaction);
