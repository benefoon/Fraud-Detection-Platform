-- Aggregate transaction data
SELECT 
    customer_id, 
    COUNT(transaction_id) AS total_transactions, 
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS fraud_count, 
    AVG(amount) AS avg_transaction_amount, 
    MAX(amount) AS max_transaction_amount
FROM transactions
GROUP BY customer_id;

-- Create indices for faster queries
CREATE INDEX idx_customer_id ON transactions (customer_id);
