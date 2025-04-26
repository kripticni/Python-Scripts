from typing import final
from typing import override
from typing import TextIO

@final
class Takmicar:

    def __init__(self, ime: str | None, z1: int | None, z2: int | None, z3: int | None):
        if ime is not None:
            self.ime = ime
        else:
            self.ime = ""
        if z1 is not None:
            self.z1 = z1
        else:
            z1 = 0
        if z2 is not None:
            self.z2 = z2
        else:
            self.z2 = 0
        if z3 is not None:
            self.z3 = z3
        else:
            self.z3 = 0

    @property
    def Ime(self) -> str:
        return self.ime
    @Ime.setter
    def Ime(self, value:str):
        self.ime = value

    @property
    def Z1(self) -> int:
        return self.z1
    @Z1.setter
    def Z1(self, value: int):
        if(value < 0 or value > 100):
           raise ValueError("Poeni su od 0 do 100")
        self.z1 = value
    @property
    def Z2(self) -> int:
        return self.z2
    @Z2.setter
    def Z2(self, value: int):
        if(value < 0 or value > 100):
           raise ValueError("Poeni su od 0 do 100")
        self.z2 = value
    @property
    def Z3(self) -> int:
        return self.z3
    @Z3.setter
    def Z3(self, value: int):
        if(value < 0 or value > 100):
           raise ValueError("Poeni su od 0 do 100")
        self.z3 = value

    def Citaj(self, r: TextIO):
        self.Z1 = int(r.readline())
        self.Z2 = int(r.readline())
        self.Z3 = int(r.readline())

    def Ukupno(self) -> int:
        return self.Z1 + self.Z2 + self.Z3

    def ToString(self):
        return self.Ime + " | " + "1." + str(self.Z1) + " 2." + str(self.Z2) \
               + " 3." + str(self.Z3) + " = " + str(self.Ukupno())

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Takmicar):
            return False

        if(self.Ukupno() == other.Ukupno()):
           return True
        max1 = 0
        max2 = 0
        
        if(self.Z1 == 100): max1 += 1
        if(self.Z2 == 100): max1 += 1
        if(self.Z3 == 100): max1 += 1

        if(other.Z1 == 100): max2 += 1
        if(other.Z2 == 100): max2 += 1
        if(other.Z3 == 100): max2 += 1

        if(max1 == max2):
            return True
        else:
            return False

    @override
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Takmicar):
            return False
        
        return not (self == other)


t1 = Takmicar("Lazar", 99, 99, 100)
t2 = Takmicar(None, None, None, None)
t2.Ime = "Unknown"
t2.Z1 = 100
t2.Z2 = 50
t2.Z3 = 0

print(t1.ToString())
print(t2.ToString())
print(t1 == t2)
