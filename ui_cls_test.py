import tkinter as tk
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Layout Example")
        self.layout_array = []
        # ------------------------------------------------------------------------
        self.frame1 = tk.Frame(self.master, bd=2, relief="solid", bg="blue")
        self.frame1.pack()

        self.frame2 = tk.Frame(self.master, bd=2, relief="solid", bg="red")
        self.frame2.pack()
        
        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------


        self.layout1_button = tk.Button(self.frame1, text="Layout 1", command=self.layout1)
        self.layout1_button.grid(row=0, column=0)
        # ------------------------------------------------------------------------
        self.layout2_button = tk.Button(self.frame1, text="Layout 2", command=self.layout2)
        self.layout2_button.grid(row=0, column=1)
        # ------------------------------------------------------------------------
        self.layout3_button = tk.Button(self.frame1, text="Layout 3", command=self.layout3)
        self.layout3_button.grid(row=0, column=2)
        # ------------------------------------------------------------------------
        self.layout4_button = tk.Button(self.frame1, text="Layout 4", command=self.layout4)
        self.layout4_button.grid(row=0, column=3)
        
        
        
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
    def layout1(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        layout1 = Layout1(self.frame2)
        self.layout_array.append(layout1)
# ------------------------------------------------------------------------
    def layout2(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        layout2 = Layout2(self.frame2)
        self.layout_array.append(layout2)
# ------------------------------------------------------------------------
    def layout3(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        layout3 = Layout3(self.frame2)
        self.layout_array.append(layout3)
# ------------------------------------------------------------------------
    def layout4(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        layout3 = Layout4(self.frame2)
        self.layout_array.append(layout3)
        
        
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
class Layout1:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0)
        self.frame2 = tk.Frame(self.master)
        self.frame2.grid(row=0, column=1)
        self.subgrid2 = tk.Frame(self.frame2)
        self.subgrid2.pack()
        self.num_fields = 1
        self.create_input_fields()
        self.button1 = tk.Button(self.frame1, text="Button 1", command=self.button1_callback)
        self.button1.pack()
        self.button2 = tk.Button(self.frame1, text="Button 2", command=self.button2_callback)
        self.button2.pack()
        self.button3 = tk.Button(self.frame1, text="Button 3", command=self.button3_callback)
        self.button3.pack()
        self.button4 = tk.Button(self.frame1, text="Button 4", command=self.button4_callback)
        self.button4.pack()

    def create_input_fields(self):
        for widget in self.subgrid2.winfo_children():
            widget.destroy()
        for i in range(self.num_fields):
            input_field = tk.Entry(self.subgrid2)
            input_field.pack()
        execute_button = tk.Button(self.subgrid2, text="Execute", command=self.execute_callback)
        execute_button.pack()

    def execute_callback(self):
        # Perform desired action
        print("executed")

    def button1_callback(self):
        self.num_fields = 1
        self.create_input_fields()

    def button2_callback(self):
        self.num_fields = 2
        self.create_input_fields()

    def button3_callback(self):
        self.num_fields = 3
        self.create_input_fields()

    def button4_callback(self):
        self.num_fields = 4
        self.create_input_fields()
# ------------------------------------------------------------------------
class Layout2:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0)
        self.frame2 = tk.Frame(self.master)
        self.frame2.grid(row=0, column=1)
        self.subgrid2 = tk.Frame(self.frame2)
        self.subgrid2.pack()
        self.num_fields = 1
        self.create_input_fields()
        self.button1 = tk.Button(self.frame1, text="Button 1", command=self.button1_callback)
        self.button1.pack()
        self.button2 = tk.Button(self.frame1, text="Button 2", command=self.button2_callback)
        self.button2.pack()
        self.button3 = tk.Button(self.frame1, text="Button 3", command=self.button3_callback)
        self.button3.pack()
        self.button4 = tk.Button(self.frame1, text="Button 4", command=self.button4_callback)
        self.button4.pack()

    def create_input_fields(self):
        for widget in self.subgrid2.winfo_children():
            widget.destroy()
        for i in range(self.num_fields):
            input_field = tk.Entry(self.subgrid2)
            input_field.pack()
        execute_button = tk.Button(self.subgrid2, text="Execute", command=self.execute_callback)
        execute_button.pack()

    def execute_callback(self):
        # Perform desired action
        print("executed")

    def button1_callback(self):
        self.num_fields = 1
        self.create_input_fields()

    def button2_callback(self):
        self.num_fields = 2
        self.create_input_fields()

    def button3_callback(self):
        self.num_fields = 3
        self.create_input_fields()

    def button4_callback(self):
        self.num_fields = 4
        self.create_input_fields()
# ------------------------------------------------------------------------
class Layout3:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0)
        self.frame2 = tk.Frame(self.master)
        self.frame2.grid(row=0, column=1)
        self.subgrid2 = tk.Frame(self.frame2)
        self.subgrid2.pack()
        self.num_fields = 1
        self.create_input_fields()
        self.button1 = tk.Button(self.frame1, text="Button 1", command=self.button1_callback)
        self.button1.pack()
        self.button2 = tk.Button(self.frame1, text="Button 2", command=self.button2_callback)
        self.button2.pack()
        self.button3 = tk.Button(self.frame1, text="Button 3", command=self.button3_callback)
        self.button3.pack()
        self.button4 = tk.Button(self.frame1, text="Button 4", command=self.button4_callback)
        self.button4.pack()

    def create_input_fields(self):
        for widget in self.subgrid2.winfo_children():
            widget.destroy()
        for i in range(self.num_fields):
            input_field = tk.Entry(self.subgrid2)
            input_field.pack()
        execute_button = tk.Button(self.subgrid2, text="Execute", command=self.execute_callback)
        execute_button.pack()

    def execute_callback(self):
        # Perform desired action
        print("executed")

    def button1_callback(self):
        self.num_fields = 1
        self.create_input_fields()

    def button2_callback(self):
        self.num_fields = 2
        self.create_input_fields()

    def button3_callback(self):
        self.num_fields = 3
        self.create_input_fields()

    def button4_callback(self):
        self.num_fields = 4
        self.create_input_fields()


class Layout4:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0)
        self.frame2 = tk.Frame(self.master)
        self.frame2.grid(row=0, column=1)
        self.subgrid2 = tk.Frame(self.frame2)
        self.subgrid2.pack()
        self.num_fields = 1
        self.create_input_fields()
        self.button1 = tk.Button(self.frame1, text="Button 1", command=self.button1_callback)
        self.button1.pack()
        self.button2 = tk.Button(self.frame1, text="Button 2", command=self.button2_callback)
        self.button2.pack()
        self.button3 = tk.Button(self.frame1, text="Button 3", command=self.button3_callback)
        self.button3.pack()
        self.button4 = tk.Button(self.frame1, text="Button 4", command=self.button4_callback)
        self.button4.pack()

    def create_input_fields(self):
        for widget in self.subgrid2.winfo_children():
            widget.destroy()
        for i in range(self.num_fields):
            input_field = tk.Entry(self.subgrid2)
            input_field.pack()
        execute_button = tk.Button(self.subgrid2, text="Execute", command=self.execute_callback)
        execute_button.pack()

    def execute_callback(self):
        # Perform desired action
        print("executed")

    def button1_callback(self):
        self.num_fields = 1
        self.create_input_fields()

    def button2_callback(self):
        self.num_fields = 2
        self.create_input_fields()

    def button3_callback(self):
        self.num_fields = 3
        self.create_input_fields()

    def button4_callback(self):
        self.num_fields = 4
        self.create_input_fields()


# ----------------------------
# ----------------------------
# ----------------------------
root = tk.Tk()
main_window = MainWindow(root)
root.mainloop()




# ------------------------------------------------------------------------
# class Layout4:
#     # def __init__(self, master):
#         # self.master = master
#         # self.button1 = tk.Button(self.master, text="Button 1", bg="blue")
#         # self.button1.pack()
#         # self.button2 = tk.Button(self.master, text="Button 2", bg="blue")
#         # self.button2.pack()
#         # self.button3 = tk.Button(self.master, text="Button 3", bg="blue")
#         # self.button3.pack()
#         # self.button4 = tk.Button(self.master, text="Button 4", bg="blue")
#         # self.button4.pack()
#     def layout4(self):
#         self.frame1.grid(row=0, column=0)
#         self.frame2.grid(row=0, column=1)
#         self.num_fields = 1
#         self.create_input_fields()

#     def create_input_fields(self):
#         for widget in self.subgrid2.winfo_children():
#             widget.destroy()
#         for i in range(self.num_fields):
#             input_field = tk.Entry(self.subgrid2)
#             input_field.pack()
#         execute_button = tk.Button(self.subgrid2, text="Execute", command=self.execute_callback)
#         execute_button.pack()

#     def execute_callback(self):
#         # Perform desired action

#     def button1(self):
#         self.num_fields = 1
#         self.create_input_fields()

#     self.layout1_button = tk.Button(self.frame1, text="Layout 1", command=self.button1)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------