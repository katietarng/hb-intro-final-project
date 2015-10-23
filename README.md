Vacation Destination Fun Questionnaire


What is the program? 
------------
This is a Buzzfeed-style survey that outputs a user's next suggested vacation destination based on the answers to the questions in the survey. Once the user has gone through the entire flow of the survey and received their destination, the program will output 5 hotel suggestions provided by Expedia's API. 

Documentation
-------------
This program does have Expedia's API URL hardcoded into the code. In order for the program to run properly, you will have to register/create an account to receive a customized API key, API secret, and account number which are required for the API. Links for the registration and specific portion of the API documentation that I used are below. 

https://www.ian.com/affiliate/signup/stepOne.jsp?addedBy=bdg&
http://developer.ean.com/docs/hotel-list

Troubleshooting
---------------
Expedia's API requires an HMAC-MD5 hash which is hardcoded into the program as well. 
