Sure, here's a line-by-line explanation of your code:

```python
from sklearn.naive_bayes import GaussianNB 
```
This line imports the `GaussianNB` class from the `sklearn.naive_bayes` module. `GaussianNB` implements the Gaussian Naive Bayes algorithm for classification.

```python
from sklearn.datasets import load_iris 
```
This line imports the `load_iris` function from the `sklearn.datasets` module. `load_iris` is a function that loads and returns the iris dataset (classification).

```python
from sklearn import metrics 
```
This line imports the `metrics` module from `sklearn`. This module includes score functions, performance metrics, pairwise metrics, and distance computations.

```python
from sklearn.model_selection import train_test_split
```
This line imports the `train_test_split` function from the `sklearn.model_selection` module. This function splits arrays or matrices into random train and test subsets.

```python
dataset = load_iris()
```
This line loads the iris dataset and stores it in the `dataset` variable.

```python
X = dataset. data
y = dataset. target
```
These lines assign the features and the target from the dataset to `X` and `y` respectively.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
```
This line splits the dataset into training set and test set. 80% of the data will be used for training and 20% for testing.

```python
gnb = GaussianNB()
```
This line creates an instance of the `GaussianNB` class.

```python
classifier = gnb.fit(X_train, y_train)
```
This line fits the model on the training data. `fit` is a method that trains the algorithm on the data.

```python
y_pred = classifier.predict(X_test)
```
This line uses the trained model to predict the target for the test data.

```python
print( 'Accuracy metrics:', metrics.classification_report(y_test, y_pred))
```
This line prints the classification report, which includes metrics such as precision, recall, f1-score, etc.

```python
print( 'Accuracy of the classifier is:', metrics.accuracy_score(y_test, y_pred))
```
This line prints the accuracy of the classifier. Accuracy is the fraction of predictions our model got right.

```python
print("Confusion matrix:")
print(metrics.confusion_matrix(y_test, y_pred))
```
These lines print the confusion matrix, which is a table used to describe the performance of a classification model.