import React, { Component } from 'react';
import './App.css';

class App extends Component {
    constructor (props){
        super(props)
        fetch(`http://127.0.0.1:8000/check/`,
            {
                mode: 'cors',
                method: 'POST',
                headers: {
                    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                },
                body: '&name=Deepraj',
            }
        )
        .then(res => res.json())
        .then(json => {
            console.log(json)
        });
    }
    render() {
        return (
            <div className="App">
              
            </div>
        );      
    }
  
}

export default App;
