import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# Loading the trained model
model = joblib.load('obesity_predictor_model.pkl')

def predict_obesity():
    try:
        # Gathering inputs from the GUI application
        data = {
            'Age': float(age.get()),
            'Gender': gender.get(),
            'Height': float(height.get()),
            'Weight': float(weight.get()),
            'family_history_with_overweight': family_history_var.get(),
            'FAVC': favc_var.get(),
            'FCVC': float(fcvc.get()),
            'NCP': float(ncp.get()),
            'CAEC': caec_var.get(),
            'SMOKE': smoke_var.get(),
            'CH2O': float(ch2o.get()),
            'SCC': scc_var.get(),
            'FAF': float(faf.get()),
            'TUE': float(tue.get()),
            'CALC': calc_var.get(),
            'MTRANS': mtrans_var.get(),
        }
        df = pd.DataFrame([data])
        
        # Predicting obesity level using the trained model
        prediction = model.predict(df)[0]
        
        # Prediction result
        messagebox.showinfo("Prediction Result", f"The predicted obesity level is: {prediction}")
        
        # Saving the prediction to CSV file
        df['Prediction'] = prediction  
        output_filename = 'prediction_output.csv'
        df.to_csv(output_filename, index=False)  
        messagebox.showinfo("Export Success", f"The prediction has been successfully exported to {output_filename}.")
    
    except ValueError as e:
        messagebox.showerror("Input Error", f"Please check the inputs. Error: {e}")
    except Exception as e:
        messagebox.showerror("Prediction Error", f"An error occurred during prediction. Error: {e}")

# GUI
root = tk.Tk()
root.title("Obesity Prediction Application")
root.configure(bg='grey')  

# Styling for Combobox
style = ttk.Style()
style.theme_use('alt')
style.configure('TCombobox', fieldbackground="white", background="white", foreground="black")
style.configure('TLabel', background="grey", foreground="white")
style.configure('TButton', background="grey", foreground="white", font=('Calibri', 9))

# Styling for textbox
def create_labeled_entry(row, label_text):
    label = tk.Label(root, text=label_text, bg='grey', fg='black', anchor='w')
    label.grid(row=row, column=0, sticky='EW')
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, sticky='EW')
    return entry

def create_labeled_combobox(row, label_text, values):
    label = tk.Label(root, text=label_text, bg='grey', fg='black', anchor='w')
    label.grid(row=row, column=0, sticky='EW')
    var = tk.StringVar()
    combobox = ttk.Combobox(root, textvariable=var, values=values, style='TCombobox')
    combobox.grid(row=row, column=1, sticky='EW')
    return var


age = create_labeled_entry(0, "Age")
gender = create_labeled_combobox(1, "Gender", ('Male', 'Female'))
height = create_labeled_entry(2, "Height (cm)")
weight = create_labeled_entry(3, "Weight (kg)")
family_history_var = create_labeled_combobox(4, "Family History with Overweight", ('Yes', 'No'))
favc_var = create_labeled_combobox(5, "Frequent Consumption of High Caloric Food", ('Yes', 'No'))
fcvc = create_labeled_entry(6, "Frequent Consumption of Vegetables (No of meals)")
ncp = create_labeled_entry(7, "Number of Main Meals (Per day)")
caec_var = create_labeled_combobox(8, "Consumption of Food Between Meals", ('No', 'Sometimes', 'Frequently', 'Always'))
smoke_var = create_labeled_combobox(9, "Smoking Habit", ('Yes', 'No'))
ch2o = create_labeled_entry(10, "Consumption of Water (liters)")
scc_var = create_labeled_combobox(11, "Monitoring Calorie Consumption", ('Yes', 'No'))
faf = create_labeled_entry(12, "Frequency of Physical Activity (No of days)")
tue = create_labeled_entry(13, "Time Using Technology Devices (Hours per day)")
calc_var = create_labeled_combobox(14, "Consumption of Alcohol", ('No', 'Sometimes', 'Frequently', 'Always'))
mtrans_var = create_labeled_combobox(15, "Mode of Transportation", ('Automobile', 'Motorbike', 'Bike', 'Public_Transportation', 'Walking'))


predict_button = tk.Button(root, text="Predict The Result", command=predict_obesity, bg='black', fg='white')
predict_button.grid(row=16, column=0, columnspan=2, sticky='EW', pady=10)

root.mainloop()
