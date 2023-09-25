#!/usr/bin/python3
import sys
import os
from pynput.keyboard import Key, Controller
import time
import pyautogui
import pywhatkit
import re

number_regex = "^[0-9+]+$"

def actual_Number(actualNo: int, whole_num: str, main_numbers: any, container_numbers: any, msg_data: any):
    if actualNo not in main_numbers:
        if actualNo not in container_numbers:
            try:
                toSendNo = whole_num
                if whole_num[0] == "0":
                    with open("nocode.log", 'a') as nocode_file:
                        nocode_file.write(str(whole_num)+"\n")
                    return

                pywhatkit.sendwhatmsg_instantly(phone_no=str(
                    toSendNo), message=msg_data, tab_close=False)
                time.sleep(15)
                pyautogui.click()
                time.sleep(5)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                with open("container.log", 'a') as final_file:
                    final_file.write(str(actualNo)+"\n")
                container_numbers.append(int(actualNo))
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(3)
            except Exception as e:
                print(str(e))


try:
    if len(sys.argv) != 3:
        print("[-] Usage: ")
        print("[-] file.py <myContacts> <contacts_to_compare>")
        exit()

    if not os.path.isfile(sys.argv[1]):
        print("[-] " + sys.argv[1] + " not found")
        exit()

    if not os.path.isfile(sys.argv[2]):
        print("[-] " + sys.argv[2] + " not found")
        exit()

    main_numbers = []
    container_numbers = []

    main_file = open(sys.argv[1], 'r')
    compare_file = open(sys.argv[2], 'r')
    keyboard = Controller()

    msg_data = ""

    if (os.path.isfile("container.log")):
        get_list = []
        container_file = open("container.log", "r")
        for cont_ainer in container_file:
            co_num = cont_ainer.replace("\n", "")
            get_list.append(int(co_num))

        container_numbers = [i for i in get_list if get_list.count(i) == 1]

    for line in main_file:
        if line.startswith('TEL;'):
            spitTel = line.strip().split(":")
            whole_number = str(spitTel[1]).replace(
                "-", "").replace(" ", "").replace("(", "").replace(")", "")
            crop_number = int(whole_number[-9:])
            main_numbers.append(crop_number)

    for con_tact in compare_file:

        spitNum = ""
        whole_num = ""
        actualNo = ""

        if con_tact.startswith('TEL;'):
            spitNum = con_tact.strip().split(":")
            whole_num = str(spitNum[1]).replace(
                "-", "").replace(" ", "").replace("(", "").replace(")", "")
            if not re.match(number_regex, whole_num) or len(whole_num) < 9:
                continue
            actualNo = int(whole_num[-9:])

            msg_data = """
Hello✋
Am *Kelvinification*
Kindly save my number for;
🪀 Status viewing
📌 Updates
s🫂 Friendship
😂 Sharing memes 
💰 Business & Opportunities
and more

If not intrested ignore 😊

save *Kelvinification*
and dm your name for save back 
♡ ㅤ   ❍ㅤ     ⎙      ⌲ 
ˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ   ˢᵃᵛᵉ   ˢʰᵃʳᵉ
        """
            actual_Number(actualNo, whole_num, main_numbers,
                          container_numbers, msg_data)

        elif not con_tact.startswith('BEGIN') and not con_tact.startswith('VERSION') and not con_tact.startswith('N') and not con_tact.startswith('FN') and not con_tact.startswith('TEL') and not con_tact.startswith('END') and not con_tact.startswith('ORG') and not con_tact.startswith('=') and not con_tact.startswith(''):
            spitNum = con_tact.strip().split(",")
            for onum in spitNum:
                whole_num = str(onum).replace(
                    "-", "").replace(" ", "").replace("(", "").replace(")", "")
                if not re.match(number_regex, whole_num) or len(whole_num) < 9:
                    continue

                actualNo = int(whole_num[-9:])

                msg_data = """
Hello✋
Am *Kelvinification*
Kindly save my number for;
🪀 Status viewing
📌 Updates
s🫂 Friendship
😂 Sharing memes 
💰 Business & Opportunities
and more

If not intrested ignore 😊

We share a common group.

save *Kelvinification*
and dm your name for save back 
♡ ㅤ   ❍ㅤ     ⎙      ⌲ 
ˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ   ˢᵃᵛᵉ   ˢʰᵃʳᵉ
        """
                actual_Number(actualNo, whole_num, main_numbers,
                              container_numbers, msg_data)

        else:
            continue

except KeyboardInterrupt:
    exit()
