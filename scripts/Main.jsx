import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Content } from './Content';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

ReactDOM.render(<Content />, document.getElementById('content'));

const responseGoogle = (response) => {
    console.log(response);
};


ReactDOM.render(
  <GoogleLogin
    clientId="911020125730-enhlgbo9dvbhjjbsn1qh73p51vqtkm3u.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={responseGoogle}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />,
  document.getElementById('googleButton')
);

Socket.on('connect', function() {
    console.log('connecting to the server!');
});