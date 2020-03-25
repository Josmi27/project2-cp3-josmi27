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
        




if __name__ == '__main__':
    unittest.main()
    # To run: python -m tests.socketio_tests in parent folder