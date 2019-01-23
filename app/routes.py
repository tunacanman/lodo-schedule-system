from app import app
from flask import render_template, request, jsonify
from relatorio.templates.opendocument import Template

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
@app.route('/index', methods = [ 'GET', 'POST'])
def form():
    if request.method == 'POST':
            classData = request.get_json(force=True)

            class Schedules(dict):

                testingCounter = 0
                contentCounter = -1
                yearCounter = -1
                monthIntervals = [1]
                monthNames = []
                years = []

                def __init__(self, classData):
                    self.classData = classData
                
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


                monthNames.append(monthNumberToName(classData[0]['start'][5:7]))
                years.append(classData[0]['start'][0:4])

                monthIntervalsCounter = 1
                for index, item in enumerate(classData):
                    monthIntervalsCounter += 1
                    try:
                        if item['start'][5:7] != classData[index + 1]['start'][5:7]:
                            monthIntervals.append(monthIntervalsCounter)
                            monthNames.append(monthNumberToName(classData[index + 1]['start'][5:7]))
                            # if item['start'][0:4] != classData[index + 1]['start'][0:4]:
                            years.append(classData[index + 1]['start'][0:4])
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


            sched = Schedules(classData)
            
            basic = Template(source='', filepath='template-schedules.odt')
            open('app/static/generated-iftest.odt', 'wb').write(basic.generate(o=sched).render().getvalue())

            return str(classData)
    return render_template('form.html')


#                                 [{'start': '2018-12-12',
#                                 'end': '2018-12-13',
#                                 'length': '6 weeks',
#                                 'course': 'Beg. Obedience',
#                                 'price': '$140',
#                                 'city': 'Glendora',
#                                 'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                                 'time': '6PM - 7PM',
#                                 'address': '555 A St, 98821',
#                                 'note': 'No dogs at first meeting!'},
#                                 {'start': '2019-01-16',
#                                 'end': '2019-02-13',
#                                 'length': '4 weeks',
#                                 'course': 'Beg. Obedience',
#                                 'price': '$180',
#                                 'city': 'Upland',
#                                 'preregister': 'Pre-Registration Required! Call (999) 555-3333',
#                                 'time': '6PM - 7PM',
#                                 'address': '555 A St, 98821',
#                                 'note': 'No dogs at first meeting!'},
#                                 {'start': '2019-01-16',
#                                 'end': '2018-12-13',
#                                 'length': '6 weeks',
#                                 'course': 'Beg. Obedience',
#                                 'price': '$140',
#                                 'city': 'Glendora',
#                                 'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                                 'time': '6PM - 7PM',
#                                 'address': '555 A St, 98821',
#                                 'note': 'No dogs at first meeting!'},
#                                 {'start': '2019-01-18',
#                                 'end': '2018-12-13',
#                                 'length': '6 weeks',
#                                 'course': 'Beg. Obedience',
#                                 'price': '$140',
#                                 'city': 'Glendora',
#                                 'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                                 'time': '6PM - 7PM',
#                                 'address': '555 A St, 98821',
#                                 'note': 'No dogs at first meeting!'},
#                                 {'start': '2019-02-16',
#                                 'end': '2018-12-13',
#                                 'length': '6 weeks',
#                                 'course': 'Beg. Obedience',
#                                 'price': '$140',
#                                 'city': 'Glendora',
#                                 'preregister': 'Pre-Registration Required! Call (999) 222-3333',
#                                 'time': '6PM - 7PM',
#                                 'address': '555 A St, 98821',
#                                 'note': 'No dogs at first meeting!'}]