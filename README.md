Image Management API dkfngldfv klfsdf

This is a Django based RESTful service that can be used to store, update, retrieve and delete images. The image will be stored on the file-system where this service lives.

Steps:dsmklv s 
-----

1. Clone or download the repository.
2. Open project folder. sdfgsd 
3. Open command prompt(admin) in that location.
4. Type python manage.py get_access_key to get token to access the API. This access key will be used to authenticate all API calls.
5. Type python manage.py runserver to get run the s sf sdfsderver.

Now, a user can store, update, retrieve and delete images through the API using the token key provided to him.
d fsd sd
The requests can be made using curl or Postman.

Functionalities: sdf sd s
---------------
(All the functionalities mentioned below were tested using Postman. Please use token key to perform these functionalities. )

1. To upload image:

Method : POSTdf dsf sdf 
URL : http://127.0.0.1:8000/image/
Header : {'Authorization' : 'Token token_key'}
Body : form-data : key=image, type=file, value=filename.extensionfd sfdss 

(Note: sdf sdfds 
	1. The uploaded file must be a valid image file, else it will not be uploaded.dfs d

 fsdfsd

  fds 
  fds

Method : GET 	
URL :  http://127.0.0.1:8000/image/
Header : {'Authorization' : 'Token token_key'}

The API will return a list of all image files linked to the given token key.

3. To display(render) a particular image:

Method : GET 	 sdsdfsd
URL :  http://127.0.0.1:8000/image/image_name.extension/
Header : {'Authorization' : 'Token token_key'}

4. To update a particular image:

Method : PATCH 	
URL :  http://127.0.0.1:8000/image/image_name.extension/
Header : {'Authorization' : 'Token token_key'}
Body : form-data : key=image, type=file, value=filename.extension		

5. To delete a particular image:

Method : DELETE 	
URL :  http://127.0.0.1:8000/image/image_name.extension/
Header : {'Authorization' : 'Token token_key'}

Also, if the user wishes to get the token key linked to his username:

Method : POST 	
URL :  http://127.0.0.1:8000/api/token/
Header : key = Content-Type, value=application/x-www-form-urlencoded
Body : x-www-form-urlencoded : 
key=username, value ='username'
key=password, value ='password'
	
For any clarification, mail me to : skrch96@gmail.com

