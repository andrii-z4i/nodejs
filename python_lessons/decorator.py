# Device := {phone, large display phone, tablet}
# Features := {wi-fi, 3g, advertisement}  
# 3 * (2^3) = 24 devices
# class phone
# class large_display(phone) <- feature
# class tablet(phone) 
# class wi_fi(phone) 
# class wi_fi2(large_display) 

# ==========IDevice=====================
# ^			^				^			^
# |			|				|			|
# Phone   LDPhone 		Tablet 		FeatureDecorator(depends IDevice)
#										^
#										|
#				=========================
#				 ^		  ^				^
#				 |		  |				|
#				WiFi 	 3G        Advertisement
from abc import ABCMeta, abstractmethod

class IDevice(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def turn_on(self):
		pass

	@abstractmethod
	def turn_off(self):
		pass

	@abstractmethod
	def do_call(self):
		pass	

class Phone(IDevice):

	def __init__(self):
		super(Phone, self).__init__()
		print "I am phone"

	def turn_on(self):
		print "I am turning on..."	

	def turn_off(self):
		print "I am turning off..."	

	def do_call(self):
		print "I am calling..."	

class LDPhone(IDevice):

	def __init__(self):
		super(LDPhone, self).__init__()
		print "I am large display phone"

	def turn_on(self):
		print "I am turning on..."	

	def turn_off(self):
		print "I am turning off..."	

	def do_call(self):
		print "I am calling..."	

class FeatureDecorator(IDevice):
	__metaclass__ = ABCMeta

	def __init__(self, idevice):
		super(FeatureDecorator, self).__init__()
		self._device = idevice 
		self.feature_description()

	@abstractmethod
	def feature_description(self):
		pass

# a = WiFi()

class WiFi(FeatureDecorator):

	def __init__(self, idevice):
		super(WiFi, self).__init__(idevice)

	def _search_for_wifi_networks(self):
		print "Searching for available wifi networks..."

	def feature_description(self):
		print "I can communicate by WiFi"

	def turn_on(self):
		self._device.turn_on()
		self._search_for_wifi_networks()

	def turn_off(self):
		self._device.turn_off()

	def do_call(self):
		self._device.do_call()

class Advertisement(FeatureDecorator):

	def __init__(self, idevice):
		super(Advertisement, self).__init__(idevice)

	def _push_to_buy_device_by_showing_ad(self):
		print "Buy our lux device to hide this ad..."

	def feature_description(self):
		print "I am boring user showing the advertisement..."

	def turn_on(self):
		self._device.turn_on()

	def turn_off(self):
		self._device.turn_off()

	def do_call(self):
		self._push_to_buy_device_by_showing_ad()
		self._device.do_call()

# client 1
print "client 1"
phone_with_wifi_and_advertisement = WiFi(Advertisement(Phone()))

phone_with_wifi_and_advertisement.turn_on()
phone_with_wifi_and_advertisement.do_call()
phone_with_wifi_and_advertisement.turn_off()

# client 2
print "client 2"
large_display_phone_with_ad_and_wifi = Advertisement(WiFi(LDPhone()))
large_display_phone_with_ad_and_wifi.turn_on()
large_display_phone_with_ad_and_wifi.do_call()
large_display_phone_with_ad_and_wifi.turn_off()

#client 3
print "client 3"
phone_with_wifi = WiFi(Phone())
phone_with_wifi.turn_on()
phone_with_wifi.do_call()
phone_with_wifi.turn_off()

