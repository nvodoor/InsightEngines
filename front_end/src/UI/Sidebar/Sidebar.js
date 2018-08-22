import React, { Component } from 'react'
import './Sidebar.css'
import { NavLink } from 'react-router-dom';

class Sidebar extends Component {

    render () {
        return (
            <div>
                <nav className="navi">
                    <NavLink className="side-container" to="/traffic" style={{textDecoration: 'none'}}>Traffic</NavLink>
                    <NavLink className="side-container" to="/login" style={{ textDecoration: 'none' }}>Login</NavLink>
                    <NavLink className="side-container" to="/cpu" style={{ textDecoration: 'none' }}>CPU</NavLink>
                    <NavLink className="side-container" to="/intrusion" style={{ textDecoration: 'none' }}>Intrusion</NavLink>
                </nav>
            </div>
        )
    }
}

export default Sidebar