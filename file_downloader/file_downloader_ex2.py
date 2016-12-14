import requests
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
 
r = requests.get(file_url, stream = True)
 
with open("python.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)
