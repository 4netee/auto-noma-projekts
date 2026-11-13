import tkinter as tk
from tkinter import messagebox

class Transportlidzeklis:
    #Bāzes klase, kas satur pamata informāciju par transportlīdzekli

    def __init__(self, marka: str, gads: int, bazes_cena: float):
        self.marka = marka
        self.gads = gads
        self.__bazes_cena = bazes_cena
        # Privātais atribūts bāzes cenai

    def get_bazes_cena(self) -> float:
        # Getter metode, lai droši nolasītu privāto bāzes cenu.
        return self.__bazes_cena

    def set_bazes_cena(self, jauna_cena: float):
        # Setter metode ar ievades pārbaudi (cenai jābūt > 0).
        if jauna_cena > 0:
            self.__bazes_cena = jauna_cena
        else:
            messagebox.showwarning("Brīdinājums", "Cenai ir jābūt lielākai par 0!")

    def izvadit_aprakstu(self) -> str:
        # Atgriež pamatinformāciju par auto.
        return f"Auto: {self.marka}, Izlaiduma gads: {self.gads}"

class AutoNoma(Transportlidzeklis):
    # Apakšklase, kas pārvalda auto nomas aprēķinus.
    def __init__(self, marka: str, gads: int, bazes_cena: float, dienu_skaits: int):
        super().__init__(marka, gads, bazes_cena)
        self.dienu_skaits = dienu_skaits
        # Papildu lauks nomas ilgumam

    def aprekinat_kopejo_cenu(self) -> float:
        dienas_maksajums = self.get_bazes_cena()
        return dienas_maksajums * self.dienu_skaits

#TKINTER LOGS

def palaist_gui():
    # Izveidojam nomas objektu
    mans_auto = AutoNoma("Audi A4", 2020, 40.0, 5)

    root = tk.Tk()
    root.title("Auto Noma")
    root.geometry("350x300")

    # Funkcija, kas atjaunina tekstu logā
    def atjaunot_rezultatu():
        teksts = (
            f"{mans_auto.izvadit_aprakstu()}\n"
            f"Bāzes cena dienā: {mans_auto.get_bazes_cena()} EUR\n"
            f"Nomas ilgums: {mans_auto.dienu_skaits} dienas\n"
            f"Kopējā cena: {mans_auto.aprekinat_kopejo_cenu()} EUR"
        )
        rezultats_label.config(text=teksts)

    # Funkcija cenas maiņai
    def mainit():
        try:
            jauna = float(jauna_cena_entry.get())
            mans_auto.set_bazes_cena(jauna)
            atjaunot_rezultatu()
        except ValueError:
            messagebox.showerror("Kļūda", "Ievadiet derīgu skaitli!")

    # Interfeisa elementi
    tk.Label(root, text="Auto Nomas Sistēma", font=("Arial", 12, "bold")).pack(pady=10)

    rezultats_label = tk.Label(root, text="", justify="left", font=("Arial", 10), bg="#f0f0f0", padx=10, pady=10)
    rezultats_label.pack(pady=10, fill="x", padx=20)
    atjaunot_rezultatu() # Sākotnējā teksta ielāde

    # Cenas maiņas daļa
    tk.Label(root, text="Ievadiet jauno bāzes cenu:").pack()
    jauna_cena_entry = tk.Entry(root)
    jauna_cena_entry.pack(pady=5)

    tk.Button(root, text="Mainīt cenu un pārrēķināt", command=mainit).pack(pady=5)

    root.mainloop()

# Programmas izpildes daļa
if __name__ == "__main__":
    print("Auto Nomas Sistēmas Tests")
    mans_auto_tests = AutoNoma("Audi A4", 2020, 40.0, 5)
    print(mans_auto_tests.izvadit_aprakstu())
    print(f"Bāzes cena dienā: {mans_auto_tests.get_bazes_cena()} EUR")
    print(f"Nomas ilgums: {mans_auto_tests.dienu_skaits} dienas")
    print(f"Kopējā cena: {mans_auto_tests.aprekinat_kopejo_cenu()} EUR")
    
    palaist_gui()
