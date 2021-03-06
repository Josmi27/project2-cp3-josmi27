## Why did you choose to test the code that you did?
The following explains my decisions around placements of at least 5 different test cases:
<ul>
  <li><em>Test Case "test_emit_namespace"</em> - I chose to test the namespace of this application because I feel as though it is important to verify where the client connects to, and where the server is listening. </li>
  <li><em>Test Case "test_client_data_to_serverS"</em> - I chose to test the sending of data from the client to the server because this is part 1 of the base functionality of the application. It is imperative that the server received the client's input, before more progress could be made. </li>
  <li><em>Test Case "test_emit_server_response"</em> - The purpose of this test was to verify that the server successfully returned data from the client request. This was important because it is a key component of the application for data to be returned to the webpage correctly.</li>
  <li><em>Test Case "test_chatbot_greetingMessage"</em> - I chose to test this chatbot message because it was one of the simplest chatbot commands/responses. I knew that if this test passed, then most of my other chatbot tests should pass. </li>
  <li><em>Test Case "test_chatbot_sayMessage"</em> - I chose to test this chatbot message because it was one of the most complicated chatbot commands/responses to test. Therefore, I decided to make certain that I included this particular chatbot test into my unit tests.</li>
</ul>

## Is there anything else you would like to test if you had the time (or was asked to do so?)
If I had the time, I would like to add more functionality and tests for CircleCI, because it is very useful in many ways for web applications, like this project! 

<br>
<em> Link To Production: </em> http://gentle-castle-06902.herokuapp.com/
