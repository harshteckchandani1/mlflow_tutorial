import mlflow

# print("Printing URI scheme below: ")

# print(mlflow.get_tracking_uri())

# print("\n")

# mlflow.set_tracking_uri("http://127.0.0.1:5000")

# print("printing new tracking uri ")

# print(mlflow.get_tracking_uri())

# print("\n")

import dagshub
dagshub.init(repo_owner='harshteckchandani1', repo_name='mlflow_tutorial', mlflow=True)

