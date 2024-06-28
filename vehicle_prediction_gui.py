import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Function to load data
def load_data():
    global anpr_data
    file_path = filedialog.askopenfilename()
    if file_path:
        anpr_data = pd.read_csv(file_path)
        messagebox.showinfo("Info", "Data Loaded Successfully")
    else:
        messagebox.showwarning("Warning", "No File Selected")

# Function to clean data
def clean_data():
    global anpr_data_cleaned
    if 'anpr_data' in globals():
        anpr_data_cleaned = anpr_data.dropna()
        messagebox.showinfo("Info", "Data Cleaned Successfully")
    else:
        messagebox.showwarning("Warning", "Load Data First")

# Function to transform data
def transform_data():
    global anpr_data_transformed
    if 'anpr_data_cleaned' in globals():
        anpr_data_transformed = anpr_data_cleaned.copy()
        anpr_data_transformed['bearing_category'] = anpr_data_transformed['bearing'] // 45
        messagebox.showinfo("Info", "Data Transformed Successfully")
    else:
        messagebox.showwarning("Warning", "Clean Data First")

# Function to train model
def train_model():
    global model
    if 'anpr_data_transformed' in globals():
        X = anpr_data_transformed[['bearing', 'duration']]
        y = anpr_data_transformed['bearing_category']
        model = RandomForestClassifier()
        model.fit(X, y)
        with open('rf_model.pkl', 'wb') as file:
            pickle.dump(model, file)
        messagebox.showinfo("Info", "Model Trained and Saved Successfully")
    else:
        messagebox.showwarning("Warning", "Transform Data First")

# Function to evaluate model
def evaluate_model():
    if 'model' in globals():
        if 'anpr_data_transformed' in globals():
            X = anpr_data_transformed[['bearing', 'duration']]
            y_true = anpr_data_transformed['bearing_category']
            y_pred = model.predict(X)
            accuracy = (y_true == y_pred).mean()
            messagebox.showinfo("Model Accuracy", f"Accuracy: {accuracy:.2f}")
        else:
            messagebox.showwarning("Warning", "Transform Data First")
    else:
        messagebox.showwarning("Warning", "Train Model First")

# Create GUI window
root = tk.Tk()
root.title("Tyrone's Vehicle Prediction Model")
root.geometry("400x300")

# Create buttons for each step
btn_load_data = tk.Button(root, text="Load Data", command=load_data)
btn_clean_data = tk.Button(root, text="Clean Data", command=clean_data)
btn_transform_data = tk.Button(root, text="Transform Data", command=transform_data)
btn_train_model = tk.Button(root, text="Train Model", command=train_model)
btn_evaluate_model = tk.Button(root, text="Evaluate Model", command=evaluate_model)

# Place buttons in the window
btn_load_data.pack(pady=10)
btn_clean_data.pack(pady=10)
btn_transform_data.pack(pady=10)
btn_train_model.pack(pady=10)
btn_evaluate_model.pack(pady=10)

# Run the GUI event loop
root.mainloop()