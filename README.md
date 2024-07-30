**PHONEX FEATURES**

- Check if a phone number is valid

- Get information about a phone number

- Generate random phone numbers for multiple countries

- Check if a phone number is registered on WhatsApp


**OLD VERSIONS**

**1.0**

features:

- validate a phone number

- get information on a specific phone number

**1.1**

Added features: 

- generate phone numbers for different countries (validity of all phone numbers is not guaranteed)

- validate WhatsApp number

**CURRENT VERSION**

**1.2**

Added features: 

- all phone numbers generated using the program exists and are 100% valid (validity of all phone numbers is guaranteed)

- saves phone numbers as a .txt file in both the current working directory and in "/storage/emulated/0/" path in a folder "phonex"

**INSTALLATION OF TERMUX**

Visit f-droid.org/en/packages/com.termux/ and download the termux app

**INSTALLATION OF PHONEX ON TERMUX**

Open termux and input the following commands:

apt update && apt upgrade

pkg install git

pkg install python3

pkg install pip

git clone https://github.com/SoloTech01/PhoneX.git

cd PhoneX

pip install -r requirements.txt

**USING PHONEX ON TERMUX AFTER INSTALLATION**

cd PhoneX

python3 phonex.py

**NOTE**

There will be constant update so as to increase the number of countries available to generate phone numbers for,it's okay to use the update feature regularly to check for updates

**DISCLAIMER**

This program was created for research and educational purposes and should not be used for any illegal activity as I will not be responsible for any misuse

**DON'T FORGET TO LEAVE A STAR✨**