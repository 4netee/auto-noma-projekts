class Transportlidzeklis:
    "Bāzes klase, kas satur pamata informāciju par transportlīdzekli."
    
    def __init__(self, marka: str, gads: int, bazes_cena: float):
        self.marka = marka
        self.gads = gads
        self.__bazes_cena = bazes_cena  
        # Privātais atribūts bāzes cenai
    def get_bazes_cena(self) -> float:
        #Getter metode, lai droši nolasītu privāto bāzes cenu.
        return self.__bazes_cena
    def set_bazes_cena(self, jauna_cena: float):
        #Setter metode ar ievades pārbaudi (cenai jābūt > 0).
        if jauna_cena > 0:
            self.__bazes_cena = jauna_cena
        else:
            print("Brīdinājums: Cenai ir jābūt lielākai par 0!")
    def izvadit_aprakstu(self) -> str:
        #Atgriež pamatinformāciju par auto.
        return f"Auto: {self.marka}, Izlaiduma gads: {self.gads}"


class AutoNoma(Transportlidzeklis):
    #Apakšklase, kas pārvalda auto nomas aprēķinus.
    def __init__(self, marka: str, gads: int, bazes_cena: float, dienu_skaits: int):
        super().__init__(marka, gads, bazes_cena)
        self.dienu_skaits = dienu_skaits  
        # Papildu lauks nomas ilgumam
    def aprekinat_kopejo_cenu(self) -> float:
        dienas_maksajums = self.get_bazes_cena()
        return dienas_maksajums * self.dienu_skaits


#Programmas izpildes daļa
if __name__ == "__main__":
    print("Auto Nomas Sistēmas Tests")
    
    #Izveidojam nomas objektu (piemēram, Audi A4 uz 5 dienām par 40 EUR dienā)
    mans_auto = AutoNoma("Audi A4", 2020, 40.0, 5)
    
    print(mans_auto.izvadit_aprakstu())
    print(f"Bāzes cena dienā: {mans_auto.get_bazes_cena()} EUR")
    print(f"Nomas ilgums: {mans_auto.dienu_skaits} dienas")
    print(f"Kopējā cena: {mans_auto.aprekinat_kopejo_cenu()} EUR")
    
    # Pārbaudām cenu maiņu (setter)
    print("\nMainām bāzes cenu...")
    mans_auto.set_bazes_cena(45.0)
    print(f"Jaunā kopējā cena par {mans_auto.dienu_skaits} dienām: {mans_auto.aprekinat_kopejo_cenu()} EUR")
