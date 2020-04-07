import webbrowser, sys

if len(sys.argv) > 1:
	address = '+'.join(sys.argv[1:])
	S = "www.google.com/"
	S = S + str(address) + '/'
	webbrowser.open('https://www.google.com/maps/place/' + address)