# Buzzfeed-Like questionnaire that will help you choose your next vacation destination based on the answers provided - #API 

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
city_dict = {'SF':SF,'NYC':NYC,'T':T,'P':P,'B':B}

# #Introduction of your questionnaire
name = raw_input('What is your name?')

start_question = raw_input('%s, are you ready to find out where your next vacation destination should be?' %(name))

# #Anticipating all types of responses from user 
responses = ('yes','Yes','Yup','yup','sure','Sure','yea','Yea')

if start_question in responses:
	print "Let's take this quiz to find out where you should go then!\nMake sure to type your response exactly as you see it in the question."
else: 
	print "Aw, that's too bad - don't be adventurous then!"	
	exit()

# # Five questions to start and then add various combinations of answers to produce destination

first_question = raw_input('\n\nWould you like your next vacation destination to be in the US, Asia, or Europe? Choose one.')


def travel_response(first_question):
	if first_question == 'US' or first_question == ' US': 

		sf_tuple = ('farm-fresh food','bridges','go to an aquarium','smaller cities')
		nyc_tuple = ('pizza','tall buildings','watch a musical','larger cities')

		response_list = []

		first_dom_question = raw_input('If you had to choose your last meal, would it be pizza or farm-fresh food?')
		response_list.append(first_dom_question)
		
		second_dom_question = raw_input('What would you find more exhilarating - bridges or tall buildings?')
		response_list.append(second_dom_question)
		
		third_dom_question = raw_input('What would you prefer to do on a Saturday evening - watch a musical or go to an aquarium?')
		response_list.append(third_dom_question)
		
		fourth_dom_question = raw_input('Lastly, do you prefer smaller cities or larger cities?')
		response_list.append(fourth_dom_question)
	
		sf_counter = 0
		nyc_counter = 0

		for responses in response_list: 
			if responses in sf_tuple:
				sf_counter += 1
			else: 
				nyc_counter += 1

		if sf_counter > nyc_counter: 
			return "You should go to San Francisco!\nHere are a list of attractions you may be interested in:" + str(SF.attributes).join 
			# Figure out how to use join method
		else: 
			return "You should go to New York City!"

	# elif first_question=='Asia' or first_question == ' Asia':

	# 	taipei_tuple = ('fried chicken','food','hike')
	# 	tokyo_tuple = ('sushi','fashion','flower garden')

	# 	first_asia_question = raw_input('Sushi or fried chicken?')
	# 	second_asia_question = raw_input('Do you spend your money more on fashion or food?')
	# 	third_asia_question = raw_input('Would you prefer to go to a flower garden or go on a hike?')

print travel_response(first_question)




		










