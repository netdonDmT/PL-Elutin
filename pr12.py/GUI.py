import tkinter as tk
from tkinter import messagebox
from parser import get_repo_data

def parse_repository():
    repo_name = entry.get().strip()
    
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите название репозитория")
        return
    
    try:
        result = get_repo_data(repo_name)
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
        
        messagebox.showinfo("Успех", "Данные сохранены в файл github_repo_data.json")
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

window = tk.Tk()
window.title("Парсер GitHub репозиториев")
window.geometry("600x400")

label = tk.Label(window, text="Введите название репозитория (формат: владелец/репозиторий):")
label.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=5)
entry.insert(0, "CocoaPods/Specs")

button = tk.Button(window, text="Получить данные", command=parse_repository)
button.pack(pady=10)

result_text = tk.Text(window, height=15, width=70)
result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

window.mainloop()