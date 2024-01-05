Sure, here's a line-by-line explanation of your code:

```python
from sklearn.naive_bayes import GaussianNB 
```
This line imports the `GaussianNB` class from the `sklearn.naive_bayes` module. `GaussianNB` implements the Gaussian Naive Bayes algorithm for classification.

```python
from sklearn.datasets import load_iris 
```
This line imports the `load_iris` function from the `sklearn.datasets` module. The `load_iris` function loads the Iris dataset, a classic dataset in machine learning and statistics.

```python
from sklearn import metrics 
```
This line imports the `metrics` module from `sklearn`. This module includes score functions, performance metrics, pairwise metrics, and distance computations.

```python
from sklearn.model_selection import train_test_split
```
This line imports the `train_test_split` function from the `sklearn.model_selection` module. This function is a quick utility that wraps input validation and `next(ShuffleSplit().split(X, y))` and application to input data into a single call for splitting (and optionally subsampling) data in a oneliner.

```python
dataset = load_iris()
```
This line loads the Iris dataset and stores it in the `dataset` variable.

```python
X = dataset. data
y = dataset. target
```
These lines assign the features and the targets from the dataset to `X` and `y`, respectively.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
```
This line splits the dataset into training set and test set. `test_size=0.2` means that 20% of the data will be used for testing, and `random_state=1` is used for reproducibility of the results.

```python
gnb = GaussianNB()
```
This line creates an instance of the `GaussianNB` class.

```python
classifier = gnb.fit(X_train, y_train)
```
This line trains the Gaussian Naive Bayes classifier on the training data.

```python
y_pred = classifier.predict(X_test)
```
This line uses the trained classifier to predict the target values for the test data.

```python
print( 'Accuracy metrics:', metrics.classification_report(y_test, y_pred))
```
This line prints the classification report, which includes precision, recall, f1-score, and support for each class.

```python
print( 'Accuracy of the classifier is:', metrics.accuracy_score(y_test, y_pred))
```
This line prints the accuracy of the classifier, which is the proportion of correct predictions over total predictions.

```python
print("Confusion matrix:")
print(metrics.confusion_matrix(y_test, y_pred))
```
These lines print the confusion matrix, which is a table layout of the performance of the model on the classification problem. The rows of the matrix are the true classes, and the columns are the predicted classes.