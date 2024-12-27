package com.fraud.model;

import java.time.LocalDateTime;

public class Transaction {

    private Long id;                // Unique identifier for the transaction
    private Long userId;            // Identifier for the user making the transaction
    private Double amount;          // Transaction amount
    private LocalDateTime timestamp; // Timestamp of the transaction
    private Float fraudProbability; // Probability of fraud (calculated)

    // Default constructor (required for frameworks like Spring)
    public Transaction() {}

    // Parameterized constructor
    public Transaction(Long id, Long userId, Double amount, LocalDateTime timestamp, Float fraudProbability) {
        this.id = id;
        this.userId = userId;
        this.amount = amount;
        this.timestamp = timestamp;
        this.fraudProbability = fraudProbability;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public Double getAmount() {
        return amount;
    }

    public void setAmount(Double amount) {
        this.amount = amount;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }

    public Float getFraudProbability() {
        return fraudProbability;
    }

    public void setFraudProbability(Float fraudProbability) {
        this.fraudProbability = fraudProbability;
    }

    // Override toString for better logging
    @Override
    public String toString() {
        return "Transaction{" +
                "id=" + id +
                ", userId=" + userId +
                ", amount=" + amount +
                ", timestamp=" + timestamp +
                ", fraudProbability=" + fraudProbability +
                '}';
    }
}
