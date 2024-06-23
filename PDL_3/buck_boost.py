from circuito import Circuito

class Buck_Boost(Circuito):
    def __init__(self,v_dc=False,r=False,c=False,l=False,f=False,dc=1) -> None:
        super().__init__(v_dc,r,c,l,f,dc)
        self.nombre="Circuito Buck Boost"

    def hallar_vo(self):
        if self.continuo:
            self.vo=abs(round(-self.v_dc*(self.dc)/(1-self.dc),2))
        else:
            self.vo="Ni idea"

    def hallar_i(self):
        if self.continuo:
            self.ir=0
            self.il=self.v_dc*self.dc/(self.r*(1-self.dc)*(1-self.dc))
            self.delta_il=self.v_dc*self.dc/(2*self.l*self.f)#es delta il /2
            self.il_max=self.il+self.delta_il
            self.il_min=self.il-self.delta_il
        else:
            pass

    def hallar_delta_vo(self):
        if self.continuo:
            self.delta_vo=abs(round(self.vo*(self.dc/(self.r*self.c*self.f)),4))
        else:
            self.delta_vo="sin datos"

    def hallar_continuidad(self):
        self.continuo=True
        self.hallar_i()
        if self.il_min<0:
            self.modo="discontinuo"
            self.dc_1="No se"
            print(f"Operación en corriente discontinua \nD1= {(self.dc_1)}")
            self.continuo=False
            self.il_min=0
    


