import chatchat
import unittest
import ap

# These should test Socket.io codepaths ([responses for client requests], so when
# the client sends a request, assertEqual the server response) within 
# your app and be unique to each other

# NEED 5

class socketio_test(unittest.TestCase):
    
    def test_server_sends_hello(self):
        client = ap.socketio.test_client(ap.app)
        response = client.get_received()
        self.assertEquals(len(response), 1)
        
        from_server = response[0]
        self.assertEqual(from_server['name'], "hello to client")
        
        data = from_server['args'][0]
        self.assertEqual(data['message'], "Hey there!")
        
        
        
        
    def test_server_relays_message(self):
        client = ap.socketio.test_client(ap.app)
        client.emit('new message', {'my message': 'Purple is beautiful!'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        # print("I am from_Server variable: ", from_server)
        self.assertEqual(from_server['name'], 'got your message')
        
        data = from_server['args'][0]
        self.assertEqual(data['your message'], u'Purple is beautiful!')
        print(response[1])







if __name__ == '__main__':
    unittest.main()
    # To run: python -m tests.socketio_tests in parent folder
    