import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            result_label.config(text=f"{temperature}°C is {celsius_to_fahrenheit(temperature):.2f}°F")
        elif var.get() == 2:  # Fahrenheit to Celsius
            result_label.config(text=f"{temperature}°F is {fahrenheit_to_celsius(temperature):.2f}°C")
        else:
            result_label.config(text="Please select a conversion option.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Entry for user input
entry_label = tk.Label(window, text="Enter Temperature:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Radio buttons for conversion options
var = tk.IntVar()
var.set(1)  # Default to Celsius to Fahrenheit

radio_celsius = tk.Radiobutton(window, text="Celsius to Fahrenheit", variable=var, value=1)
radio_celsius.pack()
radio_fahrenheit = tk.Radiobutton(window, text="Fahrenheit to Celsius", variable=var, value=2)
radio_fahrenheit.pack()

# Button to trigger conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Label to display result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
