from circuito import Circuito
from math import sqrt

class Buck(Circuito):

    def __init__(self,v_dc,r=False,c=False,l=False,f=False,dc=1) -> None:
        super().__init__(v_dc,r,c,l,f,dc)
        self.nombre="Ciercuito Buck"

    def hallar_vo(self):
        if self.continuo:
            self.vo=round((self.v_dc*self.dc),2)#ok
        else:
            self.vo=round(self.v_dc*self.dc/(self.dc+self.dc_1),2)#ok}
      
    def hallar_i(self):
        if self.continuo:
            self.il=self.vo/self.r
            self.ir=self.il
            self.delta_il=((self.vo/self.l)*(1-self.dc)/self.f)*0.5
            self.delta_il=(1-self.dc)*self.vo/(self.l*self.f*2)#es delta il /2
            self.il_max=self.il+self.delta_il
            self.il_min=self.il-self.delta_il
        else:
            self.il_min=0
            self.il_max=self.vo*self.dc_1/(self.l*self.f)


    def hallar_continuidad(self):
        #Revisado, funciona
        raiz=sqrt((self.dc*self.dc)+((8*self.l*self.f)/(self.r)))
        self.dc_1=(-self.dc+raiz)*0.5
        if(self.dc_1<(self.umbral_c)):
            self.continuo=False
            self.modo="discontinuo"
        else:
            self.continuo=True

    def hallar_delta_vo(self):
        if self.continuo:
            self.delta_vo=round(self.vo*((1-self.dc)/(8*self.l*self.c*self.f*self.f)),4)
        else:
            self.delta_vo="Sin datos"