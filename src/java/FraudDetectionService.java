import java.util.*;

public class FraudDetectionService {

    // Example fraud detection rules with basic thresholds
    public static String detectFraud(double transactionAmount, String location) {
        // Rule-based detection (basic example)
        if (transactionAmount > 10000) {
            return "Fraudulent: Transaction amount too high";
        }
        if (location.equals("Suspicious Country")) {
            return "Fraudulent: Suspicious location";
        }
        return "Legitimate";
    }

    public static void main(String[] args) {
        // Sample transaction data
        double transactionAmount = 12000;
        String location = "Suspicious Country";

        // Detect fraud
        String fraudStatus = detectFraud(transactionAmount, location);
        System.out.println("Transaction Status: " + fraudStatus);
    }
}
