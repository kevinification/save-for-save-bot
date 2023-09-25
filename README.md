## Save for save

#### The main objective for the script is to send save for save messages 
#### The script allows users to send such messages without having to save the contact first

#### whatsapp save for save bot compares 2 files
#### the first file is  your contact file which contains your contacts
#### the first file is  a vcf file

#### the second one is the comparison file
#### the file can be a vcf or a txt
#### if the file is a txt it should be list of numbers separated by a comma ( array )
#### these list can be obtained from whatsapp groups with the inspect function in the browser through whatsapp web
#### the comparison file is compare to your contacts and log file which contains a list of all send save for save
#### for contacts without country code they are logged and no message send

#### when the comparison between contacts and comparison file is done
#### the contacts that are not found in the both files are compare to log file
#### and if not found in both file, as save for save message will be send via whatsapp web
#### after sending the messsage the number will be saved in log file


### Installation

#### python3 -m venv vcf-env

#### source vcf-env/bin/activate

#### pip3 install pywhatkit pynput

### Usage

#### file.py <myContacts> <contacts_to_compare>


#### Before running the script ensure you edit the msg_data variable to fit the description of your profile,
#### the first msg_data variable is send to all contacts located in a vcf file

#### the second msg_data variable is for contacts from groups which is inform of an array and saved in a txt file or with another extension
#### the variable should thus be edited to describe the contact was retrieved from group for easier communication

## Kelvinification
### save for save
#### https://github.com/kevinification/save-for-save-bot.git