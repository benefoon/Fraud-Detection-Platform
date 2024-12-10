-- setup_database.sql

-- Creating a table to store transaction data securely
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    transaction_time DATETIME NOT NULL,
    fraud_status VARCHAR(20) NOT NULL,
    encrypted_card_number BLOB -- Store encrypted card number
);

-- Insert example encrypted transaction data (encrypted card number)
INSERT INTO transactions (customer_id, transaction_amount, transaction_time, fraud_status, encrypted_card_number)
VALUES (123, 12000, NOW(), 'Fraudulent', 'gAAAAABlY0V8oU4L9GvM4h6Ae6xOBZ9Xf4zF0dTZ-xlBw9h7Kmfg6FgD6Eos5a7hvfFSRA==');
