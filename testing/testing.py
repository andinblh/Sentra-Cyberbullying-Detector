from detoxify import Detoxify
import pandas as pd
from sklearn.metrics import classification_report

# 1. Load dataset
df = pd.read_csv("../dataset/DSPreprocessing_Twitter.csv")

# pilih kolom yang mau digunakan
texts = df["Text"].astype(str).tolist()
true_labels = df["Label"].tolist()

# 2. Load model Detoxify multilingual
model = Detoxify("multilingual")

# 3. Prediksi skor untuk setiap teks
preds = []
for t in texts:
    result = model.predict(t)
    toxic_score = result["toxicity"]
    preds.append(1 if toxic_score >= 0.5 else 0)   # threshold 0.5 (bisa diubah)

# 4. Evaluasi model
print(classification_report(true_labels, preds))
