# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()
 
# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target
 
# store the feature and target names
feature_names = iris.feature_names
target_names = iris.target_names
 
# printing features and target names of our dataset
print("Feature names:", feature_names)
print("Target names:", target_names)
 
# X and y are numpy arrays
print("\nType of X is:", type(X))
 
# printing first 5 input rows
print("\nFirst 5 rows of X:\n", X[:5])
