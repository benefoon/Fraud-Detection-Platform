const transactions = [
    { id: 1, amount: 1500, isFraud: true },
    { id: 2, amount: 200, isFraud: false },
    { id: 3, amount: 5000, isFraud: true }
];

function renderDashboard(transactions) {
    const container = document.getElementById("dashboard");
    transactions.forEach(txn => {
        const txnElement = document.createElement("div");
        txnElement.innerHTML = `
            <p>Transaction ID: ${txn.id}</p>
            <p>Amount: ${txn.amount}</p>
            <p>Status: ${txn.isFraud ? 'Fraudulent' : 'Legitimate'}</p>
        `;
        txnElement.style.color = txn.isFraud ? 'red' : 'green';
        container.appendChild(txnElement);
    });
}

renderDashboard(transactions);
