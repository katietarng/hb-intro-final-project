Vacation Questionnaire

What is the program? 
------------
This is a Buzzfeed-style survey that outputs a user's next suggested vacation destination based on their answers to the questions in the survey. Once the user has gone through the flow of the survey and received their destination, the program will output five hotel suggestions provided by Expedia's API. The program is designed to be a fun interactive survey that may help those with wanderlust decide where to plan their next adventure. 

Documentation
-------------
This program does have Expedia's API URL hardcoded into the code. In order for the program to run properly, you will have to register/create an account to receive a customized API key, API secret, and account number which are required for the API. Links for the registration and API documentation are below.

Expedia Affilate Network registration - https://www.ian.com/affiliate/signup/stepOne.jsp?addedBy=bdg<br>
Expedia Hotel List Documentation - http://developer.ean.com/docs/hotel-list

Installation and Running the Application
----------------------------------------
Have a text editor installed and readily available as you will need to change the API key, secret, and Expedia account number in order for this program to run properly. Once you've put in the correct API key, secret, and account number, you can run this application through your computer's Terminal. 

Troubleshooting
---------------
Expedia's API requires a proper HMAC-MD5 hash in order for the request to work. The program already contains a method to hash the required parameters. If the response outputs an error regarding an improper authentication, please use the link below to double check if the hash is working correctly and matches their system. 

http://developer.ean.com/md5-hash-generator/



