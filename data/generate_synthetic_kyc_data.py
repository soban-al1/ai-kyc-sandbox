import faker, random, pandas as pd
fake = faker.Faker()

def make_row():
    return {
        "age": random.randint(18, 70),
        "country": fake.country_code(),
        "doc_type": random.choice(["passport", "id_card"]),
        "pep_match": random.choice([0, 1]),
        "face_match": random.choice([0, 1]),
        "label": random.choices([0, 1], weights=[0.95, 0.05])[0],  # 5% fraud
    }

df = pd.DataFrame([make_row() for _ in range(10_000)])
df.to_csv("synthetic_kyc.csv", index=False)
