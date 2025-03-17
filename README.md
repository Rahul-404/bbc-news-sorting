# News Sorting with NLP: BBC News Dataset 📰🔍

## Overview
Welcome to the News Sorting project using Natural Language Processing (NLP) techniques applied to the BBC News Dataset. This project aims to classify news articles into predefined categories such as business, entertainment, politics, sport, and tech. By leveraging NLP, we'll extract features from the text data to build a machine learning model capable of accurately categorizing news articles.

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Dataset](#dataset)
- [Approach](#approach)
- [Results](#results)
- [Usage](#usage)
- [Project Demo](#project-demo)
- [License](#license)

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/bcc-news-classification.git
cd bcc-news-classification
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Requirements
To run the project, you'll need Python 3.x and the following libraries:
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- nltk
- wordcloud
- tensorflow
- mlflow

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 🔧 To make any updates in code: Follow the workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity -> config_entity.py
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## Dataset

The BBC News Dataset consists of news articles published by the BBC, categorized into five predefined classes: business, entertainment, politics, sport, and tech. Each article contains textual content along with its corresponding category label. The dataset is available on [Kaggle](https://www.kaggle.com/shivamkushwaha/bbc-full-text-document-classification).

### Train, Test and Validation Split:

## Approach

1. **Data Preprocessing:**
   - Text cleaning
      - Normalizing
      - remove currencies
      - remove distance
      - remove conturies
      - remove numbers
      - remove special characters
      - remove punctuations
      - remove multiple spaces
      - remove stopwords
      - lemmetization

   - Tokenization
   - Vectorization
      1. One-Hot Encoding
      2. TF-IDF Encoding
      3. Word2Vec Embeddings
      4. Glove Embeddings
      5. Fasttext Embeddings

2. **Machine Learning Models:**
   - Logistic Regression
   - Support Vector Machine (SVM)
   - Naive Bayes
   - Random Forest
   - Gradient Boost

3. **Deep Learning Models:**
   - Multi Layer Perceptron
   - LSTM with 2 Dense layers
   - LSTM
   - Bidirectional LSTM

4. **Model Evaluation:**
   - Precision, Recall, F1-Score
   - Confusion matrix and ROC curve for performance analysis.


## Results

The models were evaluated on precision, recall, F1-score and ROC curve. Below are the results:

```
+---------------------------+----------+-------+----------+
| Baseline Model (F1 Score) | Word2Vec | Glove | Fasttext |
+---------------------------+----------+-------+----------+
|    Logistic Regression    |   0.96   |  0.96 |   0.96   |
|        Naive Bayes        |   0.84   |  0.92 |   0.8    |
|            SVC            |   0.96   |  0.96 |   0.96   |
|       Random Forest       |   0.96   |  0.95 |   0.95   |
|       Gradient Boost      |   0.97   |  0.96 |   0.93   |
+---------------------------+----------+-------+----------+
```
```
+------------------------------+-------------------+---------------------+
|            Model             |     Embedding     | Validation F1 Score |
+------------------------------+-------------------+---------------------+
| Baseline Logistic Regression |       GloVe       |         0.97        |
|             MLP              |   No Embeddings   |         0.92        |
|             MLP              |       Glove       |         0.14        |
|             MLP              |   Glove(Trained)  |         0.95        |
|             MLP              |      Fasttext     |         0.92        |
|             MLP              | Fasttext(Trained) |         0.96        |
|     LSTM 2 Dense layers      |      Fasttext     |         0.18        |
|             LSTM             |      Fasttext     |         0.13        |
|      Bidirectional LSTM      |       Glove       |         0.95        |
+------------------------------+-------------------+---------------------+
```

Confusion matrices and other relevant graphs:

```
             precision    recall  f1-score   support

           0       0.98      0.96      0.97       101
           1       0.97      0.97      0.97        78
           2       0.96      0.96      0.96        82
           3       1.00      1.00      1.00       104
           4       0.98      1.00      0.99        82

    accuracy                           0.98       447
   macro avg       0.98      0.98      0.98       447
weighted avg       0.98      0.98      0.98       447
```

<!-- ![Confusion Matrix](confusion_matrix.png) -->


## Usage

To make predictions on new news articles, you can use the following function:

```python
from model import predict_category

article_text = "Your news article text here."
predicted_category = predict_category(article_text)
print(predicted_category)
```
You can also run the training script to retrain the models:
```bash
python train.py
```

## Project Demo


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
