import csv
import json
import tkinter as tk
from tkinter import messagebox

# Step 1: Create an empty list called "sales_data"
sales_data = []

# Step 2: Open and convert the CSV file to JSON format
with open('SalesJan2009.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # Skip the header row

    for row in csv_reader:
        # Extracting data and cleaning up extra quote characters
        transaction_date = row[0]
        product = row[1]
        price = float(row[2])  # Convert price to float
        payment_type = row[3]
        name = row[4].strip('"')
        city = row[5].strip('"')
        state = row[6].strip('"')
        country = row[7].strip('"')

        # Create a dictionary for each line and append it to sales_data
        data_dict = {
            'Transaction_date': transaction_date,
            'Product': product,
            'Price': price,
            'Payment_Type': payment_type,
            'Name': name,
            'City': city,
            'State': state,
            'Country': country
        }
        sales_data.append(data_dict)

# Step 3: Save sales_data to a file called "transaction_data.json"
with open('transaction_data.json', 'w') as json_file:
    json.dump(sales_data, json_file, indent=4)

# Step 4: Create a user interface (UI)
root = tk.Tk()
root.title("Sales Data Converter")
root.geometry("400x200")
root.configure(bg="#006747")  # Wayne State University Green

def quit_program():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.quit()

quit_button = tk.Button(root, text="QUIT", command=quit_program)
quit_button.pack()

# Additional UI elements
# Example: Use of 'messagebox'
def show_message():
    messagebox.showinfo("Message", "Conversion and saving to JSON completed.")

message_button = tk.Button(root, text="Show Status Message", command=show_message)
message_button.pack()

root.mainloop()
