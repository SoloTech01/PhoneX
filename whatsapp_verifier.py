import webbrowser

def verifier(number):
	if not number.startswith("+"):
		number = "+" + number
	link = "https://wa.me/" + number
	webbrowser.open(link)