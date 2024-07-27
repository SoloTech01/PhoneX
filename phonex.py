import colorama, time, os, sys
from pathlib import Path
from phonenumbers import parse,carrier,geocoder,timezone,is_valid_number
import number_gen as ng
import whatsapp_verifier as wv


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
[+] Version: 1.1
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
	print("xxxxxx" * 11)
	print(f"""{YELLOW}
[1] Validate Phone number
[2] Get info about phone number
[3] Generate phone numbers
[4] Validate whatsapp number
[5] Update tool
[6] Exit the tool {RESET}
""")
	option = input(f"{GREEN}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter a number>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}").strip()
	if option == "1":
		validate()
	elif option == "2":
		get_info()
	elif option == "3":
		os.system("clear")
		print(f"""{BLUE}
	
█▄─▄▄─█─█─█─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▀─▄█
██─▄▄▄█─▄─█─██─██─█▄▀─███─▄█▀██▀─▀██
▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄█▄▄▀
{RESET}""")
		print(f""" {GREEN}
[1] Nigeria
[2] USA
[3] UK
[4] Canada
[5] Austrailia
[6] India
[7] Germany
[8] China
""")
		country = input(f"{LB}<<<<<<<<<<<<<<<<Choose a valid option>>>>>>>>>>>>>>>>>>>").strip()
		if country == "1":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_nigeria_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
			
		elif country == "2":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_usa_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
				
		elif country == "3":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_uk_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
				
		elif country == "4":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_canada_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
				
		elif country == "5":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_austrailia_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
				
		elif country == "6":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_india_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
				
		elif country == "7":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_germany_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
	
		elif country == "8":
			valid = False
			while not valid:
				try:
					num = int(input(f"\n{YELLOW}Enter number of phone numbers to generate:{RESET} "))
					valid = True
				except ValueError:
					print(f"{RED}Enter a valid integer!!")
			print(f"{GREEN}Generating.......")
			time.sleep(2)
			
			for number in range(0, num):
				numbers_generated = ng.gen_china_number()
				print(numbers_generated)
				
			print("\n[+] Copy and save the phone numbers generated")
			
			prompt = input(f"{LB}Do you want to continue (y/n):{RESET} ").lower().strip()
			if prompt == "y":
				program_intro()
			elif prompt == "n":
				sys.exit()
			else:
				print("invalid prompt!")
				sys.exit()
	
	elif option == "4":
		time.sleep(1)
		print(f"{GREEN}[✓] Make sure whatsapp is installed on your device")
		phone_number = input(f"{YELLOW}Enter a phone number with country code:{RESET} ")
		print(".......")
		time.sleep(1)
		wv.verifier(phone_number)
				
	elif option == "5":
		print(f"{GREEN}Updating PhoneX.....{RESET}")
		time.sleep(2)
		os.system("""
		cd -
		rm -rf PhoneX
		git clone https://github.com/SoloTech01/PhoneX.git
		cd PhoneX
		python3 phonex.py
			""")
	elif option == "6":
		print(RED)
		print("Terminating....")
		time.sleep(2)
		print(RESET)
		sys.exit()

program_intro()