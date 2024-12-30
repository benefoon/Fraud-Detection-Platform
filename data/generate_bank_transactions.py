from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(42)

def generate_transactions(n):
    transactions = []
    for _ in range(n):
        transactions.append({
            'transaction_id': fake.uuid4(),
            'user_id': fake.uuid4(),
            'amount': round(random.uniform(10, 10000), 2),
            'timestamp': fake.date_time_this_year(),
            'location': fake.city(),
            'is_fraud': random.choice([0, 1])
        })
    return pd.DataFrame(transactions)

data = generate_transactions(1000)  # 1000 تراکنش
data.to_csv('transactions.csv', index=False)