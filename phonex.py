import colorama
import time
import os
import sys
from phonenumbers import parse,carrier,geocoder,timezone,is_valid_number

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
LB = colorama.Fore.LIGHTBLUE_EX
RED = colorama.Fore.RED

def validate():
	valid = False
	while not valid:
		try:
			number = input(f"{LB}Enter a phone number with country code: {RESET}")
			parsed = parse(number, None)
			valid = True
		except:
			print(f"{RED}An error occurred!{RESET}")
			print(f"{GREEN}-Ensure you input + and country code then phone number{RESET}")
		else:
			if is_valid_number(parsed) is True:
				print(f"{GREEN}Validating.....")
				time.sleep(3)
				print(f"[✓]{number} is a valid phone number{RESET}")
			elif is_valid_number(parsed) is False:
				print(f"{GREEN}Validating.....")
				time.sleep(3)
				print(f"{RED}[x]{number} is not a valid phone number{RESET}")
			time.sleep(2)
			print(f"{LB}Refreshing.....{RESET}")
			time.sleep(6)

def get_info():
	valid = False
	while not valid:
		try:
			number = input(f"{LB}Enter a phone number with country code: {RESET}")
			parsed = parse(number, None)
			valid = True
		except:
			print(f"{RED}An error occurred!{RESET}")
			print(f"{GREEN}-Ensure you input + and country code then phone number{RESET}")
		else:
			region = geocoder.description_for_number(parsed, "en")
			zone = timezone.time_zones_for_number(parsed)
			isp = carrier.name_for_number(parsed, "en")
			print(f"{GREEN}Fetching info.......")
			time.sleep(3)
			print(f"""
[✓]-PHONE NUMBER: {parsed}
[✓]-REGION: {region}
[✓]-TIMEZONE: {zone}
[✓]-INTERNET SERVICE PROVIDER(ISP): {isp} {RESET}
""")
			time.sleep(2)
			print(f"{LB}Refreshing.....{RESET}")
			time.sleep(12)

def program_intro():
	os.system("clear")
	print(f"""{BLUE}
	
█▄─▄▄─█─█─█─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▀─▄█
██─▄▄▄█─▄─█─██─██─█▄▀─███─▄█▀██▀─▀██
▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄█▄▄▀
{RESET}""")

	print(f"""{GREEN}
[+] Tool name: PhoneX
[+] Author: Solomon Adenuga
[+] Version: 1.0
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
	print("xxxxxx" * 11)
	print(f"""{YELLOW}
[1] Validate Phone number
[2] Get info about phone number
[3] Update tool
[4] Exit the tool {RESET}
""")
	option = input(f"{GREEN}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter a number>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}")
	if option.strip() == "1":
		validate()
	elif option.strip() == "2":
		get_info()
	elif option.strip() == "3":
		print(f"{GREEN}Updating PhoneX.....{RESET}")
		time.sleep(2)
		os.system("""
		cd -
		rm -rf PhoneX
		git clone https://github.com/SoloTech01/PhoneX.git
		cd PhoneX
		python3 phonex.py
			""")
	elif option.strip() == "4":
		print(RED)
		print("Terminating....")
		time.sleep(2)
		print(RESET)
		sys.exit()
	
while True:
	program_intro()