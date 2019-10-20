import math
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk   
from tkinter import messagebox
import thermal_conductivity as tc
import matplotlib.pyplot as plt


class GUI(tk.Frame):
    active_color_text = 'black'
    active_color = '#378ff6'
    button_color = '#0b1233'
    text_button = '#cdcdf0'
    back_color = '#e9e8ea'
    text_color = 'black'
    font = 'Verdana 14'
    width_entry = 6

    def __init__(self, root):
        super().__init__(root)
        self.main_window()

    def main_window(self):
        title_lable = tk.Label(root, text="Введите значения", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
        title_lable.grid(row = 0, column = 1, padx = 5, pady = 5)

        length_lable = tk.Label(root, text="Введите длину (м):", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        length_lable.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.length_input = tk.Entry(root, width = self.width_entry, font = self.font, bg = 'white', fg = self.text_color)
        self.length_input.grid(row = 1, column = 1, padx = 5, pady = 5)

        #input t_left
        t_left_lable = tk.Label(root, text="Введите температуру на левом крае:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        t_left_lable.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.t_left_input = tk.Entry(root, width = self.width_entry, bg = 'white', font = self.font, fg = self.text_color)
        self.t_left_input.grid(row = 2, column = 1, padx = 5, pady = 5)

        #input t_right
        t_right_lable = tk.Label(root, text="Введите температуру на правом крае:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        t_right_lable.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.t_right_input = tk.Entry(root, width = self.width_entry, font = self.font, bg = 'white', fg = self.text_color)
        self.t_right_input.grid(row = 3, column = 1, padx = 5, pady = 5)

        #input time
        time_lable = tk.Label(root, text="Введите время:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        time_lable.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.time_input = tk.Entry(root, width = self.width_entry, font = self.font, bg = 'white', fg = self.text_color)
        self.time_input.grid(row = 4, column = 1, padx = 5, pady = 5)

        #input count_N
        count_N_lable = tk.Label(root, text="Количество интервалов:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        count_N_lable.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.count_N_input = tk.Entry(root, width = self.width_entry, font = self.font, bg = 'white', fg = self.text_color)
        self.count_N_input.grid(row = 5, column = 1, padx = 5, pady = 5)
        
        #input T0
        start_t_lable = tk.Label(root, text="Введите начальную температуру:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        start_t_lable.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.start_t_input = tk.Entry(root, width = self.width_entry, font = self.font, bg = 'white', fg = self.text_color)
        self.start_t_input.grid(row = 6, column = 1, padx = 5, pady = 5)
        
        #material combo
        material_lable = tk.Label(root, text="Выберите материал:", bg = self.back_color,
                                fg = self.text_color, font = self.font)
        material_lable.grid(row = 7, column = 0, padx = 5, pady = 5)
        self.material_combo = ttk.Combobox(root, font = self.font, width = self.width_entry)
        self.material_combo['values'] = ('Гетинакс', 'Олово')
        self.material_combo.grid(row = 7, column = 1, padx = 5, pady = 5)

        fdm_cal_button = tk.Button(root, text = 'Вычислить по МКР', font = self.font, activebackground = self.active_color,
                                command = lambda: self.fdm_cal(), bg = 'green', fg = 'white',
                                activeforeground = self.active_color_text, bd=0, compound = tk.TOP)
        fdm_cal_button.grid(row = 8, column = 0, ipadx = 50, ipady=10 , padx = 5, pady = 5)
        
        accept_button = tk.Button(root, text = 'Вычислить по МКЭ', font = self.font, activebackground = self.active_color,
                                command = lambda: self.fdm_cal(), bg = self.button_color, fg = self.text_button,
                                activeforeground = self.active_color_text, bd=0, compound = tk.TOP)
        accept_button.grid(row = 8, column = 1, ipadx = 50, ipady=10 , padx = 5, pady = 5)

    def choice_material(self, material):
        if  material == 'Гетинакс':
            return 1350, 1400
        elif material == 'Медь':
            return 8930, 385
        else:
            return 7800, 460

    def fdm_cal(self):
        try:
            L = float(self.length_input.get())
            T_left = int(self.t_left_input.get())
            T_right = int(self.t_right_input.get())
            T0 = int(self.start_t_input.get())
            time = int(self.time_input.get())
            N = int(self.count_N_input.get())
            ro, c = self.choice_material(self.material_combo.get())
            
            thermal_conductivity = tc.ThermalConductivity(L=L, T_left=T_left, T_right=T_right, t=time,
                                        N = N, T0=T0, Ro=ro, c=c)            
            T, x = thermal_conductivity.FDM()

            fig = plt.figure()
            plt.plot(x, T)
            plt.show()
        except:
            messagebox.showerror('Ошибка','Были некорректно  введены значения.')
        #self.exit()
        

    def check(self):
        pass

    def input_window(self):
        child = self.ChildWindow([self.active_color_text, self.active_color,
                                self.button_color, self.back_color, self.text_color])
        self.data = child.data

    class ChildWindow(tk.Toplevel):
        active_color_text = None
        active_color = None
        button_color = None
        back_color = None
        text_color = None
        data = None
        font = 'Verdana 14'

        def __init__(self, colors):
            super().__init__()
            self.active_color_text = colors[0]
            self.active_color = colors[1]
            self.button_color = colors[2]
            self.back_color = colors[3]
            self.text_color = colors[4]
            self.read_window()

        def read_window(self):
            for widget in self.winfo_children():
                widget.destroy()
            
            self.title('Ввод исходных данных')
            self.geometry('700x370+345+90')
            self.resizable(False, False)
            self.config(bg = self.back_color)
            self.grab_set()
            self.focus_set()

            title_lable = tk.Label(self, text="Введите значения", bg = self.back_color,
                                    fg = self.text_color, font = "Arial 16")
            title_lable.grid(row = 0, column = 1, padx = 5, pady = 5)

            length_lable = tk.Label(self, text="Введите длину (м):", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            length_lable.grid(row = 1, column = 0, padx = 5, pady = 5)
            self.length_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.length_input.grid(row = 1, column = 1, padx = 5, pady = 5)

            #input t_left
            t_left_lable = tk.Label(self, text="Введите температуру на левом крае:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            t_left_lable.grid(row = 2, column = 0, padx = 5, pady = 5)
            self.t_left_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.t_left_input.grid(row = 2, column = 1, padx = 5, pady = 5)

            #input t_right
            t_right_lable = tk.Label(self, text="Введите температуру на правом крае:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            t_right_lable.grid(row = 3, column = 0, padx = 5, pady = 5)
            self.t_right_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.t_right_input.grid(row = 3, column = 1, padx = 5, pady = 5)

            #input time
            time_lable = tk.Label(self, text="Введите время:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            time_lable.grid(row = 4, column = 0, padx = 5, pady = 5)
            self.time_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.time_input.grid(row = 4, column = 1, padx = 5, pady = 5)

            #input count_N
            count_N_lable = tk.Label(self, text="Количество интервалов:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            count_N_lable.grid(row = 5, column = 0, padx = 5, pady = 5)
            self.count_N_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.count_N_input.grid(row = 5, column = 1, padx = 5, pady = 5)
            
            #input T0
            start_t_lable = tk.Label(self, text="Введите начальную температуру:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            start_t_lable.grid(row = 6, column = 0, padx = 5, pady = 5)
            self.start_t_input = tk.Entry(self, width = self.width_entry, bg = 'white', fg = self.text_color)
            self.start_t_input.grid(row = 6, column = 1, padx = 5, pady = 5)
            
            #material combo
            material_lable = tk.Label(self, text="Выберите материал:", bg = self.back_color,
                                    fg = self.text_color, font = self.font)
            material_lable.grid(row = 7, column = 0, padx = 5, pady = 5)
            self.material_combo = ttk.Combobox(self)
            self.material_combo['values'] = ('Метал', 'Олово')
            self.material_combo.grid(row = 7, column = 1, padx = 5, pady = 5)

            accept_button = tk.Button(self, text = 'Ввести данные', font = "Arial 12", activebackground = self.active_color,
                                  command = lambda: self.accept(), bg = 'green', fg = 'white',
                                   activeforeground = self.active_color_text, bd=0, compound = tk.TOP)
            accept_button.grid(row = 8, column = 0, ipadx = 50, ipady=10 , padx = 5, pady = 5)

        def accept(self):
            try:
                self.data = [float(self.length_input.get()), int(self.t_left_input.get()),
                        int(self.t_right_input.get()), int(self.time_input.get()), int(self.count_N_input.get()),
                        int(self.start_t_input.get()), self.material_combo.get()]
                messagebox.showinfo('','Данные успешно прочитаны')            
                #self.exit()
            except:
                messagebox.showerror('Ошибка', 'Неверно введены значения.')

if __name__ == "__main__":
    root=tk.Tk()
    root.geometry('720x420+140+90')
    root.config(bg='#e9e8ea')
    root.title('Лабараторная работа №1. Современные численные методы решения граничных задач')
    GUI(root)
    root.resizable(False, False) 
    root.mainloop()