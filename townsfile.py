temp = open("townsfile.csv","r")
towns = temp.read()
temp.close()
#print(towns)

eachTown = towns.split("\n")
#print(eachTown)

newList = []

for eachItem in eachTown:

    record = eachItem.split(",")

    newList.append(record)

#print(newList[7][0])

whatTown = input("What town are you looking for? ").title()

for eachItem in newList:
    if whatTown in eachItem:
        print("Town: "+eachItem[0])
        print("County: "+eachItem[1])
        print("Population: "+eachItem[2])
        print("Area: "+eachItem[3])
        print()

whatCounty = input("What county are you looking for? ").title()

for eachItem in newList:
    if whatCounty in eachItem:
        print("Town: "+eachItem[0])
        print("County: "+eachItem[1])
        print("Population: "+eachItem[2])
        print("Area: "+eachItem[3])
        print()



temp = open("townsfile.csv","a")

content = "\nOxford"+","+"Oxfordshire"+","+"150200"+","+"4559"+"\nStoke-On-Trent"+","+"Staffordshire"+","+"249000"+","+"9274"

temp.write(content)

temp.close()

temp = open("townsfile.csv","r")
info = temp.read()
temp.close()






town = input("What is the name of the new town?").title()
county = input("What is the county?").title()
population = input("What is the population?")
area = input("What is the area?")

temp = open("townsfile.csv","a")
stuff = "\n"+town+","+county+","+population+","+area
temp.write(stuff)
temp.close()

temp = open("townsfile.csv","r")
info = temp.read()
temp.close()
