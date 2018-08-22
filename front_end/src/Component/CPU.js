import React, { Component } from 'react'
import './Component.css'
import axios from 'axios'
import Errors from '../Response/Errors'
import Success from '../Response/Success'

class CPU extends Component {

    state = {
        datamodel: 'Enter Data Model',
        date_filter: 'Enter Date',
        invalid: 'None',
        errors: [],
        success: [],
        field_error: 'None'
    }

    handleUpdate = (e) => {
        if (e.target.name === 'datamodel') {
            this.setState ({
                datamodel: e.target.value
            })
        }

        if (e.target.name === 'date_filter') {
            this.setState ({
                date_filter: e.target.value
            })
        }
    }

    fetchData = () => {
        let form = ""
        if (this.state.datamodel === "" || this.state.datamodel === 'Enter Data Model') {
            form += "Please fill out data model. \n"
        }
        if (this.state.date_filter === "" || this.state.date_filter === "Enter Date") {
            form += "Please fill out date filter."
        }
        if (form !== "") {
            alert(form)
        }
        axios.get('http://0.0.0.0:3134/cpu', {
            params: {
                data_models: this.state.datamodel,
                date_filters: this.state.date_filter
            }
        })
        .then(res => {
            console.log(res.data)
            if (res.data.errors) {
                let data = []
                for (var key in res.data.errors) {
                    data.push({[key]: res.data.errors[key]})
                }
                this.setState({
                    errors: data,
                    success: []
                })
            }
            if (res.data.valid === true) {
                let data = []
                for (var ky in res.data) {
                    if (ky !== 'valid') {
                        if (ky === 'field_error') {
                            continue;
                        } else if (res.data.field_error === res.data[ky]) {
                            data.push({ [ky]: res.data[ky], 'field_error': res.data.field_error })
                        } else {
                            data.push({ [ky]: res.data[ky] })
                        }
                    }
                }
                console.log(data)
                this.setState({
                    success: data,
                    errors: []
                })
            }
        }
        )
        .catch(err => console.log(err))
    }

    render() {
        let lists = <p>Enter query above to see if it is valid.</p>
        if (this.state.errors.length > 0) {
            lists = this.state.errors.map(error =>
                <Errors key={Math.random() * 1000} err={error} />)
        }
        if (this.state.success.length > 0) {
            lists = this.state.success.map(item =>
                <Success key={Math.random()*1000} value={item} />
            )
        }
        return (
            <div className="contain">
                <h1>CPU Search</h1>
                <p>Data Models should be entered as alphabetical characters only. <br/>
                For the date filter you should enter dates in the following format: MM/DD/YYYY:HH:MM:SS.</p>
                <div className="input-box">
                <input type="text" value={this.state.datamodel} onChange={this.handleUpdate} name='datamodel' />
                <input type="text" value={this.state.date_filter} onChange={this.handleUpdate} name='date_filter'/>
                <button type="button" onClick={this.fetchData}>Retrieve Spec</button>
                </div>
                {lists}
            </div>
        )
    }
}

export default CPU