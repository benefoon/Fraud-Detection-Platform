package com.fraud.controller;

import org.springframework.web.bind.annotation.*;
import com.fraud.service.FraudService;
import com.fraud.model.Transaction;

@RestController
@RequestMapping("/api/fraud")
public class FraudController {
    private final FraudService fraudService;

    public FraudController(FraudService fraudService) {
        this.fraudService = fraudService;
    }

    @GetMapping("/check/{transactionId}")
    public String checkFraud(@PathVariable String transactionId) {
        // Call fraud detection logic
        return fraudService.checkFraud(transactionId);
    }
}
