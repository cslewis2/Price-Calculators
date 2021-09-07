lets do it agai...NOTT nlhlhhy

#indoor full court jr pro rates@@@
def jpro_lesson_prices():
    jpro_member = 67
    jpro_nonmember = 74   
    jx_discount = 2
    return jpro_member,jpro_nonmember,jx_discount
sales = jpro_lesson_prices()

#alternative lesson sites--on ball machine and outside courts
def other_cases():
    ball_mach = 12
    jpro_outside = 4
    return ball_mach,jpro_outside
alt_cases=other_cases()

#LESSON TIME VIA USER INPUT
def class_length():
    clas_tim = (float(input('how long is the lesson today? Input as decimal  ')))
    #print ('Total class time is',ClasTim,'hours')
    return (clas_tim)
class_hours = class_length()

#CALCULATE CLASS SIZE VIA USER INPUTS
def class_size():
    while True:    
        try:
            members = (int(input ('how many members today?  ')))
            non_members = (int(input('how many nonmembers today?  ')))
            total_class = (members+non_members)
            #print ('Class size is ',total_class)
        except ValueError:
            print ('numbers only please try again')        
            continue
        else:
            print('thanks for using a number')
            break             
    return members,non_members,total_class
students_inclass=class_size()
#keep adding error correction
# HOW MANY MEMBERS IN Jrx

def jrx_participants():
    jrx_students = (int(input ('How many of these members in Jrx?  ')))
    jrxdisctot=jrx_students*sales[2]
    jpro_jrx_rate = sales[0] - jrxdisctot
    return (jrx_students,jpro_jrx_rate)
jrx_rate = jrx_participants()

# CALCULATE TOTAL MEMBER (NOT IN Jrx) RATE--new variable
#Logic and calculation for each individual member BILLING CHARGE

total_member_cost = ((sales[0] + ((students_inclass[2] - 1) * 2)) * class_hours)
if total_member_cost >= 1: 
    #print ('total member non jx lesson cost is...$',TotMrate)
    billed_member_rate=sales[0] / students_inclass[2]
    print ('BILLING CHARGE for ',class_hours,' hour(s) FOR EACH MEMBER IS  $',billed_member_rate)
elif (students_inclass[2]) < 1:
    print ('I didnt know ghosts took lessons...RUN' or 'enter a whole number greater than zero')
print ()

#CALCULATE MEMBER JrX BILLING CHARGE

total_jxmember_cost = (((jrx_rate[1] + ((students_inclass[2]-1)*2)) * class_hours) / students_inclass[2])
#Logic for jJrx calculation
if jrx_rate[0] >= 1:
    print ('BILLING CHARGE for Jrx student (always a member) is  $',total_jxmember_cost)
else:
    print ('No jrx kids in this lessson')
print ()

#CALCULATE NONMEMBER BILLING CHARGE-new variable

total_nonmember_cost=((sales[1] + ((students_inclass[2]-1)*2)) * class_hours)
#Logic and calculation for Non member BILLING CHARGE
if students_inclass[1] >= 1:
    #print ('total nonmember lesson cost is... $',TotNrate)
    total_nonmember_cost = sales[1] / students_inclass[2]
    print ('BILLIMG CHARGE for ',class_hours,' hour(s) FOR EACH NONMEMBER IS  $',total_nonmember_cost)
print ()

#CALCULATE BALL MACHINE LESSON BILLING CHARGE calculations

print(' BALL MACHINE RATES')
#MEMBER RATE (NO JRX)
total_member_ball = ((sales[0] - alt_cases[0] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is on ball machine Member BILLING CHARGE is $',total_member_ball)
print()
#MEMBER IN JRX
total_jxmember_ball = ((sales[0] - sales[2] - alt_cases[0] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is on ball machine JX Member BILLING CHARGE is $',total_jxmember_ball)
print()
#NON MEMBER
total_nonmember_ball = ((sales[1] - alt_cases[0] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is on ball machine NONmember BILLING CHARGE is $',total_nonmember_ball)
print()

#CALCULATE OUTDOOR LESSON RATES BILLING CHARGE

print ('OUTDOOR RATES')
#MEMBER NO JRX
total_member_outside = ((sales[0] - alt_cases[1] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is on OUTSIDE Member BILLING CHARGE is $',total_member_outside)
print()
#MEMBER IN JRX
total_jxmember_outside = ((sales[0] - alt_cases[1] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is OUTSIDE JX Member BILLING CHARGE is $',total_jxmember_outside)
print()
#NON MEMBER
total_nonmember_outside = ((sales[1] - alt_cases[1] + ((students_inclass[2] - 1) * 2)) * class_hours) / students_inclass[2]
print ('If lesson is OUTSIDE NONmember BILLING CHARGE is $',total_nonmember_outside)
