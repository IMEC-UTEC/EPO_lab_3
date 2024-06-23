from circuito import Circuito
from math import sqrt

class Boost(Circuito):
    def __init__(self,v_dc=False,r=False,c=False,l=False,f=False,dc=1) -> None:
        super().__init__(v_dc,r,c,l,f,dc)
        self.nombre="Circuito Boost"
        
    def hallar_vo(self):
        if self.continuo:
            self.vo=round((self.v_dc/(1-self.dc)),2)
        else:
            raiz=sqrt(1+((2*self.dc*self.dc*self.r)/(self.l*self.f)))
            self.vo=round((self.v_dc/2)*(1+raiz),2)

    def hallar_i(self):
        if self.continuo:
            self.ir=self.vo/self.r
            self.il=(self.v_dc)/self.r*(1-self.dc)*(1-self.dc)
            self.delta_il=self.v_dc*self.dc/(2*self.f*self.l)#delta il /2
            self.il_max=self.il+self.delta_il
            self.il_min=self.il-self.delta_il
        else:
            self.il_min=0
            self.delta_il=(self.v_dc*self.dc)/(self.l*self.f)#sacado del libro
            self.il_max=self.delta_il

    def hallar_delta_vo(self):
        if self.continuo:
            self.delta_vo=round(self.vo*(self.dc/(self.r*self.c*self.f)),4)#ok
        else:
            self.delta_vo="Sin datos"

    def hallar_continuidad(self):
        self.continuo=True
        self.hallar_i()
        if self.il_min<0:
            self.continuo=False
            self.modo="discontinuo"
            self.hallar_i()
        else:
            self.continuo=True