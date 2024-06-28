Tyrone has an idea for the following:
Examine the general driving patterns of all the vehicles as clusters.
After examining general driving patterns, note outliers in the vehicle's movements.
Examine how often outliers are caused by specific vehicles. 
Tyrone is assuming that if a vehicle has only a small number of outliers over a year, then the outliers may indicate the driver being in a state of high adrenaline. 
Tyrone then believes that by examining the driving pattern changes occurring during the day of occurrence for the specific vehicle, it may reveal insights on how adrenaline can influence decision-making in terms of driving, and thus, assist with location prediction.

Explanation of Scripts
Data Collection (data_collection.py):

This script loads data from several TSV files and combines them into a single DataFrame.
It also loads speed limits data and saves both combined data sets to CSV files for further use.
Data Cleaning (data_cleaning.py):

This script cleans the collected data by removing rows with missing car IDs and converting all column names to lowercase.
It saves the cleaned data to new CSV files.
Data Transformation (data_transformation.py):

This script transforms the cleaned data by extracting the date and time from the timestamp column, if it exists.
It saves the transformed data to a new CSV file.
Feature Engineering (feature_engineering.py):

This script creates new features, such as categorizing the bearing into compass directions.
It saves the feature-engineered data to a new CSV file.
Model Selection and Training (model_selection.py):

This script selects and trains a RandomForestClassifier using the feature-engineered data.
It saves the trained model to a file using joblib.
Model Evaluation (training_evaluation.py):

This script evaluates the performance of the trained model using accuracy score and classification report.
It prints the evaluation metrics to the console.
Each script is designed to handle a specific step in the data processing and model training pipeline, ensuring that the data is properly prepared and the model is appropriately trained and evaluated. 

Random Forest Classifier
    Random Forest is an ensemble learning method used for classification and regression tasks.
    It operates by constructing multiple decision trees during training and outputting the class 
    that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.


Key Characteristics of Random Forest:
1. Ensemble Method: 
        Combines multiple decision trees to improve the model's performance and robustness.
2. Bootstrap Aggregation (Bagging):
     Uses bootstrapping (sampling with replacement) to create multiple subsets of the training data and builds a decision tree on each subset.
3. Random Feature Selection:
     At each split in the decision tree, a random subset of features is selected to determine the best split.
4. Overfitting Prevention:
     By averaging the results of multiple trees, Random Forest reduces the risk of overfitting compared to individual decision trees.

///////////////////////////////////////////
///////////////////////////////////////////
Implementation in the Code
The model selection and training steps are performed in model_selection.py and training_evaluation.py.

***************************************
model_selection.py:
This script selects and trains the Random Forest Classifier using the feature-engineered data.

python:
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    import joblib

    # Load the feature-engineered data
    anpr_features = pd.read_csv('anpr_features.csv')

    # Select features (independent variables) and target variable (dependent variable)
    X = anpr_features[['latitude', 'longitude', 'bearing_category']]
    y = anpr_features['car_id']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(clf, 'rf_model.pkl')

    print("Model training complete. Model saved to rf_model.pkl")

*********************************
training_evaluation.py:
This script evaluates the performance of the trained Random Forest Classifier.

python

    import pandas as pd
    from sklearn.metrics import classification_report, accuracy_score
    import joblib

    # Load the feature-engineered data and the trained model
    anpr_features = pd.read_csv('anpr_features.csv')
    clf = joblib.load('rf_model.pkl')

    # Select features and target variable
    X = anpr_features[['latitude', 'longitude', 'bearing_category']]
    y = anpr_features['car_id']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Predict on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print evaluation metrics
    print(f"Model Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)

////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////

Summary:
Model Used: 
    Random Forest Classifier.
Implementation Steps:
    Data Preparation: 
        Loading and cleaning data, feature engineering.
    Model Training: 
        Using RandomForestClassifier from scikit-learn.
    Model Evaluation: 
        Assessing the model's performance using accuracy and classification report metrics.
The current approach has led to a very low model accuracy due to the following issues:

Limited feature selection.
High cardinality of the target labels.
Possible overfitting or insufficient data for some labels.




