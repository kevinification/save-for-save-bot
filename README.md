## Save for save

#### whatsapp save for save bot compares 2 files
#### the first file is  your contact file which contains your contacts
#### the first file is  a vcf file

#### the second one is the comparison file
#### the file can be a vcf or a txt
#### if the file is a txt it should be list of numbers separated by a comma
#### these list can be obtained from the inspect function in the browser through whatsapp web
#### the comparison file is compare to your contacts and log file which contains a list of all send save for save

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