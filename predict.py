x = [[10,9],[1,4],[10,1],[7,10],[3,10],[1,1],[8,5],[3,7],[3,6],[7,3]]
y = ['fruit','protein','fruit','vegetable','vegetable','protein','fruit','vegetable','protein','fruit']
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)
tomato = [[6,4]]
print(classifier.predict(tomato))
orange = [[7,3]]
print(classifier.predict(orange))
