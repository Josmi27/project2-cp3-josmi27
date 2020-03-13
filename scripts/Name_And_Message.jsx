import * as React from 'react';

import { Socket } from './Socket';

export class Name_And_Message extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: '', message: ''};

        this.handleUsernameAndMessageChange = this.handleUsernameAndMessageChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleUsernameAndMessageChange(event) {
        const target = event.target;
        const Entered_message = target.value;
        const Entered_username = target.name;
        
        this.setState({
            [Entered_username]: Entered_message
        });
    }
    


    handleSubmit(event) {
        // sends username and message to server
        Socket.emit('Entered data', {
            'username': this.state.value,
            'message': this.state.message
        })
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label> 
                    <font color="#DAA520">Username:</font>
                    <input name = "value" type="text" value={this.state.value} onChange={this.handleUsernameAndMessageChange} />
                </label>
                
                <h4><font color="#DAA520">Message: </font></h4>
                <textarea name = "message" value={this.state.message} onChange={this.handleUsernameAndMessageChange} rows="10" cols="30"></textarea>
              
            <br></br>    
            <input type="submit" value="Submit" />
            </form>
    );
  } 
}