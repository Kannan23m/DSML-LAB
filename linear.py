from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data1.xlsx')
X = df[['gives birth','aquatic','aerial','legs']]
y = df[['class label']]
target_names = ['mammal','reptile','fish','amphbibian','bird']
feature_names = ['gives birth','aquatic','aerial','legs']
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
print(x_train)
print(y_train)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(y_pred)
print(clf.predict(x_train))
print(y_train.values.ravel())