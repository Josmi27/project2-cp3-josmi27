import chatchat
import unittest
import ap

class socketio_test(unittest.TestCase):
    
    def test_server_client_connects(self):
        client = ap.socketio.test_client(ap.app)
        self.assertTrue(client.is_connected())
    
    def test_server_client_disconnects(self):
        global disconnected
        disconnected = None
        client = ap.socketio.test_client(ap.app)
        client.disconnect()
        self.assertEqual(disconnected, None)
    
    def test_emit_namespace(self):
        client = ap.socketio.test_client(ap.app)
        receive = client.get_received()
        print(receive)

        client.emit('Entered data', {
            'username': "Joshua",
            'message': "My message"
        })

        received = client.get_received()
        self.assertEqual(received[0]['namespace'][0], '/')   
    
    def test_emit_server_response(self):
        client = ap.socketio.test_client(ap.app)
        receive = client.get_received()
        # print(receive)

        client.emit('Entered data', {
            'username': "Joshua",
            'message': "My message"
        })

        received = client.get_received()
        self.assertEqual(received[0]['name'], 'Info is now sending from server')
    
    
    
    def test_client_data_to_serverS(self):
        client = ap.socketio.test_client(ap.app)
        receive = client.get_received()

        client.emit('Entered data', {
            'username': "Joshua",
            'message': "My message"
        })

        received = client.get_received()
        self.assertEqual(received[0]['args'][0]['name'], 'Joshua')
        self.assertEqual(received[0]['args'][0]['post'], 'My message')
        

    
    #CHATCHAT TESTS
    
    def test_socketio_case_chatbot_aboutMessage(self, usern="Joshua", message="!! about"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "Welcome to the chatroom of brotherhood. I was created to uphold the unification of Iotas nationally. And always remember our 5 principles: Scholarship, Leadership, Citizenship, Fidelity, and Brotherhood!")
        

    def test_socketio_case_chatbot_helpMessage(self, usern="Joshua", message="!! help"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result, "The following commands are available to you: '!! about' | '!! help' | '!! say <something>' | '!! service date' | '!! party date' | '!! brotherhood quote'")


    def test_socketio_case_chatbot_serviceMessage(self, usern="Joshua", message="!! service date"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result,  "At this current time, the next community service date will be held on April 23, following the regional convention.")
    
    def test_socketio_case_chatbot_partyMessage(self, usern="Joshua", message="!! party date"): 
        self.usern = usern
        self.message = message
        result = chatchat.ChatBot(usern, message)[1]
        self.assertEqual(result,  "You already know when the party is {}, stop playing with me brother!".format(usern)) 



if __name__ == '__main__':
    unittest.main()
    # To run: python -m tests.socketio_tests in parent folder