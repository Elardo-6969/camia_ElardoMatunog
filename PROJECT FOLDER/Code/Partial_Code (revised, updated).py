import tkinter as tk
import datetime as dt
from tkinter import ttk
import tkinter.font as tkfont
import os.path

#CREATE INPUT FILE FOR HISTORY

file=os.path.isfile("input.txt")

if file==False:
    with open("input.txt", "x") as f:
        f.close()

#SUBMIT FUNCTION FOR USER TO INPUT PURCHASE; WILL INPUT THE DATA TO INPUT.TXT
#NOW WITH INPUT VALIDATION; WRONG INPUT WILL RESULT IN A NOTIFICATION (TOPLEVEL WIDGET)

def submit():
    file=os.path.isfile("balance.txt")

    if file==False:
        info_popup("balance_error_a")
    else:
        with open("balance.txt", "r") as file:
            balance=float(file.read())
        quantity=quan.get()
        try:
            quantity=int(quantity)
            if quantity < 1:
                info_popup("quant_error_a")
            units=unit.get()
            description=desc.get().replace(" ", "-")
            price=cost.get()
            try:
                price=float(price)
                if price < 0:
                    info_popup("price_error_a")
                else:
                    date=dt.datetime.now().strftime("%B-%d-%Y")
                    totalcost=float(int(quantity)*float(price))
                    category=selected.get()
                    #CHATGPT TOLD ME TO ADD THIS WHEN I WAS DEBUGGING, TS IS FOR THE ALTERNATING COLORS OF THE ROWS
                    row_count = len(table.get_children())

                    if row_count % 2 == 0:
                        table.insert('', tk.END, values=(quantity, units, description, price, totalcost, category, date), tags=('evenrow',))
                    else:
                        table.insert('', tk.END, values=(quantity, units, description, price, totalcost, category, date), tags=('oddrow',)) #it ends here
                     
                    with open("input.txt", "a") as file:
                        file.write(f"{quantity} {units} {description} {price} {totalcost} {category} {date}\n")
                    
                    with open("balance.txt", "w") as file:
                        file.write(str(balance-totalcost))
                        balance_label=tk.Label(app, text=f"Balance: {balance-totalcost}                   ", pady=20, bg=bg_color, fg=dark_green, font=("Arial", 10, "bold"))
                        balance_label.place(x=500, y=105)
                    desc.delete(0, tk.END)
                    cost.delete(0, tk.END)
                    quan.delete(0, tk.END)
                    unit.delete(0, tk.END)
                    selected.set(value="Category")
            except ValueError:
                info_popup("price_error_b")
        except ValueError:
            info_popup("quant_error_b")

#DELETE FUNCTION MADE BY CHATGPT

def delete_item():
    selected = table.selection()
    print(selected)
    if not selected:
        return

    # Get index of selected row
    item = selected[0]
    print(item)
    row_index = table.index(item)
    print(row_index)

    # Remove from Treeview
    table.delete(item)

    # Remove the same line from the file
    with open("input.txt", "r") as f:
        lines = f.readlines()

    if row_index < len(lines):
        del lines[row_index]

    with open("input.txt", "w") as f:
        f.writelines(lines)

def confirm_delete():
    global conf
    conf=tk.Toplevel(app)
    conf.geometry("300x150")

    conf_label=tk.Label(conf, text="Are you sure that you want to\nDELETE ALL of your purchase history?",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
    conf_label.place(x=30, y=30)
    
    button_style = {
    "bg": primary_green,
    "fg": "white",
    "activebackground": dark_green,
    "activeforeground": "white",
    "font": ("Arial", 10, "bold"),
    "bd": 0,
    "padx": 3,
    "pady": 3
    }
    
    conf_yes=tk.Button(conf, text="yes", command=lambda: choice_del("yes"), **button_style)
    conf_yes.place(x=110, y=70)

    conf_no=tk.Button(conf, text="no", command=lambda: choice_del("no"), **button_style)
    conf_no.place(x=160, y=70)

#DELETES EVERYTHING IN THE TABLE AND FILE WHEN CLICKED YES; OOTHERWISE JUST DESTROY THE WIDGET

def choice_del(option):
    conf.destroy()

    if option=="yes":
        with open("input.txt", "w") as file:
            file.write("")
        for item in table.get_children():
            table.delete(item)

#INPUT VALIDATION MADE BY CHATGPT HOPEFULLY THATS ALL

def balance_get():
    global balance
    
    try:
        balance=balance_entry.get()
        balance=float(balance)
        if balance <= 0:
            info_popup("balance_error_c")
        else:
            with open("balance.txt", "x") as f:
                f.close()
            with open("balance.txt", "w") as f:
                f.write(str(balance))
            balance_label=tk.Label(app, text=f"Balance: {balance}                         ", pady=20,
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
            balance_label.place(x=500, y=25)
            add_balance=tk.Button(app, text="Add Balance", command=addBalance,
                          bg=accent_yellow, fg=dark_green,
                          font=("Arial", 10, "bold"),
                          bd=0)
            add_balance.place(x=500, y=190)
    except ValueError:
        info_popup("balance_error_b")
    
#ADD BALANCE WIDGET

def addBalance():
    global addBalance_Widget
    global addBalance_Entry
    addBalance_Widget=tk.Toplevel(app)
    addBalance_Widget.geometry("350x150")

    addBalance_Label=tk.Label(addBalance_Widget, text="Enter balance to add:",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
    addBalance_Label.place(x=50, y=50)

    addBalance_Entry=tk.Entry(addBalance_Widget)
    addBalance_Entry.place(x=200, y=50)

    addBalance_Submit=tk.Button(addBalance_Widget, text="Add", command=addBalance_Get, **button_style)
    addBalance_Submit.place(x=50, y=80)

#FUNTION TO GET THE BALANCE IN THE "ADD BALANCE" TOPLEVEL OBJECT SINCE THERES
#NO WAY TO MAKE A LAMBDA FUNCTION DO VARIABLE ASSIGNMENTS

def addBalance_Get():
    with open("balance.txt", "r") as file:
        balance=float(file.read())
    try:
        getBalance=float(addBalance_Entry.get())
        with open("balance.txt", "w") as file:
            balance+=getBalance
            file.write(str(balance))
            balance_label=tk.Label(app, text=f"Balance: {balance}                                         ", pady=20,
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
            balance_label.place(x=500, y=25)
        addBalance_Widget.destroy()
        print(getBalance)
    except ValueError:
        info_popup("balance_error_b")

#NOTIFY THE USER IF THERE HAS BEEN AN ERROR IN THEIR INPUT

def info_popup(type):
    global info_window
    info_window=tk.Toplevel(app)
    if type=="balance_error_a":
        info_label=tk.Label(info_window, text="Enter balance!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="balance_error_b":
        info_label=tk.Label(info_window, text="Balance must be a number!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="balance_error_c":
        info_label=tk.Label(info_window, text="Balance must be a number greater than 0!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="quant_error_a":
        info_label=tk.Label(info_window, text="Quantity must be a number greater than zero!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="quant_error_b":
        info_label=tk.Label(info_window, text="Quantity must be a number!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="price_error_a":
        info_label=tk.Label(info_window, text="Price must be a number greater than zero!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    if type=="price_error_b":
        info_label=tk.Label(info_window, text="Price must be a number!",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
        info_label.pack()
    info_ok=tk.Button(info_window, text="OK", command=lambda: info_window.destroy(), **button_style)
    info_ok.pack()

def summary():
    global summary_widget
    summary_widget=tk.Toplevel(app)
    sum_ask=tk.Label(summary_widget, text="What way would you like your\nexpenses be summarized?",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
    sum_ask.pack()

    sum_category_btm=tk.Button(summary_widget, text="Category", command=sum_cat).pack()
    sum_category_btm=tk.Button(summary_widget, text="Months", command=sum_month).pack()
    
def sum_cat():   
    #INITIALIZE VARIABLES FOR SUMMARY
    global total_food_cost
    global total_toiletries_cost
    global total_electronics_cost
    global total_misc_cost
    global total_clothing_cost
    global total_school_cost
    global total_transp_cost
    #RESET VAR EVERY DECLARATION OF FUNCTION
    total_food_cost=0.0
    total_toiletries_cost=0.0
    total_electronics_cost=0.0
    total_misc_cost=0.0
    total_clothing_cost=0.0
    total_school_cost=0.0
    total_transp_cost=0.0
    summary_widget.destroy()
    with open("input.txt", "r") as file:
        for line in file:
            parts=line.split()
            category=parts[5]
            totalcost=float(parts[4])
            if category=="Food":
                total_food_cost+=totalcost
            if category=="Toiletries":
                total_toiletries_cost+=totalcost
            if category=="Electronics":
                total_electronics_cost+=totalcost
            if category=="Miscellaneous":
                total_misc_cost+=totalcost
            if category=="Clothing":
                total_clothing_cost+=totalcost
            if category=="School":
                total_school_cost+=totalcost
            if category=="Transportation":
                total_transp_cost+=totalcost
        print(total_food_cost)
    sum_cat_win=tk.Toplevel(app)
    sum_cat_tab=ttk.Treeview(sum_cat_win, columns=('category', 'totals'), show="headings")
    sum_cat_tab.heading('category', text="Categories")
    sum_cat_tab.heading('totals', text="Total in Each Category")
    sum_cat_tab.insert(parent='', index=tk.END, values=("Food", total_food_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("Toiletries", total_toiletries_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("Electronics", total_electronics_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("School", total_school_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("Transport", total_transp_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("Clothing", total_clothing_cost))
    sum_cat_tab.insert(parent='', index=tk.END, values=("Miscellaneous", total_misc_cost))
        
    sum_cat_tab.pack()

def sum_month():
    global jan_cost
    global feb_cost
    global mar_cost
    global apr_cost
    global may_cost
    global jun_cost
    global jul_cost
    global aug_cost
    global sep_cost
    global oct_cost
    global nov_cost
    global dec_cost
    summary_widget.destroy()
    sum_mon_win=tk.Toplevel(app)
    jan_cost=0.0
    feb_cost=0.0
    mar_cost=0.0
    apr_cost=0.0
    may_cost=0.0
    jun_cost=0.0
    jul_cost=0.0
    aug_cost=0.0
    sep_cost=0.0
    oct_cost=0.0
    nov_cost=0.0
    dec_cost=0.0
    with open("input.txt", "r") as f:
        for line in f:
            parts=line.split()
            totalcost=float(parts[4])
            date=parts[6].replace("-", " ")
            date=date.split()
            month=date[0]
            if month=="January":
                jan_cost+=totalcost
            if month=="February":
                feb_cost+=totalcost
            if month=="March":
                mar_cost+=totalcost
            if month=="April":
                apr_cost+=totalcost
            if month=="May":
                may_cost+=totalcost
            if month=="June":
                jun_cost+=totalcost
            if month=="July":
                jul_cost+=totalcost
            if month=="August":
                aug_cost+=totalcost
            if month=="September":
                sep_cost+=totalcost
            if month=="October":
                oct_cost+=totalcost
            if month=="November":
                nov_cost+=totalcost
            if month=="December":
                dec_cost+=totalcost
    sum_mon_tab=ttk.Treeview(sum_mon_win, columns=('Months', 'Total Cost'), show="headings")
    sum_mon_tab.heading("Months", text="Months")
    sum_mon_tab.heading("Total Cost", text="Total")
    sum_mon_tab.insert(parent='', index=tk.END, values=("January", jan_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("February", feb_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("March", mar_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("April", apr_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("May", may_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("June", jun_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("July", jul_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("August", aug_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("September", sep_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("October", oct_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("November", nov_cost))
    sum_mon_tab.insert(parent='', index=tk.END, values=("December", dec_cost))
    sum_mon_tab.pack()

app = tk.Tk()

bg_color = "#F6FFE0"      
primary_green = "#4CAF50"
accent_yellow = "#FFD54F"
dark_green = "#2E7D32"

app.configure(bg=bg_color)

title = tk.Label(app,
    text="🌿 Budget Tracker 💛",
    bg=primary_green,
    fg="white",
    font=("Arial", 18, "bold"),
    pady=10
)
title.pack(fill="x")

#ADD EXPENSE

quanlabel = tk.Label(app, text="Purchase Quantity:",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
quanlabel.place(x=50, y=70)

quan=tk.Entry(app)
quan.place(x=200, y=70)

unitlabel = tk.Label(app, text="Purchase Unit (e.g. box):",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 9, "bold"))
unitlabel.place(x=50, y=110)

unit=tk.Entry(app)
unit.place(x=200, y=110)

desclabel = tk.Label(app, text="Purchase Description:",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
desclabel.place(x=50, y=150)

desc=tk.Entry(app)
desc.place(x=200, y=150)

costlabel = tk.Label(app, text="Unit Cost (₱): ",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
costlabel.place(x=50, y=190)

cost=tk.Entry(app)
cost.place(x=200, y=190)

catlabel = tk.Label(app, text="Category:",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
catlabel.place(x=50, y=230)

category=['Food', 'Toiletries', 'Electronics', 'School', 'Miscellaneous', 'Clothing', 'Transportation']

selected=tk.StringVar(value='Category')

tk.OptionMenu(app, selected, *category).place(x=200, y=230)

#submit=Button(app, text="Submit", command=lambda: lbl.config(text=selected.get())).pack()

#lbl=Label(app, text="")
#lbl.pack()

button_style = {
    "bg": primary_green,
    "fg": "white",
    "activebackground": dark_green,
    "activeforeground": "white",
    "font": ("Arial", 10, "bold"),
    "bd": 0,
    "padx": 10,
    "pady": 5
}

button=tk.Button(app, text="Submit", command=submit, **button_style)
button.place(x=50, y=270)

#HISTORY

button = tk.Button(app, text="Delete Selected", command=delete_item,
                          bg=accent_yellow, fg=dark_green,
                          font=("Arial", 10, "bold"),
                          bd=0, padx=5, pady=5)
button.place(x=170, y=270)

button = tk.Button(app, text="Delete All", command=confirm_delete,
                          bg=accent_yellow, fg=dark_green,
                          font=("Arial", 10, "bold"),
                          bd=0, padx=5, pady=5)
button.place(x=300, y=270)

table=ttk.Treeview(app, columns=('pieces', 'unit', 'description', 'unit price', 'total','category', 'date'), show="headings")
table.heading('pieces', text="🔢 Quantity in pcs")
table.heading('unit', text="💲 Unit (e.g. box)")
table.heading('description', text="📝 Description")
table.heading('unit price', text="📈 Price/Unit")
table.heading('total', text="💰 Total Price")
table.heading('category', text="🛒 Category")
table.heading('date', text="🗓 Date Entered")
table.place(x=50, y=340, width=1150, height=300)

table.tag_configure('oddrow', background="#F1F8E9")
table.tag_configure('evenrow', background="#FFFFFF")

table.column('pieces', width=140)
table.column('unit', width=140)
table.column('description', width=200)
table.column('unit price', width=140)
table.column('total', width=140)
table.column('category', width=150)
table.column('date', width=170)

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
    background="#FFFFFF",
    foreground="black",
    rowheight=25,
    fieldbackground="#FFFFFF"
)

style.configure("Treeview.Heading",
    background=primary_green,
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=(10, 8)   
)

count = 0

with open("input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        if count % 2 == 0:
            table.insert('', tk.END,
                         values=(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]),
                         tags=('evenrow',))
        else:
            table.insert('', tk.END,
                         values=(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]),
                         tags=('oddrow',))

        count += 1

#BALANCE

file=os.path.isfile("balance.txt")

if file==False:

    balance_label=tk.Label(app, text="Enter balance:",
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
    balance_label.place(x=500, y=65)

    balance_entry=tk.Entry(app)
    balance_entry.place(x=600, y=70)

    balance_button=tk.Button(app, text="Submit", command=balance_get, **button_style)
    balance_button.place(x=750, y=69)

else:

    with open("balance.txt", "r") as f:
        balance_inFile=f.read()
    balance_label = tk.Label(app, text=f"  Balance: {balance_inFile}                                   ", pady=15,
                     bg=bg_color, fg=dark_green,
                     font=("Arial", 10, "bold"))
    balance_label.place(x=500, y=105)

    #ADD BALANCE

    add_balance = tk.Button(app, text="Add Balance", command=addBalance,
                          bg=accent_yellow, fg=dark_green,
                          font=("Arial", 10, "bold"),
                          bd=0, padx=5, pady=5)
    add_balance.place(x=500, y=270)

#SUMMARIZE EXPENSES

summary_btn = tk.Button(app, text="Summary of Expenses", command=summary,
                          bg=accent_yellow, fg=dark_green,
                          font=("Arial", 10, "bold"),
                          bd=0, padx=5, pady=5)
summary_btn.place(x=800, y=270)

#RUN APP

app.title("A&M Budget Tracker")
app.geometry('1920x1080')
app.mainloop()
