import React, { Component } from 'react'
import './Component.css'

class Ind extends Component {
    render() {
        return (
            <div className="contain">
                <h1>Welcome to Query Text.</h1>
                <p>The purpose of this application is to 
                see if you are making a valid query for a search on the Insight Engines platform. Invalid queries will be highlighted in red. Valid queries highlighted in green.</p>
            </div>
        )
    }
}

export default Ind