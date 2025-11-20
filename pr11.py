import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Елютин Даниил Викторович")
root.geometry("600x400")

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')

tab3 = tk.Frame(tab_control)
tab_control.add(tab3, text='Текст')

tab_control.pack(expand=1, fill='both', padx=10, pady=10)

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                return
            result = num1 / num2
        else:
            result = "Неизвестная операция"
        
        result_label.config(text=str(result))
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

tk.Label(tab1, text="Первое число:").grid(row=0, column=0, padx=10, pady=10)
num1_entry = tk.Entry(tab1)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(tab1, text="Операция:").grid(row=1, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
operation_combo = ttk.Combobox(tab1, textvariable=operation_var, values=operations, state="readonly")
operation_combo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(tab1, text="Второе число:").grid(row=2, column=0, padx=10, pady=10)
num2_entry = tk.Entry(tab1)
num2_entry.grid(row=2, column=1, padx=10, pady=10)

calc_button = tk.Button(tab1, text="Вычислить", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=20)

tk.Label(tab1, text="Результат:").grid(row=4, column=0, padx=10, pady=10)
result_label = tk.Label(tab1, text="", bg="white", relief="sunken", width=20)
result_label.grid(row=4, column=1, padx=10, pady=10)

def show_selection():
    selected = []
    
    if var1.get():
        selected.append("Первый")
    if var2.get():
        selected.append("Второй")
    if var3.get():
        selected.append("Третий")
    
    if selected:
        messagebox.showinfo("Ваш выбор", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Ваш выбор", "Вы ничего не выбрали")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

cb1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
cb2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
cb3 = tk.Checkbutton(tab2, text="Третий", variable=var3)

cb1.pack(pady=10)
cb2.pack(pady=10)
cb3.pack(pady=10)

show_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
show_button.pack(pady=20)

def load_file():
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, content)
            messagebox.showinfo("Успех", "Файл успешно загружен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")

def clear_text():
    text_widget.delete(1.0, tk.END)

button_frame = tk.Frame(tab3)
button_frame.pack(pady=10)

load_button = tk.Button(button_frame, text="Загрузить файл", command=load_file)
load_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Очистить текст", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)


text_frame = tk.Frame(tab3)
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_widget = tk.Text(text_frame, wrap=tk.WORD, width=60, height=15)
scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


hint_label = tk.Label(tab3, text="Используйте кнопки выше для загрузки и очистки текста", 
                     fg="gray", font=("Arial", 10))
hint_label.pack(pady=5)


root.mainloop()