import React, { Component } from 'react';
import './App.css';
import axios from 'axios'

class App extends Component {
    constructor (props){
        super(props)
        this.state = {
            selected_file: ""
        }
        this.fileSelectHandler = this.fileSelectHandler.bind(this)
        this.fileUploadHandler = this.fileUploadHandler.bind(this)
        axios.get(`http://127.0.0.1:8000/img/`)
        .then(res => {
            console.log(res)
        });
    }

    fileSelectHandler(event){
        this.setState({
            selected_file: event.target.files[0]
        })
    }

    fileUploadHandler(){
        const formData = new FormData()
        formData.append('image', this.state.selected_file)
        axios.post(`http://127.0.0.1:8000/imgup/`, formData)
        .then(res => {
            console.log(res)
        });
    }

    render() {
        return (
            <div className="App">
                <input type="file" onChange={this.fileSelectHandler} />
                <button onClick={this.fileUploadHandler}>Upload</button>
            </div>
        );      
    }
  
}

export default App;
