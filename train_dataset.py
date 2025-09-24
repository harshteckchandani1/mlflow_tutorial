import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import dagshub
import os

# DagsHub repo credentials
os.environ["MLFLOW_TRACKING_USERNAME"] = "harshteckchandani1"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "2583c044d34ddb31d0bec5b341574b83ade9ba8e"

# Set MLflow tracking URI to your DagsHub repo
mlflow.set_tracking_uri("https://dagshub.com/harshteckchandani1/mlflow_tutorial.mlflow")



# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# Load wine dataset
wine = load_wine()
x = wine.data
y = wine.target

# train test split

x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size=0.10, random_state=42)

# define the params for RF model

max_depth = 5
n_estimators = 8 

# Mention experiment name below for user convenience
mlflow.set_experiment("test123")

with mlflow.start_run():
    rf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rf.fit(x_train, y_train)

    y_pred = rf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_param('max_depth', max_depth)
    mlflow.log_param('n_estimators', n_estimators)

    # Creating confusion matrix 
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, fmt= 'd', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion matrix')

    # save plot 
    plt.savefig("confusion-matrix.png")

    # Log artifacts using mlflow
    mlflow.log_artifact("confusion-matrix.png")
    mlflow.log_artifact(__file__)

    print(accuracy)