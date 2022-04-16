# import phonenumbers
# from test import number

# from phonenumbers import geocoder

# ch_number = phonenumbers.parse(number,"CH")
# print(geocoder.description_for_number(ch_number, "en"))

import trunofficial

owner = trunofficial.search('____mobile no----') #2024561111
print(owner.name)

mobile = owner.phone
print(mobile.number)
print(mobile.countrycode)
print(mobile.carrier)

house = owner.address
print(house.city)
print(house.timezone)