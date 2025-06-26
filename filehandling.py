car=open("./uday.txt","r")
para=car.readlines();
first_letter=[]
result=""
for line in para:
     first_letter.append(line[0])
result="".join(first_letter)
result=result.replace("GG","G G")
print(result)


