# Buzzfeed-Like questionnaire that will help you choose your next vacation destination based on the answers provided - #API 

# Creating my class of cities
class City(object):
	def __init__ (self,name,province,attributes):
		self.name = name
		self.province = province
		self.attributes = attributes
	def show_attractions(self,list_attributes):
		print self.attributes

# Creating my city instances with 5 attributes
SF = City('San Francisco','California',['Golden Gate Bridge','The Painted Ladies','California Academy of Science','California-style Cuisine','Cable Cars'])
NYC = City('New York City','New York',['Empire State Building','Statue of Liberty','Broadway','New York-style Pizza','Museum of Modern Art'])
T = City('Tokyo','Japan',['Tokyo Tower', 'Shinjuku Zen Garden/Park','Harajuku Shopping District','Sushi','Cherry Blossom Watching'])
TPE = City('Taipei','Taiwan',['Taipei 101', 'Night Markets','Sun Yat Sen Memorial','Chicken-Fried Steak','Hiking Elephant Mountain'])
P = City('Paris','France',['Eiffel Tower','Sacre-Couer','Mona Lisa painting','Crepes','Palace of Versailles'])
B = City('Barcelona','Spain',['Sagrada Familia','Gothic Quarter','Casa Batllo','Tapas and Sangria','Architecture'])

# Creating dictionary to reference attractions easily once quiz questions are over
# city_list = {'SF': 'San Francisco','NYC':'New York City','T':'Tokyo','P':'Paris','B':'Barcelona'}

# #Introduction of your questionnaire
name = raw_input('What is your name?')

start_question = raw_input('%s, are you ready to find out where your next vacation destination should be?' %(name))

# #Anticipating all types of responses from user 
responses = ('yes','Yes','Yup','yup','sure','Sure')

if start_question in responses:
	print "Great! Let's take this quiz to find out where you should go!"
else: 
	print "Aw, that's too bad - don't be adventurous then!"	
	exit()

# # Five questions to start and then add various combinations of answers to produce destination

first_question = raw_input('Would you like your next vacation destination to be in the U.S., Asia, or Europe?')

def domestic_travel(first_question):
	if first_question=='U.S.': 

		sf_tuple = ('farm-fresh food','suspension bridge','aquarium','smaller cities')
		nyc_tuple = ('pizza','100-story buildings','musical','larger cities')

		sf_counter = 0
		nyc_counter = 0

		first_dom_question = raw_input('If you had a life/death choice to choose between eating pizza for the rest of your life or eating farm-fresh food, what would you choose?')
		second_dom_question = raw_input('What would you find more exhilarating - a suspension bridge or 100-story buildings?')
		third_dom_question = raw_input('What would you prefer to do on a Saturday evening - watch a musical or go to an aquarium?')
		fourth_dom_question = raw_input('Lastly, do you prefer smaller cities or larger cities?')

		response_list = ['%s','%s','%s','%s'] % (first_mini_question,second_mini_question,third_mini_question,fourth_mini_question)

		for responses in response_list: 
			if responses in sf_tuple:
				sf_counter += 1
			else: 
				nyc_counter += 1

		if sf_counter > nyc_counter: 
			print "You should go to San Francisco"
		else: 
			print 'You should go to New York City'

		
	else: 
		print "Good to know! Let's move on!"

print domestic_travel(first_question)

def international_travel(first_question):
	if first_question=='internationally':

		










