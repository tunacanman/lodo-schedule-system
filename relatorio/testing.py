
class Schedules(dict):

    counter = 0

    def testing(self):
        Schedules.counter += 1
        if (Schedules.counter == 2) or (Schedules.counter == 3):
            return True
        else:
            return False

    def content(self):
        monthName = "January"
        print(monthName)


sched = Schedules(customer={'name': 'poop'},
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
                    {'start': '2019-1-16',
                    'end': '2019-2-13',
                    'length': '4 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$180',
                    'city': 'Upland',
                    'preregister': 'Pre-Registration Required! Call (999) 555-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2018-12-12',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2018-12-12',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'},
                    {'start': '2018-12-12',
                    'end': '2018-12-13',
                    'length': '6 weeks',
                    'course': 'Beg. Obedience',
                    'price': '$140',
                    'city': 'Glendora',
                    'preregister': 'Pre-Registration Required! Call (999) 222-3333',
                    'time': '6PM - 7PM',
                    'address': '555 A St, 98821',
                    'note': 'No dogs at first meeting!'}])


o = Schedules()

for x in 'xxxxx':
    if o.testing():
        o.content()