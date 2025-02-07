try:
    
    with open("data.txt","r")as f:
        list=[]
        for line in f :
            
            list.append(line.strip())
        print(len(list))

except FileNotFoundError:
    print("file not found :(")




