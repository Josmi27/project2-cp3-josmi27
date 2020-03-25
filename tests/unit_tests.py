import chatchat
import unittest

   
class unit_test(unittest.TestCase):
    
    # These should not start up a local Flask server nor test Socket.io functionality
    # These should test code paths in your app and be unique to each other
    
    # Tests are meant to verify that things do work, actually work, and things that don’t work, actually don’t. 
    # Use them as a way of communicating your expectations for what the code should (or should not!) do.
    
    # Rewrite your code in a way so that it’s easier to write tests on it,
    
    
    
    ####  Confirm the colors of every little thing. The reason why is to stress the importance
    # of matching the Iota theme
    
    
    def test_chatbot_aboutMessage(self, usern="Joshua", message="!! about"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "Welcome to the chatroom of brotherhood. I was created to uphold the unification of Iotas nationally. And always remember our 5 principles: Scholarship, Leadership, Citizenship, Fidelity, and Brotherhood!")
        

    def test_chatbot_helpMessage(self, usern="Joshua", message="!! help"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "The following commands are available to you: '!! about' | '!! help' | '!! say <something>' | '!! service date' | '!! party date' | '!! brotherhood quote'")


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

    
    
if __name__ == '__main__':
    unittest.main()
    # To run unit tests: cd current directory -> python unit_tests.py 
    