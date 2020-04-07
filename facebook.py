import webbrowser, sys

if len(sys.argv )> 1:
	friend = ''.join(sys.argv[1:]).lower()
	webbrowser.open('https://www.facebook.com/' + friend)