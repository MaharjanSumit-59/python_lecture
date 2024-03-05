import datetime
database={}
class reminder:
    def store(key1,value1):  
        database.update({key1:value1})
        print(database)
        return database
    def check(data1,a): #only check year but not month and day
        st=datetime.datetime.now().year
        val=data1[a]
        if st==val:
            print(f'Happy {a}!!!')   #only prints the recent correct value if there are multiple correct one
        else:
            print(f"It's {st},nothing special but {a} is on {val}")
        
rem1=reminder
while True:
    print('[1] Store')
    print('[2] Check')
    x=int(input("Enter your choice: "))
    if x==1:
       a=input("Enter your event: ")
       b=int(input(f"Enter date for {a}: "))
       data1=rem1.store(a,b)
    if x==2:
       rem1.check(data1,a)
    ask=input("Continue?")
    if ask=='n':
        break





