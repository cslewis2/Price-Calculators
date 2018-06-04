#This module deals with Jr pro calculations only.
#Define Jr Pro Rates and other variables up front if possible

from decimal import *
Mjpro = 67.00
Njpro = 74
Jx = 2
Out = 4
Bm = 12
MjproOut = Mjpro - Out
NjproOut = Njpro - Out

#LESSON TIME VIA USER INPUT
ClasTim = (float(input('how long is the lesson today? Input as decimal  ')))
print ('Total class time is',ClasTim,'hours')
print ()

#CALCULATE CLASS SIZE VIA USER INPUTS
Mclass = (int(input ('how many members today?  ')))
Nclass = (int(input('how many nonmembers today?  ')))
Totclass = (Mclass+Nclass)
print ('Class size is ',Totclass)

# HOW MANY MEMBERS IN Jrx
JrxNum = (int(input ('How many of these members in Jrx?  ')))
JrxDiscTot=JrxNum*Jx
MjproJx=Mjpro-JrxDiscTot
#MjproJx=Mjpro-JrxDiscTot
print ()
###CALCULATE TOTAL MEMBER (NOT IN Jrx) COST--new variable
TotMrate = ((Mjpro + ((Totclass - 1) * 2)) * ClasTim)
#Logic and calculation for each individual member BILLING CHARGE
if Mclass >= 1: 
    #print ('total member non jx lesson cost is...$',TotMrate)
    Mrate=TotMrate/Totclass
    print ('BILLIMG CHARGE for ',ClasTim,' hour(s) FOR EACH MEMBER IS  $',Mrate)
elif (Mclass + Nclass) <1:
    print ('I didnt know ghosts took lessons...RUN' or 'enter a whole number greater than zero')
print ()

###CALCULATE MEMBER JrX BILLING CHARGE
TotMrateJx = (((MjproJx + ((Totclass-1)*2)) * ClasTim) / Totclass)
#Logic for jJrx calculation
if JrxNum >= 1:
    print ('BILLING CHARGE for Jrx student (always a member) is  $',TotMrateJx)
else:
    print ('No jrx kids in this lessson')
print ()

###CALCULATE NONMEMBER BILLING CHARGE-new variable
TotNrate=((Njpro+ ((Totclass-1)*2)) * ClasTim)
#Logic and calculation for Non member BILLING CHARGE
if Nclass >= 1:
    #print ('total nonmember lesson cost is... $',TotNrate)
    Nrate = TotNrate / Totclass
    print ('BILLIMG CHARGE for ',ClasTim,' hour(s) FOR EACH NONMEMBER IS  $',Nrate)
print ()

###CALCULATE BALL MACHINE LESSON BILLING CHARGE calculations
print(' BALL MACHINE RATES')
TotMrateBall = ((Mjpro - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine Member BILLING CHARGE is $',TotMrateBall)
print()
#MEMBER NOT IN JRX
TotMJxrateBall = ((Mjpro - Jx - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine JX Member BILLING CHARGE is $',TotMJxrateBall)
print()
#NON MEMBER
TotNrateBall = ((Njpro - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine NONmember BILLING CHARGE is $',TotNrateBall)
print()

###CALCULATE OUTDOOR LESSON RATES BILLING CHARGE
MjproJxOut = (MjproJx - Out)
print ('OUTDOOR RATES')
#MEMBER NOT IN JRX
TotMrateOut = ((MjproOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on OUTSIDE Member BILLING CHARGE is $',TotMrateOut)
print()
#MEMBER IN JRX
TotMJxrateOut = ((MjproJxOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is OUTSIDE JX Member BILLING CHARGE is $',TotMJxrateOut)
print()
#NON MEMBER
TotNrateOut = ((NjproOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is OUTSIDE NONmember BILLING CHARGE is $',TotNrateOut)
