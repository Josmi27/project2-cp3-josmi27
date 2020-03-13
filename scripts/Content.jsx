import * as React from 'react';

import { Socket } from './Socket';
import { Name_And_Message } from './Name_And_Message';
import { Chat_Log } from './Chat_Log';
import { GoogleLogin } from 'react-google-login';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'names_and_posts': [] 
        };
    }
    
    componentDidMount() {
        Socket.on('Info is now sending from server', (data) => {
            this.setState({
                'name_received': data['name'],
                'post_received': data['post']
            });
        })
    }

    render() {
        let username = this.state.name_received
        let message = this.state.post_received

        return (
            <div>
                <GoogleLogin />
                <h1><font color="#DAA520">The Official I-Phi Chat App!</font></h1>
                <Name_And_Message />
                <Chat_Log />
                <ul><font color="#DAA520">{username}: {message}</font></ul>
                
            </div>
        );
    }
}