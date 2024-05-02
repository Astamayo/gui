import tkinter as tk
from tkinter import messagebox

def connect():
    selected_port = port_var.get()
    if selected_port:
        messagebox.showinfo("Connection", f"Connecting to {selected_port}...")
        # Add your connection logic here

        # Create entry field for barcode
        barcode_label.pack()
        barcode_entry.pack()
        save_button.pack()
    else:
        messagebox.showwarning("Error", "Please select a port first.")

def save_barcode():
    barcode = barcode_var.get()
    if barcode:
        messagebox.showinfo("Barcode", f"Barcode '{barcode}' saved.")
        # Add code to save the barcode or process it further
        # For now, just clear the entry field and hide the save button
        barcode_var.set("")
        barcode_entry.pack_forget()
        save_button.pack_forget()
        barcode_label.pack_forget()
    else:
        messagebox.showwarning("Error", "Please enter a barcode.")

def save_and_exit():
    root.destroy()

root = tk.Tk()
root.title("Port Selection")

# Dropdown for port selection
ports = ["COM1", "COM2"]  # Example ports
port_var = tk.StringVar(root)
port_var.set(ports[0])  # Set default value
port_dropdown = tk.OptionMenu(root, port_var, *ports)
port_dropdown.pack()

# Connect button
connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

# Barcode entry field and save button (initially hidden)
barcode_var = tk.StringVar(root)
barcode_label = tk.Label(root, text="Enter Barcode:")
barcode_entry = tk.Entry(root, textvariable=barcode_var)
save_button = tk.Button(root, text="Save Barcode", command=save_barcode)

# Save and Exit button
save_exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)
save_exit_button.pack()

root.mainloop()