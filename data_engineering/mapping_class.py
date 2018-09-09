# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:19:21 2018

@author: BrunoAdmin
"""

class Mapper(object):
    
    def __init__(self):
        self.from_service_mapping = {'': "Personal, Permit and Other Services",
                                     'Driver licence': "Car and Motorbike related Service",
                                     'QGAP': "Personal, Permit and Other Services",
                                     'Shop 14 High Range Drive Cannon Park Centre Thuringowa Services: driver licensing': "Car and Motorbike related Service",
                                     'boat licence': "Boat related Service",
                                     'boat license': "Boat related Service",
                                     'boat licensing': "Boat related Service",
                                     'buses': "Public transport",
                                     'driver authorisation': "Car and Motorbike related Service",
                                     'driver licence': "Car and Motorbike related Service",
                                     'driver licence replacements and renewals': "Car and Motorbike related Service",
                                     'driver license': "Car and Motorbike related Service",
                                     'driver licensing': "Car and Motorbike related Service",
                                     'driver tests': "Driving Test",
                                     'driving test bookings': "Driving Test",
                                     'heavy vehicles': "Car and Motorbike related Service",
                                     'heavy vehicles and light vehicles safety inspections': "Car and Motorbike related Service",
                                     'industry licensing': "Business Service",
                                     'industry licensing services': "Business Service",
                                     'learner driver licence test': "Driving Test",
                                     'light vehicles': "Car and Motorbike related Service",
                                     'limousines': "Car and Motorbike related Service",
                                     'motorbikes': "Car and Motorbike related Service",
                                     'motorcycles': "Car and Motorbike related Service",
                                     'operator accreditation': "Personal, Permit and Other Services",
                                     'passenger transport': "Personal, Permit and Other Services",
                                     'passenger transport services': "Personal, Permit and Other Services",
                                     'practical driver testing': "Driving Test",
                                     'practical driver testing bookings': "Driving Test",
                                     'practical driver tests': "Driving Test",
                                     'practical driving test': "Driving Test",
                                     'practical driving tests': "Driving Test",
                                     'practical driving tests for all licence classes except motorcycles': "Driving Test",
                                     'pre-registraion inspections': "Personal, Permit and Other Services",
                                     'pre-registration checks': "Personal, Permit and Other Services",
                                     'pre-registration insepctions': "Car and Motorbike related Service",
                                     'pre-registration inspections': "Car and Motorbike related Service",
                                     'pre-registration inspections (except trailers)': "Car and Motorbike related Service",
                                     'pre-registration inspections for all vehicles': "Car and Motorbike related Service",
                                     'pre-registration inspections for vehicles': "Car and Motorbike related Service",
                                     'pre-registration inspections light vehicles': "Car and Motorbike related Service",
                                     'pre-registration vehicle inspections': "",
                                     'product sales': "Personal, Permit and Other Services",
                                     'registration': "Personal, Permit and Other Services",
                                     'registration of vehicles and vessels': "Car and Motorbike related Service",
                                     'release of information': "General Information Service",
                                     'safety inspections': "Other Services",
                                     'taxis': "Public transport",
                                     'transfer': "Personal, Permit and Other Services",
                                     'vehicle safety inspections': "Car and Motorbike related Service",
                                     'vehicles': "Car and Motorbike related Service"}
        self.from_survey_mapping = {}
        
    def convert(self, keyword):
        custom_category = self.from_service_mapping.get(keyword)
        
        if custom_category == None:
            print('problem')
            return "Personal, Permit and Other Services"
        else:
            return custom_category
