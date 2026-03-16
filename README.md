# 🎬 Movie Recommendation System

A **Machine Learning based Movie Recommendation System** that suggests movies to users based on similarity between movie features such as genres, keywords, cast, and overview. The system analyzes movie metadata and recommends movies that are most similar to the one selected by the user.

---

## 📌 Overview

Recommendation systems are widely used in streaming platforms like Netflix and Amazon Prime. This project implements a **content-based recommendation system** that recommends movies by computing similarity between movie descriptions.

The system processes movie datasets, extracts important features, converts them into vectors, and calculates similarity scores to recommend the most relevant movies.

---

## ✨ Features

* 🎥 Movie recommendation based on similarity
* 🔎 Search movies and get similar recommendations
* 📊 Uses content-based filtering technique
* ⚡ Fast recommendation using cosine similarity
* 🧠 Built using machine learning and NLP techniques

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **NLTK**
* **Streamlit / Flask (for UI if implemented)**
* **TMDB Movie Dataset**

---

## 📂 Project Structure

```
movie-recommendation-system
│
├── data/
│   ├── movies.csv
│   └── credits.csv
│
├── notebooks/
│   └── movie_recommendation.ipynb
│
├── app.py
├── similarity.pkl
├── movie_list.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load movie datasets containing information about movies and their credits.
2. Perform **data preprocessing and feature engineering**.
3. Combine relevant features such as:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
4. Convert textual data into numerical vectors using **CountVectorizer / TF-IDF**.
5. Calculate similarity between movies using **Cosine Similarity**.
6. Recommend the **top 5 most similar movies** to the selected movie.

---

## 📊 Dataset

The dataset used for this project is the **TMDB Movie Dataset**.

It includes information such as:

* Movie title
* Genres
* Cast
* Crew
* Keywords
* Overview
* Popularity metrics

Dataset Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 💻 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```

### 2️⃣ Navigate to the project directory

```bash
cd movie-recommendation-system
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

If using Python script:

```bash
python app.py
```

If using Streamlit interface:

```bash
streamlit run app.py
```

---

## 🎥 Example Recommendation

**Input Movie:** Avatar

**Recommended Movies:**

1. Guardians of the Galaxy
2. John Carter
3. Star Trek
4. Jupiter Ascending
5. Avengers

---

## 🚀 Future Improvements

* Implement **Collaborative Filtering**
* Hybrid recommendation system
* User login and watch history tracking
* Deep learning based recommendation models
* Deploy the application on **Heroku / AWS / Streamlit Cloud**

---

## 🤝 Contributing

Contributions are welcome!
If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful, please consider **starring the repository** ⭐
