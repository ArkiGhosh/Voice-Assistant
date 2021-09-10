import pywhatkit as kit
import speech_recog as sp
import csv
import pyautogui as pg
import time


class Whatsapp():

    def __init__(self):
        #input name from the user
        sp.assistant_response('Who do you want to send a message to?')
        self.contact_name = sp.input_command()

    def send_message(self):

        #accessing the list of contacts
        with open('contacts.csv', 'r') as file:
            reader = csv.DictReader(file)
            target = None
            for i in reader:
                if i['Name'] == self.contact_name:
                    target = i['Number']
                    

        if target == None:
            response = "You need to add this number in your contact list or check the name again"
            sp.assistant_response(response)
            return 0

        else:
            #get message the user wants to send
            sp.assistant_response("What would you like to write to them?")
            answer_first_query = sp.input_command()
            print(answer_first_query)

            #get scheduled time
            sp.assistant_response("At what hour do you want to send the message?")
            hour = sp.input_command()
            sp.assistant_response("At what minute do you want to send the message?")
            minute = int(sp.input_command())
            sp.assistant_response("a.m. or p.m.?")
            meridian = sp.input_command()
            if meridian == 'pm':
                hour = int(hour) + 12    #to make target time according to 24 hour clock
            print(hour, minute, meridian)
            #sending the message
            sp.assistant_response('Ok, scheduled to send message at ' + str(hour) + str(minute) + meridian)
            kit.sendwhatmsg(target, answer_first_query, int(hour), int(minute), tab_close = True, close_time = 10)
            pg.press("enter")
            return 1

    def contact_not_present(self):

        #asking for the contact
        sp.assistant_response('Please add the number for' + self.contact_name + 'with the country code')
        new_contact = input()

        #adding the contact
        with open('contacts.csv', 'a', newline = "") as file:
            write = csv.writer(file)
            write.writerow([self.contact_name, new_contact])


    def Instant_Message(self):
        
        #accessing the list of contacts
        with open('contacts.csv', 'r') as file:
            reader = csv.DictReader(file)
            target = None
            for i in reader:
                if i['Name'] == self.contact_name:
                    target = i['Number']
                    

        if target == None:
            response = "You need to add this number in your contact list or check the name again"
            sp.assistant_response(response)
            return 0

        else:
            #get message the user wants to send
            sp.assistant_response("What would you like to write to them?")
            answer_first_query = sp.input_command()
            print(answer_first_query)
            sp.assistant_response('Ok, sending the message')
            kit.sendwhatmsg_instantly(target, answer_first_query, wait_time = 40, tab_close = True, close_time = 10)
            time.sleep(6)
            width, height = pg.size()
            pg.click(width / 2, height / 2)
            time.sleep(10)
            pg.press("enter")
            time.sleep(10)
            return 1

#test
#a = Whatsapp()
#a.send_message()