import java.util.*;

public class FraudDetectionService {
    public static void main(String[] args) {
        // Example transaction
        Map<String, Object> transaction = new HashMap<>();
        transaction.put("customerId", 12345);
        transaction.put("amount", 5000);
        transaction.put("location", "New York");
        transaction.put("time", "2024-12-10T10:15:30");

        // Simulate fraud detection
        boolean isFraud = detectFraud(transaction);
        System.out.println("Transaction Fraudulent: " + isFraud);
    }

    public static boolean detectFraud(Map<String, Object> transaction) {
        double amount = (double) transaction.get("amount");
        String location = (String) transaction.get("location");

        // Simple rule-based fraud detection
        return amount > 1000 && "New York".equals(location);
    }
}
