orderamount=[]
names=[] 
import csv
alldata=[]
import os
shop=1
order=0
amount1=0
ordercounter=[]
customers=[]
amountpercustomer=[]
orderspercustomer=[]
addresspercustomer=[]
datepercustomer=[]
spdates=[]
amounts=[]
co=5
orders=[]
amountperday=[]
user1=[]
user2=[]
user3=[]
shop==1
def bruh (c):
    c+=1
un=str(input("Give usernumber: "))
#pw=str(input("Give password: "))
account=["userone","usertwo","userthree"]
while un!='userone' and un!='usertwo' and un!='userthree':
    un=str(input("Give the correct usernumber: "))
alldata.append(un)
today=str(input("Give today's date: "))
alldata.append(today)
# ordercounter.append(today)
spdates.append(today)
# amountperday.append(today)
try:
    if os.stat("namesfile.txt").st_size != 0:
          with open("namesfile.txt", "r") as nf:
              for line in nf:
                  names.append(str(line.strip()))
          with open("addressfile.txt", "r") as adf:
              for line in adf:
                  addresspercustomer.append(str(line.strip()))  
          with open("datefile.txt", "r") as df:
              for line in df:
                  datepercustomer.append(str(line.strip()))                                
          with open("customeramountfile.txt", "r") as caf:
              for line in caf:
                  amountpercustomer.append(float(line.strip()))
          with open("customerorderfile.txt", "r") as cof:
              for line in cof:
                  orderspercustomer.append(int(line.strip())) 
          with open("sdates.txt", "r") as sdf:
              for line in sdf:
                  spdates.append(str(line.strip()))
          with open("sorders.txt", "r") as sof:
              for line in sof:
                  orders.append(int(line.strip()))
          with open("samount.txt", "r") as saf:
              for line in saf:
                  amounts.append(int(line.strip()))
          with open ('userone1.txt','a') as u1f:
               for line in u1f :
                  user1.append(str(line.strip()))
          with open ('usertwo2.txt','a') as u2f:
               for line in u2f :
                  user2.append(str(line.strip()))  
          with open ('userthree3.txt','a') as u3f:
               for line in u3f :
                  user3.append(str(line.strip())) 
          # for a in range(len(names)):
          #     customers.append(names[a])
          #     customers.append(addresspercustomer[a])
          #     customers.append(datepercustomer[a])
          #     customers.append(amountpercustomer[a])
          #     customers.append(orderspercustomer[a])
          # for i in range(len(spdates)):
          #     ordercounter.append(spdates[i])
          #     ordercounter.append(orders[i])
          #     amountperday.append(spdates[i])
          #     amountperday.append(amounts[i])
          
    
except:             
    while shop==1:
      try:
        for a in range(len(names)):
              customers.append(names[a])
              customers.append(addresspercustomer[a])
              customers.append(datepercustomer[a])
              customers.append(amountpercustomer[a])
              customers.append(orderspercustomer[a])
        for i in range(len(spdates)):
              ordercounter.append(spdates[i])
              ordercounter.append(orders[i])
              amountperday.append(spdates[i])
              amountperday.append(amounts[i])
      except:
        userwants=int(input("To access the system press 1, to make a new order press 2, to log-out press 3(note: IF this is your first time running the programm you will not be able to access the system): "))
        while (userwants<1 and userwants>3) or userwants==str:
            userwants=int(input('Give the correct number: '))
        if userwants==1:
              print ("For Numbers of order placed by one specific customer press 1, for Number of orders in one specific day press 2, for Total amount of all orders delivered press 3, for Total amount of the orders placed by a specific customer press 4, for Total amount of the orders placed by a specific day press 5, for the 'names of customers' list press 6, for the orders entered per user press 7")
                
              output=int(input("Give number: "))
              if output==1:
                  customername=str(input("Give the name of the customer: "))
                  index1=names.index(customername)
                  position1=(index1+1)*5-1
                  print (customers[position1])
              elif output==2:
                  sdate=str(input('Give date: '))
                  index2=ordercounter.index(sdate)
                  position2=index2+1
                  print (ordercounter[position2])
              elif output==3:
                  print(sum(amountpercustomer))
              elif output==4:
                  customername2=str(input('Give the name of the customer: '))
                  index3=names.index(customername2)
                  position3=(index3+1)*5-2
                  print (customers[position3])
              elif output==5:
                  sdate1=str(input('Give date: '))
                  index4=amountperday.index(sdate1)
                  position4=index4+1
                  print (amountperday[position4])
              elif output==6:
                  print(nf)
              elif output==7:
                  userx=str(input('Give usernumber: '))
                  if userx=='userone':
                      print(u1f)
                  elif userx=='usertwo':
                      print(u2f)
                  elif userx=='userthree':
                      print(u3f)
              elif output==8:
                  with open("alldata.csv",'a') as csvfile:
                      reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                      for row in reader:
                          print(', '.join(row))
              elif output==9:
                  with open("ordersperdays.csv",'a') as csv1file:
                      writer1 = csv.writer(csv1file)
                      writer1.writerow(amountperday)
                      reader1 = csv.reader(csv1file, delimiter=' ', quotechar='|')
                      for row in reader1:
                          print(', '.join(row))
             
              
              
                  
        elif userwants==2:
            order += 1
            name = str(input("Give the name of the customer: "))
            alldata.append(name)
            
            if un=='userone':
                user1.append(name)
            elif un=='usertwo':
                user2.append(name)
            elif un=='userthree':
                user3.append(name)
            if name in names:
                amount = int(input("Give total amount of order: "))
                alldata.append(amount)
                if un=='userone':
                    user1.append(amount)
                elif un=='usertwo':
                    user2.append(amount)
                elif un=='userthree':
                    user3.append(amount)
                amount1+=amount
                index=names.index(name)
                position=(index+1)*5-1
                number=customers[position]+1
                customers.pop(position)
                customers.insert(position, number)
                orderspercustomer.pop(index)
                orderspercustomer.insert(index, number)
                customeramount=customers[position-1]+amount
                customers.pop(position-1)
                customers.insert(position-1, customeramount)
                amountpercustomer.pop(index)
                amountpercustomer.insert(index, customeramount)
            else:
                 print("This customer is new, lets make an ID, type NO to stop")
                 address = str(input("Give address: "))
                 if address=="NO":
                     break
                 else:
                     with open("alldata.csv",'a') as csvfile:
                         writer = csv.writer(csvfile)
                         writer.writerow(address)
                     addresspercustomer.append(address)
                     date = str(input("Give date: "))
                     with open("alldata.csv",'a') as csvfile:
                         writer = csv.writer(csvfile) 
                         writer.writerows(date)
                     datepercustomer.append(date)
                     customers.append(name)
                     customers.append(address)
                     customers.append(date)
                     names.append(name)
                     amount = int(input("Give total amount of order: "))
                     alldata.append(amount)
                     if un=='userone':
                        user1.append(amount)
                     elif un=='usertwo':
                        user2.append(amount)
                     elif un=='userthree':
                        user3.append(amount)
                     print("Done")
                     amount1+=amount
                     orderamount.append(amount)
                     customers.append(amount)
                     amountpercustomer.append(amount)
                     customers.append(1)
                     orderspercustomer.append(1)
        elif userwants==3:
           with open ('namesfile.txt','a') as nfile:
               for n in names:
                   nfile.write('%s\n' % n)
           with open ('addressfile.txt','a') as afile:
               for a in addresspercustomer:
                   afile.write('%s\n' % a)
           with open ('datefile.txt','a') as dfile:
               for d in datepercustomer:
                   dfile.write('%s\n' % d)
           with open ('customeramountfile.txt','a') as cafile:
               for ca in amountpercustomer:
                   cafile.write('%s\n' % ca)
           with open ('customerorderfile.txt','a') as cofile:
               for co in orderspercustomer:
                   cofile.write('%s\n' % co)
           ordercounter.append(today)
           ordercounter.append(order)
           orders.append(order)
           amountperday.append(amount1)
           amounts.append(amount1)
           # with open ('ordersperdayfile.txt','a') as pdfile:
           #     for pd in ordercounter:
           #         pdfile.write('%s\n' % pd)
           with open ('sorders.txt','a') as sofile:
               for so in orders:
                   sofile.write('%s\n' % so)
           with open ('sdates.txt','a') as sdfile:
               for sd in spdates:
                   sdfile.write('%s\n' % sd)
           with open ('samount.txt','a') as safile:
               for sa in amounts:
                   safile.write('%s\n' % sa)
           if un=='userone':
                with open ('userone1.txt','a') as u1file:
                    for u1 in user1:
                        u1file.write('%s\n' % u1)
           elif un=='usertwo':
                with open ('usertwo2.txt','a') as u2file:
                    for u2 in user2:
                        u2file.write('%s\n' % u2)
           elif un=='userthree':
                with open ('userthree3.txt','a') as u3file:
                    for u3 in user3:
                        u3file.write('%s\n' % u3)
           with open("alldata.csv",'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(alldata)
           print ('Bye')
           shop+=1
            
          
    # else:
    #      with open("namesfile.txt", "r") as nf:
    #          for line in nf:
    #              names.append(str(line.strip()))
    #      with open("addressfile.txt", "r") as adf:
    #          for line in adf:
    #              addresspercustomer.append(str(line.strip()))  
    #      with open("datefile.txt", "r") as df:
    #          for line in df:
    #              datepercustomer.append(str(line.strip()))                                
    #      with open("customeramountfile.txt", "r") as caf:
    #          for line in caf:
    #              amountpercustomer.append(float(line.strip()))          
    #      with open("sdates.txt", "r") as sdf:
    #          for line in sdf:
    #              spdates.append(str(line.strip()))
    #      with open("sorders.txt", "r") as sof:
    #          for line in sof:
    #              orders.append(int(line.strip()))
    #      with open("samount.txt", "r") as saf:
    #          for line in saf:
    #              amounts.append(int(line.strip()))
    #      for i in range(len(names)):
    #          customers.append(names[i])
    #          customers.append(addresspercustomer[i])
    #          customers.append(datepercustomer[i])
    #          customers.append(amountpercustomer[i])
    #          customers.append(orderspercustomer[i])
    #      for i in range(len(spdates)):
    #          ordercounter.append(spdates[i])
    #          ordercounter.append(orders[i])
    #          amountperday.append(spdates[i])
    #          amountperday.append(amounts[i])
# else:
#      with open("namesfile.txt", "r") as nf:
#          for line in nf:
#              names.append(str(line.strip()))
#      with open("addressfile.txt", "r") as adf:
#          for line in adf:
#              addresspercustomer.append(str(line.strip()))  
#      with open("datefile.txt", "r") as df:
#          for line in df:
#              datepercustomer.append(str(line.strip()))                                
#      with open("customeramountfile.txt", "r") as caf:
#          for line in caf:
#              amountpercustomer.append(float(line.strip()))          
#      with open("customerorderfile.txt", "r") as of:
#          for line in of:
#              orderspercustomer.append(int(line.strip()))              
#      for i in range(len(names)):
#          customers.append(names[i])
#          customers.append(addresspercustomer[i])
#          customers.append(datepercustomer[i])
#          customers.append(amountpercustomer[i])
#          customers.append(orderspercustomer[i])
         
    #  for i in range (0,len(names)):
    #      customers.append(names[i*6])
    #  for i in range (len(names)):
    #      customers.append(names[(i+1)*6-5])
    # for i in range (len(names)):
    #      customers.append(names[])
                          
                     
