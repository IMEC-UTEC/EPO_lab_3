from buck import Buck
from boost import Boost
from buck_boost import Buck_Boost

r=15
v_dc=12
f=100000
c=0.00022
l=0.0001

duty_cycles= [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for duty_cycle in duty_cycles:
    buck=Buck(v_dc=v_dc,r=r,c=c,l=l,f=f,dc=duty_cycle)
    buck.calcular()

for duty_cycle in duty_cycles:
    boost=Boost(v_dc=v_dc,r=r,c=c,l=l,f=f,dc=duty_cycle)
    boost.calcular()

for duty_cycle in duty_cycles:
    buck_bost=Buck_Boost(v_dc=v_dc,r=r,c=c,l=l,f=f,dc=duty_cycle)
    buck_bost.calcular()