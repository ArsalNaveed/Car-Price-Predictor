import tkinter as tk    #library used for GUI
from tkinter import font  #used to define custom fonts for the GUI elements
from tkinter.font import Font   #used to define custom fonts for the GUI elements
from sklearn.linear_model import LinearRegression     #used for performing linear regression analysis.

# Training the model with data (car age || number of km's driver || accidents)
car_data = [
    [3, 50000, 0],   # Car 1: age=3 years, kms=50000, accidents=0
    [5, 80000, 2],   # Car 2: age=5 years, kms=80000, accidents=2
    [2, 30000, 1],   # Car 3: age=2 years, kms=30000, accidents=1
    [6, 100000, 3],  # Car 4: age=6 years, kms=100000, accidents=3
    [4, 60000, 1],   # Car 5: age=4 years, kms=60000, accidents=1
    [2, 40000, 0],   # Car 6: age=2 years, kms=40000, accidents=0
    [1, 20000, 0],   # Car 7: age=1 year, kms=20000, accidents=0
    [5, 90000, 2]    # Car 8: age=5 years, kms=90000, accidents=2
]

car_cost = [2000000, 1800000, 2200000, 1600000, 1900000, 2300000, 2500000, 1700000]  # Cost of the cars above in rupees

model = LinearRegression()
model.fit(car_data, car_cost)

def predict_car_price():                            # function is defined.
    car_age = int(age_entry.get())                  #user inputs
    kms_driven = int(kms_entry.get())
    accidents = int(accidents_entry.get())

    car_to_predict = [[car_age, kms_driven, accidents]]     #The car details are stored in list
    predicted_cost = model.predict(car_to_predict)

    result_label.config(text="Predicted cost of the used car: PKR %.2f" % predicted_cost[0])    #The predicted car price is displayed in the GUI


# Create the GUI window
window = tk.Tk()
window.title("Car Price Prediction (PKR)")
window.geometry("600x400")

# Create custom font
custom_font = font.Font(family="Helvetica", size=14)

# Heading
heading_label = tk.Label(window, text="Welcome to Car Price Predictor", font=custom_font, pady=10, underline=True)
heading_label.config(font=("bold underline", custom_font.cget("size")))  # Set the label text to bold and underline
heading_label.pack()

# Create input labels and entry fields
age_label = tk.Label(window, text="Car Age (in years):", font=custom_font)
age_label.pack()
age_entry = tk.Entry(window, font=custom_font)
age_entry.pack()

kms_label = tk.Label(window, text="Kilometers Driven:", font=custom_font)
kms_label.pack()
kms_entry = tk.Entry(window, font=custom_font)
kms_entry.pack()

accidents_label = tk.Label(window, text="Number of Accidents:", font=custom_font)
accidents_label.pack()
accidents_entry = tk.Entry(window, font=custom_font)
accidents_entry.pack()

predict_button = tk.Button(window, text="Predict", command=predict_car_price, font=custom_font)
predict_button.pack()

result_label = tk.Label(window, text="", font=custom_font, pady=10)
result_label.config(font=("bold", custom_font.cget("size")))  # Set the label text to bold
result_label.pack()

window.mainloop()
