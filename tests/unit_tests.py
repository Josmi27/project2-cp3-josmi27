import chatchat
import unittest

   
class unit_test(unittest.TestCase):

    def test_chatbot_greetingMessage(self, usern="Joshua", message="!! greeting"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "Welcome to the chatroom of brotherhood.")
        

    def test_chatbot_helpMessage(self, usern="Joshua", message="!! help"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "The following commands are available to you: '!! greeting' | '!! help' | '!! say <something>' | '!! service date' | '!! party date' | '!! brotherhood quote'\
         | '!! who' | '!! why' | '!! what' | '!! when'")


    def test_chatbot_serviceMessage(self, usern="Joshua", message="!! service date"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result,  "At this current time, the next community service date will be held on April 23, following the regional convention.")
    
    def test_chatbot_partyMessage(self, usern="Joshua", message="!! party date"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result,  "You already know when the party is {}, stop playing with me brother!".format(usern)) 

    def test_chatbot_sayMessage(self, usern="Joshua", message="!! say happiness"): 
        self.usern = usern
        self.message = "{}".format(message[7:])
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "happiness") 

    def test_chatbot_whoMessage(self, usern="Joshua", message="!! who"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "My name is... I-Phi Bot!") 
    
    def test_chatbot_whatMessage(self, usern="Joshua", message="!! what"): 
        self.usern = usern
        self.message = "I am a chatbot. But not just any chatbot. I am the I-Phi Bot, created by Joshua Smith."
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "I am a chatbot. But not just any chatbot. I am the I-Phi Bot, created by Joshua Smith.") 
    
    def test_chatbot_whyMessage(self, usern="Joshua", message="!! say happiness"): 
        self.usern = usern
        self.message = "{}".format(message[7:])
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "happiness") 
        
    def test_chatbot_whenMessage(self, usern="Joshua", message="!! when"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "I was originally created on March 7, 2020. Fun fact: That's my birthday!") 
    
    def test_chatbot_noMessage(self, usern="Joshua", message="!! "): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "That is not a correct command. Please try again!") 
    
    
    
if __name__ == '__main__':
    unittest.main()
    # To run unit tests: cd current directory -> python -m tests.unit_tests 