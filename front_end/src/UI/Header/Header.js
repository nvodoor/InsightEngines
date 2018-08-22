import React, { Component } from 'react'
import './Header.css'
import logo from './logo.png'

class Header extends Component {

    hamClick = () => {
        const navi = document.getElementsByClassName('navi')
        if (navi[0].style.display === "none") {
            navi[0].style.display = "flex"
        } else {
            navi[0].style.display = "none"
        }
        
    }

    render () {
        return (
            <div>
                <header className='header'>
                    <div id="hamburger" onClick={this.hamClick}>
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                    <span id="top"><img src={logo} width="100%" height="100%" alt="logo"></img></span>
                    <h1>Query Text</h1>
                </header>
            </div>
        )

    }
}

export default Header;