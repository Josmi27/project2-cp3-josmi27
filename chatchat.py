import requests

url = "https://150000-quotes.p.rapidapi.com/keyword/Brotherhood"

headers = {
    'x-rapidapi-host': "150000-quotes.p.rapidapi.com",
    'x-rapidapi-key': "2bc8488dedmsh09812c800fb6b89p19fb19jsn6987dc57cdda"
    }

response = requests.request("GET", url, headers=headers)
json_body = response.json()


def ChatBot(username, message):
    
    if message == "!! who":
            response = "My name is... I-Phi Bot!"
        
    elif message == "!! greeting":
            response = "Welcome to the chatroom of brotherhood."
            
    elif message == "!! help":
            response = "The following commands are available to you: '!! greeting' | '!! help' | '!! say <something>' | '!! service date' | '!! party date' | '!! brotherhood quote'\
         | '!! who' | '!! why' | '!! what' | '!! when'"
        
    elif message == '!! say {}'.format(message[7:]):
            response = "{}".format(message[7:])
            
    elif message == "!! service date":
        response = "At this current time, the next community service date will be held on April 23, following the regional convention."
    
    elif message == "!! party date":
        response = "You already know when the party is {}, stop playing with me brother!".format(username) 
        
    elif message == "!! brotherhood quote":
        response = "Here is your quote of brotherhood!: {}".format(json_body["message"])
            
    elif message == "!! why":
        response = "I was created to uphold the unification of Iotas nationally. And always remember our 5 principles: Scholarship, Leadership, Citizenship, Fidelity, and Brotherhood!"
    
    elif message == "!! what":
        response = "I am a chatbot. But not just any chatbot. I am the I-Phi Bot, created by Joshua Smith."
    
    elif message == "!! when":
        response = "I was originally created on March 7, 2020. Fun fact: That's my birthday!"
        
    else:
        response = "That is not a correct command. Please try again!"
        
    return username, response