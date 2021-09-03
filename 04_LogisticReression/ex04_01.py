import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))


# 2. Importing the Data set
dataset = pd.read_csv('../data/input/Social_Network_Ads.csv')

# 3. Splitting our Data set in Dependent and Independent variables
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

# 4. Splitting the Data set into the Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,
                                                    random_state = 0)
# 5. Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train01 = X_train
X_test01 = X_test

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

X_train02 = X_train
X_test02 = X_test
# 6. Fitting Logistic Regression to the Training Set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# 7. Predicting the Test set results
y_pred = classifier.predict(X_test)

# 8. Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#  Visualizing the training set result
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1,
                               stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1,
                               stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
