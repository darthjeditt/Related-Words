# Related Words Machine Learning Project

This project focuses on training a Word2Vec model on the "reuters" dataset to generate word embeddings and explore related words. The goal is to understand the relationships between words and capture their semantic meanings.

## Setup and Dependencies
To run the project, ensure you have the following dependencies installed:
- NLTK (Natural Language Toolkit)
- Gensim
- Scikit-learn

You can install the dependencies by running the following command:
```
pip install nltk gensim scikit-learn
```

## Project Overview
1. Import Libraries: Import the necessary libraries, including NLTK, Gensim, and Scikit-learn, to perform the required tasks.

2. Download Datasets: Download the "reuters" dataset, which contains a collection of documents and news articles, using the NLTK library.

3. Preparing the Dataset: Preprocess the dataset by splitting it into training and validation sets using the `train_test_split` function from Scikit-learn.

4. Callback Function: Define a callback function to display the loss after each epoch during the training process.

5. Preprocess Text and Train Dataset: Implement a function to preprocess the text, filtering out words based on a set criteria, and apply it to the training dataset.

6. Training the Model: Train the Word2Vec model using the training dataset. Specify the vector size, window size, minimum word count, number of workers, epochs, and enable loss computation. Use the callback function to display the loss after each epoch.

7. Save the Model: Save the trained Word2Vec model to a file for future use.

## Usage
1. Clone or download the project.
2. Install the project dependencies as mentioned in the "Setup and Dependencies" section.
3. Run the Python script or Jupyter Notebook containing the project code.
4. Follow the output to observe the training progress and save the trained model.
5. Run the 'main' python file for a custom GUI to test the trained model.

## Conclusion
The "Related Words" project showcases the training of a Word2Vec model on the "reuters" dataset. By understanding the relationships between words and generating word embeddings, we can explore the semantic meanings of words. The trained model can be utilized in various natural language processing tasks, such as word similarity, word analogies, and text classification. This project serves as a foundation for working with word embeddings and analyzing textual data.