
class Schedules(dict):

    testingCounter = 0
    contentCounter = -1
    yearCounter = -1
    monthIntervals = [1]
    monthNames = []
    years = []

    classes=[{'start': '2018-12-12',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2019-01-16',
                    'end': '2019-02-13',
                    'length': '4 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$180',
                    'city': 'Upland',
                    'preregister': 'Pre-Registration Required! Call (999) 555-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2019-01-16',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2019-01-18',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2019-02-16',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'}]
    
    def monthNumberToName(monthNumber):
        if monthNumber == '01':
            return 'January'
        elif monthNumber == '02':
            return 'February'
        elif monthNumber == '03':
            return 'March'
        elif monthNumber == '04':
            return 'April'
        elif monthNumber == '05':
            return 'May'
        elif monthNumber == '06':
            return 'June'
        elif monthNumber == '07':
            return 'July'
        elif monthNumber == '08':
            return 'August'
        elif monthNumber == '09':
            return 'September'
        elif monthNumber == '10':
            return 'October'
        elif monthNumber == '11':
            return 'November'
        elif monthNumber == '12':
            return 'December'


    monthNames.append(monthNumberToName(classes[0]['start'][5:7]))
    years.append(classes[0]['start'][0:4])

    monthIntervalsCounter = 1
    for index, item in enumerate(classes):
        monthIntervalsCounter += 1
        try:
            if item['start'][5:7] != classes[index + 1]['start'][5:7]:
                monthIntervals.append(monthIntervalsCounter)
                monthNames.append(monthNumberToName(classes[index + 1]['start'][5:7]))
                # if item['start'][0:4] != classes[index + 1]['start'][0:4]:
                years.append(classes[index + 1]['start'][0:4])
        except:
            continue

    @property
    def testing(self):
        Schedules.testingCounter += 1
        for i in Schedules.monthIntervals:
            if Schedules.testingCounter == i:
                return True
        return False

    @property
    def content(self):
        Schedules.contentCounter += 1
        return Schedules.monthNames[Schedules.contentCounter]
    
    @property
    def year(self):
        Schedules.yearCounter += 1
        return Schedules.years[Schedules.yearCounter]


sched = Schedules(customer={'name': 'poop'})

# class Schedules(set):
#     pass

# sched = Schedules(classes={{'January',{'start': '2018-1-12',
#                     'end': '2018-1-13',
#                     'length': '6 weeks',
#                     'course': 'Beg. Obedience',
#                     'price': '$140',
#                     'city': 'Glendora',
#                     'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                     'time': '6PM - 7PM',
#                     'address': '555 A St, 98821',
#                     'note': 'No dogs at first meeting!'},
#                     {'start': '2018-1-12',
#                     'end': '2018-1-13',
#                     'length': '7 weeks',
#                     'course': 'Beg. Obedience',
#                     'price': '$140',
#                     'city': 'Glendora',
#                     'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                     'time': '6PM - 7PM',
#                     'address': '555 A St, 98821',
#                     'note': 'No dogs at first meeting!'}},
#                     {'February',{'start': '2018-2-12',
#                     'end': '2018-2-13',
#                     'length': '6 weeks',
#                     'course': 'Beg. Obedience',
#                     'price': '$140',
#                     'city': 'Glendora',
#                     'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                     'time': '6PM - 7PM',
#                     'address': '555 A St, 98821',
#                     'note': 'No dogs at first meeting!'},
#                     {'start': '2018-2-12',
#                     'end': '2018-2-13',
#                     'length': '7 weeks',
#                     'course': 'Beg. Obedience',
#                     'price': '$140',
#                     'city': 'Glendora',
#                     'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                     'time': '6PM - 7PM',
#                     'address': '555 A St, 98821',
#                     'note': 'No dogs at first meeting!'}}})

# MONTH SECTION HEADERS
# =====================
# Template will have an IF (a function in Data that returns boolean) at the beginning of the for loop
# with content (a function in Data that returns month) that is displayed on True

# Data will have: 
# a function that counts the number of classes in each month
# a function called by Template's IF:
#   initially (counter = 0) it returns true and the content function returns first month
#   the counter increments each time the function is called. when it hits a value corresponding to the start of a new month, it returns true
# a content function called by Template when IF function returns True
#   each time it is called, a counter is incremented and the next month is returned 