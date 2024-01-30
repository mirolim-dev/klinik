from datetime import date
patients_data = [
{
    'username': 'patient61',
    'first_name': 'Emily',
    'last_name': 'Garcia',
    'phone': '4444124444',
    'gender': 0,
    'address': '1011 Pine Lane',
    'date_of_birth': date(1987, 7, 22),
    'insurance_provider': 'Healthway',
    'insurance_policy_number': 'GHI123'
},
{
    'username': 'patient62',
    'first_name': 'David',
    'last_name': 'Lee',
    'phone': '3333312333',
    'gender': 1,
    'address': '2222 Maple Street',
    'date_of_birth': date(1995, 3, 8),
    'insurance_provider': 'PrimeCare',
    'insurance_policy_number': 'JKL456'
},
{
    'username': 'patient63',
    'first_name': 'Maria',
    'last_name': 'Rodriguez',
    'phone': '2222222122',
    'gender': 0,
    'address': '3333 Oak Avenue',
    'date_of_birth': date(1978, 11, 17),
    'insurance_provider': 'Wellbeing',
    'insurance_policy_number': 'MNO789'
},

{
    'username': 'patient64', 
    'first_name': 'William', 
    'last_name': 'Johnson', 
    'phone': '1111111211', 
    'gender': 1, 
    'address': '4444 Elm Drive', 
    'date_of_birth': date(1982, 8, 25), 
    'insurance_provider': 'Harmony Health', 
    'insurance_policy_number': 'PQR012'
},

{
    'username': 'patient65', 
    'first_name': 'Elizabeth', 
    'last_name': 'Davis', 
    'phone': '7777127777', 
    'gender': 0, 
    'address': '5555 Birch Street', 
    'date_of_birth': date(1998, 6, 4), 
    'insurance_provider': 'Vitality', 
    'insurance_policy_number': 'STU345'
},

{
    'username': 'patient66', 
    'first_name': 'Daniel', 
    'last_name': 'Clark', 
    'phone': '6666661266', 
    'gender': 1, 
    'address': '6666 Willow Way', 
    'date_of_birth': date(1975, 2, 14), 
    'insurance_provider': 'ThriveHealth', 
    'insurance_policy_number': 'VWX678'
},

{
    'username': 'patient67', 
    'first_name': 'Anna', 
    'last_name': 'Miller', 
    'phone': '5555125554', 
    'gender': 0, 
    'address': '7777 Poplar Street', 
    'date_of_birth': date(1980, 12, 6), 
    'insurance_provider': 'Serenity', 
    'insurance_policy_number': 'YZ901'
},

{
    'username': 'patient68', 
    'first_name': 'James', 
    'last_name': 'Wilson', 
    'phone': '4444124443', 
    'gender': 1, 
    'address': '8888 Oakwood Lane', 
    'date_of_birth': date(1993, 5, 20), 
    'insurance_provider': 'FlourishCare', 
    'insurance_policy_number': 'ABC1234'
},

{
    'username': 'patient69', 
    'first_name': 'Christine', 
    'last_name': 'Brown', 
    'phone': '3333312332', 
    'gender': 0, 
    'address': '9999 Maple Avenue', 
    'date_of_birth': date(1986, 9, 2)
},
{
    'username': 'patient71', 
    'first_name': 'Sarah', 
    'last_name': 'Jackson', 
    'phone': '7777712776', 
    'gender': 0, 
    'address': '1011 Cherry Lane', 
    'date_of_birth': date(1989, 2, 5), 
    'insurance_provider': 'HealthPlus', 
    'insurance_policy_number': 'GHI456'
},
{
    'username': 'patient72', 
    'first_name': 'Matthew', 
    'last_name': 'Walker', 
    'phone': '6661266665', 
    'gender': 1, 
    'address': '2222 Pine Street', 
    'date_of_birth': date(1996, 10, 12), 
    'insurance_provider': 'Guardian Health', 
    'insurance_policy_number': 'JKL789'
},
{
    'username': 'patient73', 
    'first_name': 'Victoria', 
    'last_name': 'Taylor', 
    'phone': '5555551253', 
    'gender': 0, 
    'address': '3333 Oak Avenue', 
    'date_of_birth': date(1979, 4, 21), 
    'insurance_provider': 'HealthFirst', 
'insurance_policy_number': 'MNO123'},
{
    'username': 'patient74', 
    'first_name': 'Christopher', 
    'last_name': 'Williams', 
    'phone': '4441244442', 
    'gender': 1, 
    'address': '4444 Elm Drive', 
    'date_of_birth': date(1983, 7, 30), 
    'insurance_provider': 'VitalCare', 
    'insurance_policy_number': 'PQR456'
},
{
    'username': 'patient75', 
    'first_name': 'Jennifer', 
    'last_name': 'Davis', 
    'phone': '3333312331', 
    'gender': 0, 
    'address': '5555 Birch Street', 
    'date_of_birth': date(1999, 1, 8), 
    'insurance_provider': 'Harmony Health', 
    'insurance_policy_number': 'STU789'
},
{
    'username': 'patient76', 
    'first_name': 'Andrew', 
    'last_name': 'Clark', 
    'phone': '222132220', 
    'gender': 1, 
    'address': '6666 Willow Way', 
    'date_of_birth': date(1976, 6, 19), 
    'insurance_provider': 'ThriveWell', 
    'insurance_policy_number': 'VWX012'
},
{
    'username': 'patient77', 
    'first_name': 'Katherine', 
    'last_name': 'Miller', 
    'phone': '1132111110', 
    'gender': 0, 
    'address': '7777 Poplar Street', 
    'date_of_birth': date(1981, 5, 15), 
    'insurance_provider': 'Serenity Health', 
    'insurance_policy_number': 'YZ345'
},
{
    'username': 'patient78', 
    'first_name': 'Joseph', 
    'last_name': 'Wilson', 
    'phone': '6666612664', 
    'gender': 1, 
    'address': '8888 Oakwood Lane', 
    'date_of_birth': date(1994, 9, 27), 
    'insurance_provider': 'Flourish Care', 
    'insurance_policy_number': 'ABC5678'
},
{
    'username': 'patient79', 
    'first_name': 'Margaret', 
    'last_name': 'Brown', 
    'phone': '5555512552', 
    'gender': 0, 
    'address': '9999 Maple Avenue', 
    'date_of_birth': date(1987, 3, 3), 
    'insurance_provider': 'Harmony Health', 
    'insurance_policy_number': 'DEF901'
},
]