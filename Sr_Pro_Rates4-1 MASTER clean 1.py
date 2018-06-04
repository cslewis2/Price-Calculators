#This module deals with Jr pro calculations only.
#Define Jr Pro Rates and other variables up front if possible
Mspro = 73
Nspro = 80
Jx = 2
Out = 4
Bm = 12
MsproOut = Mspro - Out
NsproOut = Nspro - Out


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
MsproJx=Mspro-JrxDiscTot
#MsproJx=Mspro-JrxDiscTot

print ()
###CALCULATE TOTAL MEMBER (NOT IN Jrx) COST--new variable
TotMrate = ((Mspro + ((Totclass - 1) * 2)) * ClasTim)
#Logic and calculation for each individual member BILLING CHARGE
if Mclass >= 1: 
    #print ('total member non jx lesson cost is...$',TotMrate)
    Mrate=TotMrate/Totclass
    print ('BILLIMG CHARGE for ',ClasTim,' hour(s) FOR EACH MEMBER IS  $',Mrate)
elif (Mclass + Nclass) <1:
    print ('I didnt know ghosts took lessons...RUN' or 'enter a whole number greater than zero')
print ()

###CALCULATE MEMBER JrX BILLING CHARGE
TotMrateJx = (((MsproJx + ((Totclass-1)*2)) * ClasTim) / Totclass)
#Logic for jJrx calculation
if JrxNum >= 1:
    print ('BILLING CHARGE for Jrx student (always a member) is  $',TotMrateJx)
else:
    print ('No jrx kids in this lessson')
print ()

###CALCULATE NONMEMBER BILLING CHARGE
TotNrate=((Nspro+ ((Totclass-1)*2)) * ClasTim)
#Logic and calculation for Non member BILLING CHARGE
if Nclass >= 1:
    #print ('total nonmember lesson cost is... $',TotNrate)
    Nrate = TotNrate / Totclass
    print ('BILLIMG CHARGE for ',ClasTim,' hour(s) FOR EACH NONMEMBER IS  $',Nrate)
print ()

#BALL MACHINE LANE BILLING CHARGE calculations
print(' BALL MACHINE RATES')
TotMrateBall = ((Mspro - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine Member BILLING CHARGE is $',TotMrateBall)
print()

TotMJxrateBall = ((Mspro - Jx - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine JX Member BILLING CHARGE is $',TotMJxrateBall)
print()

TotNrateBall = ((Nspro - Bm + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on ball machine NONmember BILLING CHARGE is $',TotNrateBall)
print()

#OUTDOOR LESSON RATES BILLING CHARGE calculations
MsproJxOut = (MsproJx - Out)
print ('OUTDOOR RATES')
TotMrateOut = ((MsproOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is on OUTSIDE Member BILLING CHARGE is $',TotMrateOut)
print()

TotMJxrateOut = ((MsproJxOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is OUTSIDE JX Member BILLING CHARGE is $',TotMJxrateOut)
print()

TotNrateOut = ((NsproOut + ((Totclass - 1) * 2)) * ClasTim)/Totclass
print ('If lesson is OUTSIDE NONmember BILLING CHARGE is $',TotNrateOut)