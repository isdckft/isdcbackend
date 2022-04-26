from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer



# Get the parameters
@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def iris(request):
    mlIris()
    return render(request,'ml/irisresult.html')

@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def dataPreProc(request):
    mldatapreproc()
    return render(request,'ml/datapreprocres.html')

def mlIris():
    # dataset beolvasása
    df=pd.read_csv(settings.STATIC_DIR+'/ml/data/iris.csv')
    outputname ='/ml/irisresult.html'
    filename = settings.TEMPLATE_DIR+outputname
 

    file=open(filename, "w")
    print ("<!DOCTYPE html>{% extends 'base.html' %}{% block body_block %}", file=open(filename, "a"))
    print("<h1>Iris ML Example</h1>", file=open(filename, "a"))
    print("<pre>", file=open(filename, "a"))



    # Create arrays for the features and the response variable
    y = df['species'].values
    X = df.drop('species', axis=1).values

    # Split into training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42, stratify=y)

    # Set the classification
    knn = KNeighborsClassifier(n_neighbors=6)

    # Fit the classifier to the data
    knn.fit(X_train,y_train)

    # Predict the test data
    y_pred = knn.predict(X_test)

    # Print the test data
    print("Prediction: {}".format(y_pred),file=open(filename, "a"))

    # Print the accuracy
    print('Iris accuracy',file=open(filename, "a"))
    print(knn.score(X_test, y_test),file=open(filename, "a"))

    # Generate the confusion matrix and classification report
    print("Classification matrix (TP, TN, FP, FN)",file=open(filename, "a"))
    print(confusion_matrix( y_test,y_pred),file=open(filename, "a"))
    print("Classification report",file=open(filename, "a"))
    print("Precision=TP/(TP+FP), Recall=TP/(TP+FN), F1sore/2*precision*recall/(precisuon+recall)",file=open(filename, "a"))
    print(classification_report(y_test,y_pred),file=open(filename, "a"))
    print("</pre>", file=open(filename, "a"))
    print ("{% endblock %}", file=open(filename, "a"))
    file.close()

    return True

   

def mldatapreproc():

    # Data Preprocessing demo

    # Output HTML 
    outputname ='/ml/datapreprocres.html'
    filename = settings.TEMPLATE_DIR+outputname
    file=open(filename, "w")
    print ("<!DOCTYPE html>{% extends 'base.html' %}{% block body_block %}", file=open(filename, "a"))
    print("<h1>Data Preprocessing example</h1>", file=open(filename, "a"))
    print("<pre>", file=open(filename, "a"))

    # Importing the dataset
    dataset = pd.read_csv(settings.STATIC_DIR+'/ml/data/countrysal.csv')



    print('Input data', file=open(filename, "a"))
    print(dataset, file=open(filename, "a"))
    X = dataset.iloc[:, :-1].values # the features goes into X matrix
    y = dataset.iloc[:, 3].values # the last column goes into y array


    # complete missing values
    imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean') 
    imputer = imputer.fit(X[:, 1:3])
    X[:, 1:3] = imputer.transform(X[:, 1:3])

    # Encoding the Independent Variable

    labelencoder_X = LabelEncoder()
    # Transforms the country names into numbers
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

    # Transform the first columns into 3 columns
    onehotencoder = OneHotEncoder(categorical_features = [0])
    X = onehotencoder.fit_transform(X).toarray()
    # Encoding the Dependent Variable
    labelencoder_y = LabelEncoder()

    #transforms y to numbers
    y = labelencoder_y.fit_transform(y)


    # split data set to traineng set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Feature Scaling - Stanradisation
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(X_train)
    x_test = sc_x.transform(X_test)


    print('Preprocessed data with StandardScaler', file=open(filename, "a"))
    print (x_train, file=open(filename, "a"))
    print(x_test, file=open(filename, "a"))
    print(y_train, file=open(filename, "a"))
    print(y_test, file=open(filename, "a"))

    # Feature Scaling- Normalisation
    from sklearn.preprocessing import Normalizer
    sc_x = Normalizer()
    x_train = sc_x.fit_transform(X_train)
    x_test = sc_x.transform(X_test) # you do not need to fit it, because it is on the same basis as x_train


    print('Preprocessed data with Normalizer', file=open(filename, "a"))
    print (x_train, file=open(filename, "a"))
    print(x_test, file=open(filename, "a"))
    print(y_train, file=open(filename, "a"))
    print(y_test, file=open(filename, "a"))

    print("</pre>", file=open(filename, "a"))
    print ("{% endblock %}", file=open(filename, "a"))
    file.close()
    return True
  