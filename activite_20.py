#activite 20
adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
print("la première adresse dans la liste:",adresses_ip[0])
print("la dernière adresse dans la liste:",adresses_ip[-1])
print("la troisième adresse dans la liste:",adresses_ip[2])
adresses_ip.append("172.31.0.1")
adresses_ip.remove("200.100.50.1")
print("le nombre d'adresses restants dans la liste :", len(adresses_ip))
if "192.168.0.1" in adresses_ip:
    print("192.168.0.1 est dans la liste.")

for n in adresses_ip:
    if n.startswith("10.0.0") :
        print(n,"est de classe A.")       

adresses_ip.sort()        
print("la liste par ordre croissant:",adresses_ip)
compt=0
for n in adresses_ip:
    if n.startswith("192.168") :
        print(n,"est de classe C.")   
        compt+=1

if compt<len(adresses_ip)  :
    print("certains adresses n'appartiennent pas à la classe C.")   

i=0
for n in adresses_ip:
    if n.startswith("200.100") :
        i+=1
        
print(f"{i} adresses IP sont des adresses IP publiques.")          