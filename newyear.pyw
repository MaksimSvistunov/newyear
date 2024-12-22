import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import random

# картинки
def get_ascii_art():
    art_list = [
        """
           *
          ***
         *****
        *******
       *********
      ***********
     *************
          |||||   
        """,
        """
                           _{}_
                         .'    '.
                        /_......_
               _ __ _ ."`        `".
              |      |    ______    
              |;     |_.-'o    o`-._/
              ||     |      V       |
              ||_ ,  |  `'----'`  /
              '-.` .-';'---.--.--';
                 ||   |       '.  
                _||_ /'-.____   ` ;
               /    )        |    | |`
               | _.'                
                ||         ()      
                ||               |
                 ||         ()         |_/
                 ||                    ;
            jgs  ||         ()        ' '.
               .'|| '.             -'     '-.
            .-'  ||     `"   "  `            `--.
        """,
        """
                 __
               _|==|_  
                ('')___/
            >--(`^^')
              (`^'^'`)
              `======'  ldb
        """,
        """
            __§§§§§§___________§§§§§§§
            §§§§___§§§_______§§§____§§§§
            __§§§§___§§§____§§§___§§§§
            ____§§§§_§§§§__§§§§_§§§§
            ______§§§§§§§§§§§§§§§§
            §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
            §§§§§__§§§§__§§§__§§§§_§§§§§§
            §__§§§§§§____§§§____§§§§§§__§
            §____________§§§____________§
            §____________§§§____________§
            §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
            §____________§§§____________§
            §____________§§§____________§
            §____________§§§____________§
            §____________§§§____________§
            §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
        """
    ]
    return random.choice(art_list)


#  функция случайного поздравления
def get_greeting(name):
    greetings = [
        f"🎄 С Новым Годом, {name}! 🎄\nПусть этот волшебный праздник принесет вам радость, тепло и незабываемые моменты!",
        f"✨ Здоровья и счастья в новом году, {name}! ✨\nПусть каждый день будет светлым и добрым, наполненным удачей и сюрпризами!",
        f"🌟 Успехов и процветания, {name}! 🌟\nНовых горизонтов, смелых идей и их воплощения!",
        f"💫 Радости и любви, {name}! 💫\nПусть в сердце царит гармония, в душе — свет, а в доме — уют.",
        f"🎉 Новых побед и свершений, {name}! 🎉\nПусть наступающий год станет временем новых открытий и ярких достижений!"
    ]
    return random.choice(greetings)


def on_greet_click():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Предупреждение", "Введите имя!")
        return
    ascii_art = get_ascii_art()
    greeting = get_greeting(name)
    output_text.set(f"{ascii_art}\n\n{greeting}")
    image_label.grid_forget()  # Убираем изображение, если оно было ранее
    output_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")  # Показываем текстовое поздравление


def on_special_click():
    special_greeting =  "Дорогой Матвей, чтобы твоя машина не ломалась,\nвсего самого хорошего и отличного настроения! 😊"

    # Создание изображения с помощью PIL
    try:
        image = Image.open('1.jpg')  # Открываем картинку
        draw = ImageDraw.Draw(image)  # Создаем объект для рисования на изображении

        # Преобразуем изображение в формат, который может отобразить tkinter
        img_tk = ImageTk.PhotoImage(image)
        
        output_text.set(special_greeting)
        output_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")  # Показываем текстовое поздравление

        # Отображаем изображение
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Сохраняем ссылку на изображение
        image_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)  # Показываем картинку

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


# Окно
root = tk.Tk()
root.title("Новогодние поздравления")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 500
window_height = 500

# Окно по центру
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

# устанавливаем размеры и позицию окна
root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

# разрешаем изменение размеров окна
root.resizable(True, True)

# Сетка
root.grid_rowconfigure(0, weight=0)  # Строка для полей ввода и кнопок
root.grid_rowconfigure(1, weight=0)  # Строка для кнопок
root.grid_rowconfigure(2, weight=1)  # Строка для вывода текста
root.grid_rowconfigure(3, weight=0)  # Строка для картинки
root.grid_columnconfigure(0, weight=1)  # Для всех колонок, чтобы занимали всю ширину
root.grid_columnconfigure(1, weight=1)

tk.Label(root, text="Введите ваше имя:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# кнопки
btn_greet = tk.Button(root, text="Поздравить", command=on_greet_click)
btn_greet.grid(row=1, column=0, padx=5, pady=5, sticky="w")

btn_special = tk.Button(root, text="отдельное поздравление для Матвея, «Secret Point»", command=on_special_click)
btn_special.grid(row=1, column=1, padx=5, pady=5, sticky="e")

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, justify="left", anchor="nw", font=("Courier", 10), wraplength=window_width-20)

image_label = tk.Label(root)

root.mainloop()
