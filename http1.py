import urllib.request
a_url = "http://stackoverflow.com/"
data = urllib.request.urlopen(a_url).read()
print(data)