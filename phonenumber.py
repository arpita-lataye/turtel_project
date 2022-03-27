import phonenumbers
from p_test_number import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))