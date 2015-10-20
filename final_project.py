# Buzzfeed-Like questionnaire that will help you choose your next vacation destination based on the answers provided - #API 
# city ID - write a method to return a dictionary with the values for Expedia

from urllib2 import urlopen
from json import load
import md5
import time


# Creating my class of cities

class City(object):
	def __init__ (self,name,province,attributes):
		self.name = name
		self.province = province
		self.attributes = attributes

# Creating my city instances with 5 attributes
SF = City('San Francisco','California',['Golden Gate Bridge','The Painted Ladies','California Academy of Science','California-style Cuisine','Cable Cars'])
NYC = City('New York City','New York',['Empire State Building','Statue of Liberty','Broadway','New York-style Pizza','Museum of Modern Art'])
T = City('Tokyo','Japan',['Tokyo Tower', 'Shinjuku Zen Garden/Park','Harajuku Shopping District','Sushi','Cherry Blossom Watching'])
TPE = City('Taipei','Taiwan',['Taipei 101', 'Night Markets','Sun Yat Sen Memorial','Chicken-Fried Steak','Hiking Elephant Mountain'])
P = City('Paris','France',['Eiffel Tower','Sacre-Couer','Mona Lisa painting','Crepes','Palace of Versailles'])
B = City('Barcelona','Spain',['Sagrada Familia','Gothic Quarter','Casa Batllo','Tapas and Sangria','Architecture'])

# Creating dictionary and list name to reference attractions easily once quiz questions are over
city_dict = {'SF':SF,'NYC':NYC,'TP': TPE ,'T':T,'P':P,'B':B}

# API function to produce list of hotels from Expedia
def find_hotels(city, country, state):
	service = "http://api.ean.com/ean-services/rs/hotel/"
	version = "v3/"
	method = "list"
	other_elements = "&cid=496231&customerIpAddress=50.148.140.1&customerUserAgent=OSX10.9.5&customerSessionId=123456&minorRev=30&locale=en_US&currencyCode=USD"
	response_type = "json"
	API_KEY = "###############"
	API_secret= "##############"
	hash = md5.new()
	timestamp = str(int(time.time()))
	signature = md5.new(API_KEY + API_secret + timestamp).hexdigest()
	city = "%s" % (city)
	countryCode = "%s" % (country)
	state = "%s" % (state)

	print '\n------------------------------\nCheck out this list of hotel suggestions\n------------------------------'
	hotel_url = service + version + method + '?apiKey=' + API_KEY + '&sig=' + signature + '&_type=' + response_type + other_elements + '&city=' + city + '&countryCode=' + countryCode + '&stateProvinceCode=' + state 
	response = urlopen(hotel_url)
	json_response = load(response)
	firstSix = json_response['HotelListResponse']['HotelList']['HotelSummary'][0:6]

	for hotels in firstSix:
		print "\nHotel Name: ", hotels["name"]
		print "Address: ", hotels["address1"]
		print "Rating: ", hotels["hotelRating"]
		print "Location: ", hotels["locationDescription"]
	exit()


# #Introduction of your questionnaire
name = raw_input('What is your name?')

start_question = raw_input('%s, are you ready to find out where your next vacation destination should be?' %(name))

# #Anticipating all types of responses from user 
responses = ('yes','Yes','Yup','yup','sure','Sure','yea','Yea')

if start_question in responses:
	print "\nLet's take this quiz to find out where you should go then!\nMake sure to type your response exactly as you see it in the question."
else: 
	print "Aw, that's too bad - don't be adventurous then!"	
	exit()


first_question = raw_input('\n\nWould you like your next vacation destination to be in the US, Asia, or Europe? Choose one.')

def travel_response(first_question):
	if first_question == 'US' or first_question == ' US': 

		sf_tuple = ('farm-fresh food','bridges','go to an aquarium','smaller cities')
		nyc_tuple = ('pizza','tall buildings','watch a musical','larger cities')

		dom_response_list = []

		first_dom_question = raw_input('Choose your preference - farm-fresh food or pizza?')
		dom_response_list.append(first_dom_question)
		
		second_dom_question = raw_input('What would you find more exhilarating - bridges or tall buildings?')
		dom_response_list.append(second_dom_question)
		
		third_dom_question = raw_input('What would you prefer to do on a Saturday evening - watch a musical or go to an aquarium?')
		dom_response_list.append(third_dom_question)
		
		fourth_dom_question = raw_input('Lastly, do you prefer smaller cities or larger cities?')
		dom_response_list.append(fourth_dom_question)
	
		sf_counter = 0
		nyc_counter = 0

		for responses in dom_response_list: 
			if responses in sf_tuple:
				sf_counter += 1
			else: 
				nyc_counter += 1

		if sf_counter > nyc_counter: 
			print "You should go to San Francisco!\nHere are a list of attractions you may be interested in: " + ', '.join(SF.attributes)
			hotels = find_hotels("San%20Francisco","US","California")
			return hotels 
		else: 
			print "You should go to New York City!\nHere are a list of attractions you may be interested in: " + ', '.join(NYC.attributes)
			hotels = find_hotels("New%20York%20City","US","New%20York")
			return hotels 

	elif first_question =='Asia' or first_question == ' Asia':

		taipei_tuple = ('fried chicken','food','hike')
		tokyo_tuple = ('sushi','fashion','flower garden')

		asia_response_list = []

		tp_counter = 0
		tokyo_counter = 0

		first_asia_question = raw_input('Choose your preference - sushi or fried chicken?')
		asia_response_list.append(first_asia_question)

		second_asia_question = raw_input('Do you tend to spend your money on fashion or food?')
		asia_response_list.append(second_asia_question)

		third_asia_question = raw_input('Would you prefer to go to a flower garden or go on a hike?')
		asia_response_list.append(third_asia_question)

		for responses in asia_response_list: 
			if responses in taipei_tuple:
				tp_counter += 1
			else: 
				tokyo_counter += 1

		if tp_counter > tokyo_counter:
			print "You should go to Taipei!\nHere are a list of attractions you may be interested in: " + ', '.join(TPE.attributes)
			hotels = find_hotels("Taipei","TW",None)
			return hotels 
		else: 
			print "You should go to Tokyo!\nHere are a list of attractions you may be interested in: " + ', '.join(T.attributes)
			hotels = find_hotels("Tokyo","JP",None)
			return hotels

	else: 

		paris_tuple = ('duck','classic art','a palace','chocolate')
		barce_tuple = ('seafood','gothic architecture','a grand church','flan')

		euro_response_list = []

		paris_counter = 0
		barce_counter = 0

		first_euro_question = raw_input('Choose your preference - seafood or duck?')
		euro_response_list.append(first_euro_question)

		second_euro_question = raw_input('What would you find more interesting - classic art or gothic architecture?')
		euro_response_list.append(second_euro_question)

		third_euro_quesion = raw_input('What would you like to see more - a grand church or a palace?')
		euro_response_list.append(third_euro_quesion)

		fourth_euro_question = raw_input('Choose a dessert - chocolate or flan?')
		euro_response_list.append(fourth_euro_question)

		for responses in euro_response_list: 
			if responses in paris_tuple:
				paris_counter += 1
			else: 
				barce_counter += 1

		if paris_counter > barce_counter:
			print "You should go to Paris!\nHere are a list of attractions you may be interested in: " + ', '.join(P.attributes) 
			hotels = find_hotels("Paris","France",None)
			return hotels 
		else: 
			print "You should go to Barcelona!\nHere are a list of attractions you may be interested in: " + ', '.join(B.attributes)
			hotels = find_hotels("Barcelona","Spain",None)
			return hotels

print travel_response(first_question)



		










