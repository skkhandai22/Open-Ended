def children_encoding(children):

    if children == '0':
        return 0
    elif children == '1':
        return 1 
    elif children== '2':
        return 2
    elif children =='3':
        return 3
    else :return 4    
def age_encoding(age):
    if age == '18-21':
        return 0
    elif age == '22-25':
        return 1
    elif age == '26-30':
        return 2
    elif age =='31-35':
        return 3
    elif age =='36-40':
        return 4
    elif age == '41-45':
        return 5
    elif age =='45-50':
        return 6
    elif age =='51-55':
        return 7
    elif age =='55-60':
        return 8
    elif age =='61-65':
        return 9
    elif age =='65-70':
        return 10
    elif age == '71 and above':
        return 11
    else:                           #unknown
        return 12
def occupation_encoding(occupation):
    if occupation == 'Professional':
        return 4
    elif occupation =='Secretarial/Admin':
        return 6
    elif occupation =='Manual Worker':
        return 2
    elif occupation == 'Housewife':
        return 1
    elif occupation== 'retired':
        return 5
    elif occupation == 'Other':
        return 3
    elif occupation =='Unknown':
        return 8
    elif occupation=='Business Manager':
        return
    else:
        return 7                          #'Student'
def partner_occupation_encoding(partner_occupation):
    if partner_occupation == 'Professional':
        return 4
    elif partner_occupation =='Secretarial/Admin':
        return 6
    elif partner_occupation=='Manual Worker':
        return 2
    elif partner_occupation=='Housewife':
        return 1
    elif partner_occupation=='Retired':
        return 5
    elif partner_occupation == 'Other':
        return 3
    elif partner_occupation== 'NA':
        return 8
    elif partner_occupation == 'Business Manager':
        return 0
    else:
        return 7                              #'Student'
def home_encoding(home):
    if home == 'Own Home':
        return 1
    elif home == 'Rent Privately':
        return 2
    elif home =='Rent from Council/HA':
        return 3
    elif home =='Live in Parental Hom':
        return 0
    else:
        return 4                       

def family_encoding_encoding(family_income):
    if family_income== '>=35,000':
        return 11
    elif family_income == '<22,500, >=20,000':
        return 7
    elif family_income== '<25,000, >=22,500':
        return 8
    elif family_income =='<30,000, >=27,500':
        return 10
    elif family_income =='<20,000, >=17,500':
        return 6
    elif family_income == '<27,500, >=25,000':
        return 9
    elif family_income == '< 4,000':
        return 0 
    elif family_income == '<15,000, >=12,500':
        return 4
    elif family_income =='<17,500, >=15,000':
        return 5
    elif family_income=='< 8,000, >= 4,000':
        return 1
    elif family_income=='<12,500, >=10,000':
        return 3
    elif family_income=='<10,000, >= 8,000':
        return 2
    else:
        return  12                            #'Unknown