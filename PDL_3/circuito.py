from math import sqrt
class Circuito:
    def __init__(self,v_dc=False,r=False,c=False,l=False,f=False,dc=1) -> None:
        self.nombre=""
        self.v_dc=v_dc
        self.r=r
        self.c=c
        self.l=l
        self.f=f
        self.dc=dc
        self.dc_1=0
        self.continuo=False
        self.umbral_c=1-dc
        self.vo=0
        self.il=0
        self.il_max=0
        self.il_min=0
        self.ir=0
        self.delta_il=0
        self.delta_vo=0
        self.modo="continuo"

    def calcular(self):
        self.hallar_continuidad()
        self.hallar_vo()
        self.hallar_delta_vo()
        self.hallar_i()
        print(f"{self.nombre} con D = {self.dc}")
        print(f"Il max:{round(self.il_max,3)} A, Il min {round(self.il_min,3)}, modo de operación {self.modo}")
        print(f"Vo: {self.vo} V, Delta Vo:{self.delta_vo} V.")
        if self.continuo:
            print(f"ripple:{round(self.delta_vo/self.vo,6)}")
        print("")
        print("")

    def hallar_vo(self):
        pass
    def hallar_continuidad(self):
        pass
    def hallar_i(self):
        pass
    def hallar_delta_vo(self):
        pass
