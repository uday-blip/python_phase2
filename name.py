fruit=5
for row in range(1,fruit+1):
    u=""
    for col in range(1,fruit+1):
        if row==fruit or col==1 or col==fruit:
            u+="u"+" "
        else:
            u+=" "+" "
    print(u)