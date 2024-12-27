package com.fraud.service;

import org.springframework.stereotype.Service;

@Service
public class FraudService {
    public String checkFraud(String transactionId) {
        // Business logic to check fraud
        // This could involve calling a machine learning model API
        return "Fraud Probability for Transaction " + transactionId + ": 85%";
    }
}
