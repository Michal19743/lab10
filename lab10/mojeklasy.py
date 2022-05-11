# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:04:32 2019

@author: Student
"""

def testy():
    
    #Zadanie 1:
    
    s1 = Student("Michał", "Rakowski", 19743, "IIS")
    
    print(s1.imie)
    print(s1.nazwisko)
    print(s1.kierunek)
    print(s1)
    
    print()
    
    
    #Zadanie 2:
    
    s2 = Student("Piotr","Kiryczuk",54321,"IIS")
    
    print(s1.__lt__(s2))
    print(s1.__eq__(s2))
    
    print()
    
    
    #Zadanie 3:
    
    s3 = Student("Łukasz", "Broda", 12345, "IIS")
    
    print("Licznik: %s"%(s3.getLicznik()))
    
    print()
    
    
    #Zadanie 4:
    
    s4 = StudentInformatyki("Majkel", "Rakson", 32123, "", "Programista")
    
    print(s4)
    print(s4.specjalnosc)
    pass
    
    
class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek

    def __str__(self):
        return " Imie: %s\n nazwisko: %s\n nr ideksu: %s\n kierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

    def __lt__(self,other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
            
    def getLicznik(self):
        return self.__licznik
        
    def rok_drugi(self):
        return self
    
    @rok_drugi
    def funkcja():
        print("Czesc")



class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc


if __name__ == "__main__":
    testy()