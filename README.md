# 🎬 Bollywood Movie Recommendation System

A minimalistic Streamlit app that recommends Bollywood movies based on their **overview** or **genre**, using Natural Language Processing and cosine similarity.

## 📌 Project Overview

This project uses the IMDB dataset of Bollywood movies (1951–2023) to build a content-based recommendation engine. Users can input a movie name, and the app suggests similar titles based on textual features.

## 🧠 Techniques Used

- **Natural Language Processing (NLP)** for text cleaning and vectorization
- **TF-IDF Vectorizer** to convert movie overviews into numerical format
- **Cosine Similarity** to measure textual closeness between movies
- **Streamlit** for building an interactive web app

## 📁 Dataset

- `IMDB-Movie-Dataset(2023-1951).csv`: Contains movie name, genre, overview, director, and cast

## 🚀 Features

- Recommend movies based on **plot overview**
- Recommend movies based on **genre**
- Clean and responsive **Streamlit UI**
- Bollywood-specific recommendations

## 🧪 Sample Recommendations

- Input: `"Jawan"` → Output: `"Jailer"`, `"Rocky Aur Rani Kii Prem Kahaani"`, `"Jaane Jaan"`
- Input Genre: `"Action"` → Output: `"Jawan"`, `"Jailer"`, `"Kyo Kii... Main Jhuth Nahin Bolta"`

## 📊 What I Learned

- How to apply NLP techniques to real-world datasets
- Using cosine similarity for content-based filtering
- Building user-friendly apps with Streamlit
- Handling large datasets and optimizing recommendations

## 📬 Contact
Made with ❤️ by [Hemlalit](https://www.linkedin.com/in/hemlalitmali/)
