# Coding Challenge for a BMW Job Interview

While it might be unorthodox to post code from a job 
interview coding challenge, I not only found this challenge 
enjoyable, but also a good opportunity to showcase various
modeling techniques.

### Project Structure
- [`data`](data): this folder contains the CSV files used in the coding
challenged. I believe this was a combination of real and synthesized/anonymized
data


- [`Tasks-BMW.pdf`](Tasks-BMW.pdf): actual writeup describing each section of the coding
challenge. There were four tasks, so I created separate notebooks for
tasks 1, 2, and combined 3-4.


- [`Task1.ipynb`](Task1.ipynb): Ensemble of binary classifiers for a tabular dataset
of mixed data types. Classifiers included SVM, naive Bayes, and a
gradient boosted classifier. All models were hyperoptimized using
sklearn's grid search method. The ensembler was based on hard voting of
the predictors.


- [`Task2.ipynb`](Task2.ipynb): Dimensionality reduction using latent semantic
analysis, unsupervised outlier detection using isolation forests,
and nearest neighbor search using k-d trees


- [`Task3-4.ipynb`](Task3-4.ipynb): Creates some functions to calculate elapsed time
between timestamps