# imported the requests library 
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
 
#URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save 
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
        '''
        Saving recieved content as a png file in binary format
        '''
         
        #write the contents of the response (r.content) 
        # to a new file in binary mode.
        f.write(r.content)
