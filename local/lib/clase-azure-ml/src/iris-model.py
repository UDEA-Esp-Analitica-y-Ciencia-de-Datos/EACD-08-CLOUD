from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import pickle

if __name__ == "__main__":
    iris = datasets.load_iris()

    #Datasets: Prep
    x=iris.data
    y=iris.target

    #Train and test data
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3)

    #ML Model: Model Selection
    knn=neighbors.KNeighborsClassifier()
    knn.fit(x_train, y_train)

    #Predictions
    predictions=knn.predict(x_test)

    #Accuracy
    print(accuracy_score(y_test,predictions))

    #Registro
    with open('./outputs/iris_model.pkl', 'wb') as model_pkl:
        pickle.dump(knn, model_pkl)
        