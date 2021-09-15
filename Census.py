census = {}
s = ' '
listOfFamilys = {}
numberOfPersons = int(input('how many people live in this house?'))
personNumber = 1
familyNumber = 0
for list2 in range(numberOfPersons):
    personalProfile = []
    print(f'Hellow Person number {personNumber} Please enter your information as requested!')
    personNumber += 1
    firstAndLastName = input('Enter your first and last name,\nand use space between them!')
    age = int(input('how old are you?'))
    jender = input('Enter Your Jender.\nf for females.\nm for males.\nu for unknownjender.')
    personalProfile.append(firstAndLastName)
    personalProfile.append(age)
    if jender == 'f':
        personalProfile.append('female')
    elif jender == 'm':
        personalProfile.append('male')
    else:
        personalProfile.append('jender is unknown')
    if age >= 18:
        education = input('Enter your education level')
        personalProfile.append(education)
        job = input('Do you have any job?\nyes or no.')
        if job == 'yes':
            jobName = input('what is your job?')
            print(f'How much is your salary as a {jobName}?')
            monthlySalary = input()
            personalProfile.append(jobName)
            personalProfile.append(monthlySalary)
        marriage = input('are you married?\nyes or no.')
        if marriage == 'yes':
            personalProfile.append('married')
            householder = input('are you householder?\nyes or no.')
            if householder == 'yes':
                personalProfile.append('householder')
            if marriage == 'yes' and householder == 'yes':
                for family in range(1):
                    familyMembers = []
                    familyMembers.append(firstAndLastName + ' is householder')
                    familyNumber += 1
                    spouse = input('Do you livewith your spouse?\nyes or no.')
                    if spouse == 'yes':
                        spouseName = input('Enter First and Last Name of your spouse.')
                        familyMembers.append(spouseName + ' is spouse')
                    else:
                        reasonDoNotLiveWithSpouse = input('The reason don\'t live with your spouth is the divorce or death of your spouse?\ndivorce or death.')
                        if reasonDoNotLiveWithSpouse == 'divorce':
                            familyMembers.append('spouse is divorced')
                        elif reasonDoNotLiveWithSpouse == 'death':
                            familyMembers.append('spouse is dead')
                    children = input('Do you have children?\nyes or no.')
                    if children == 'yes':
                        howManyChildren = int(input('how many children do you have?'))
                        childNumber = 1
                        for child in range(howManyChildren):
                            print(f'Enter first and last name of child number {childNumber}!')
                            childName = input()
                            familyMembers.append(childName + ' child_' + str(childNumber))
                            childNumber += 1
                    listOfFamilys.update({'Family_' + str(familyNumber): familyMembers,})
    census.update({'Person Number_' + str(personNumber): personalProfile,})
print(census)
print(f'{familyNumber}.Family live in this house.')
print(listOfFamilys)
