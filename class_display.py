import json
import datetime
import os
import subprocess

with open('./sememestre_V/horario.json') as horario:
    val = json.load(horario)
t = datetime.datetime.now()
values= []
dia = t.weekday();
hora = t.hour
hora_nueva= -1
video = "*"
plataforma ="*"
clave ="*"
materia = "*"
for ite in val:
    if dia in ite["dia"] :
        if ite["horario"][0]<= hora and ite["horario"][1] > hora:
            video = ite["video"]
            plataforma = ite["plataforma"]
            clave = ite["clave"]
            materia = ite["materia"]
            break
if(materia == "*"):
    print("libre al fin",end='')
    f = open('./sememestre_V/a.sh','w')
    f.write(f"https://www.youtube.com/watch?v=Qvhcs93C2x8&list=RDQvhcs93C2x8&start_radio=1")
    f.close()
    f = open('./sememestre_V/b.sh','w')
    f.write(f"https://www.youtube.com/watch?v=Qvhcs93C2x8&list=RDQvhcs93C2x8&start_radio=1")
    f.close()
    f = open('./sememestre_V/clave.sh','w')
    f.write("echo "" ")
    f.close()
else:
    print(f"{materia}")
    f = open('./sememestre_V/a.sh','w')
    f.write(f"echo {video}")
    f.close()
    f = open('./sememestre_V/b.sh','w')
    f.write(f"echo {plataforma}")
    f.close()
    f = open('./sememestre_V/clave.sh','w')
    if clave != "":
        f.write(f"echo \"CLAVE: {clave}\"")
    else:
        f.write(f"echo """)
    f.close()
