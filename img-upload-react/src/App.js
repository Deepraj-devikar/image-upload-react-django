import React, { Component } from 'react';
import './App.css';
import axios from 'axios'

class App extends Component {
    constructor (props){
        super(props)
        const user = {
                name: 'Deepraj',
            }
        axios.post(`http://127.0.0.1:8000/check/`, { user })
        .then(res => {
            console.log(res)
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
