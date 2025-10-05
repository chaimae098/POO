def F7(num):
    if num == 0 :
        return 0
    elif num< 0:
        return f"le nombre doit etre positif"    
    elif num == 1 :
        return 1
    else :
        return F7(num-1)+F7(num-2)   
