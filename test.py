import requests
urlfile=requests.get("http://7xq5c6.com1.z0.glb.clouddn.com/url.txt").text
urllist=urlfile.split('\n')
for url in urllist:
   header=requests.head(url).headers
   print header['location']