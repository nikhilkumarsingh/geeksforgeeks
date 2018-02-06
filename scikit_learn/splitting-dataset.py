# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()
 
# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target
 
# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
 
# printing the shapes of the new X objects
print(X_train.shape)
print(X_test.shape)
 
# printing the shapes of the new y objects
print(y_train.shape)
print(y_test.shape)
