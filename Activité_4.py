with open("Table_multiplication.txt","w+") as file:
    for i in range(1,11):
        file.write(f"La table de multiplication de {i:02d}\n")
        for j in range(1,11):
            file.write(f"{i:02d} x {j:02d} = {i*j:02d}\n")
        file.write("\n")
    file.close()    