#  Sentra: Cyberbullying Detector

**Sentra** adalah aplikasi deteksi cyberbullying berbasis **Natural Language Processing (NLP)** yang dirancang untuk mendeteksi komentar bernuansa **bullying, toxic, insult, body shaming, dan hate speech**, khususnya pada **Bahasa Indonesia**.

Aplikasi ini menggabungkan pendekatan **Rule-Based System** dan **Machine Learning (Detoxify Multilingual)** untuk menghasilkan deteksi yang lebih akurat, termasuk untuk **sindiran dan sarkasme**.

---

##  Fitur Utama

-  Deteksi komentar **Bullying / Non-bullying**
-  Klasifikasi tipe bullying (toxic, insult, appearance, identity attack, dll)
-  Dukungan **multibahasa** (auto-translation)
-  Rule-Based Engine untuk konteks lokal Bahasa Indonesia
-  Confidence score hasil prediksi
-  Antarmuka interaktif menggunakan **Streamlit**

---

##  Arsitektur Sistem

```text
User Input
   │
   ▼
Rule-Based Engine (Bahasa Indonesia)
   │   (jika terdeteksi)
   ├──▶ Hasil Final
   │
   ▼
Auto Translation (ID → EN)
   │
   ▼
Detoxify Multilingual Model
   │
   ▼
Hasil Deteksi + Confidence````

---

##  Model yang Digunakan

### 1️. Rule-Based Engine

Digunakan untuk mendeteksi pola bullying yang bersifat eksplisit dan kontekstual, seperti:

* Kata kasar lokal
* Sarkasme Bahasa Indonesia
* Body shaming eksplisit
* Bias budaya & slang

 **Cepat dan akurat** untuk pola yang sudah dikenal.

---

### 2️. Detoxify Multilingual

Model deep learning berbasis **Transformer** yang digunakan untuk mendeteksi:

* Toxicity
* Insult
* Identity attack
* Threat
* Obscene content


---

##  Struktur Folder

```text
Sentra Cyberbullying Detector/
│
├── app/                # Streamlit App
│   └── app.py
│
├── src/                # Core logic
│   ├── classifier.py
│   ├── model.py        # Detoxify model
│   ├── rule_engine.py
│   └── preprocessing.py
│
├── dataset/            # Dataset cyberbullying
├── testing/            # Evaluasi & testing
├── requirements.txt
└── README.md
```

---

##  Cara Menjalankan Aplikasi

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/sentra-cyberbullying-detector.git
cd sentra-cyberbullying-detector
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Jalankan Aplikasi

```bash
streamlit run app/app.py
```

---
