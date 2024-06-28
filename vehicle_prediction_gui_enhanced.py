import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import joblib

# Function to load data
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = pd.read_csv(file_path)
        messagebox.showinfo("Data Load", "Data loaded successfully!")
        analyze_button.config(state=tk.NORMAL)
        evaluate_button.config(state=tk.NORMAL)

# Function to analyze data
def analyze_data():
    if data is not None:
        analysis_text.delete('1.0', tk.END)
        analysis_text.insert(tk.END, f"Data Head:\n{data.head()}\n\n")
        analysis_text.insert(tk.END, f"Data Info:\n{data.info()}\n\n")
        analysis_text.insert(tk.END, f"Data Description:\n{data.describe()}\n\n")

# Function to evaluate model
def evaluate_model():
    try:
        model = joblib.load("rf_model.pkl")
        features = data.drop('bearing_category', axis=1)
        labels = data['bearing_category']
        accuracy = model.score(features, labels)
        evaluation_text.delete('1.0', tk.END)
        evaluation_text.insert(tk.END, f"Model Accuracy: {accuracy:.2f}\n\n")
        evaluation_text.insert(tk.END, "Classification Report:\n")
        # Add code here to display the full classification report if needed
    except Exception as e:
        messagebox.showerror("Model Evaluation", f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("BAPU - Behavior Analysis and Prediction Using ANPR")
root.geometry("800x600")

# Load the logo image
logo_path = "C:\\Users\\tfel4\\OneDrive\\Documents\\2024\\WAPOL Hackathon\\BAPU logo.webp"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((200, 200), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a style for the notebook (tabs)
style = ttk.Style()
style.configure('TNotebook.Tab', font=('Arial', '12', 'bold'), padding=[10, 5])
style.configure('TButton', font=('Arial', '12', 'bold'), background="#4CAF50", foreground="white", padding=10)
style.map('TButton', background=[('active', '#45a049')])

# Create the notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=20, expand=True)

# Create frames for each tab
tab1 = ttk.Frame(notebook, width=800, height=400)
tab2 = ttk.Frame(notebook, width=800, height=400)
tab3 = ttk.Frame(notebook, width=800, height=400)

tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)

# Add tabs to the notebook
notebook.add(tab1, text='Home')
notebook.add(tab2, text='Data Analysis')
notebook.add(tab3, text='Model Evaluation')

# Home Tab
home_label = ttk.Label(tab1, text="Welcome to BAPU", font=('Arial', 24, 'bold'))
home_label.pack(pady=20)

logo_label = tk.Label(tab1, image=logo_photo)
logo_label.pack(pady=10)

home_text = tk.Text(tab1, height=10, width=60, font=('Arial', 14))
home_text.pack(pady=20)
home_text.insert('1.0', "BAPU (Behavior Analysis and Prediction Using ANPR) is an innovative solution for predicting the location of vehicles of interest using Automatic Number Plate Recognition (ANPR) data.")

# Data Analysis Tab
analysis_label = ttk.Label(tab2, text="Data Analysis", font=('Arial', 20, 'bold'))
analysis_label.pack(pady=20)

analysis_text = tk.Text(tab2, height=15, width=80, font=('Arial', 14))
analysis_text.pack(pady=20)

analyze_button = ttk.Button(tab2, text="Analyze Data", command=analyze_data)
analyze_button.pack(pady=10)
analyze_button.config(state=tk.DISABLED)

# Model Evaluation Tab
evaluation_label = ttk.Label(tab3, text="Model Evaluation", font=('Arial', 20, 'bold'))
evaluation_label.pack(pady=20)

evaluation_text = tk.Text(tab3, height=15, width=80, font=('Arial', 14))
evaluation_text.pack(pady=20)

evaluate_button = ttk.Button(tab3, text="Evaluate Model", command=evaluate_model)
evaluate_button.pack(pady=10)
evaluate_button.config(state=tk.DISABLED)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load Data", command=load_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Global variable to store the loaded data
data = None

# Run the application
root.mainloop()