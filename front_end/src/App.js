import React from 'react';
import { Route, BrowserRouter, Switch, Redirect } from 'react-router-dom';
import './App.css';
import Header from './UI/Header/Header.js'
import Sidebar from './UI/Sidebar/Sidebar.js'
import CPU from './Component/CPU.js'
import Ind from './Component/Ind'
import Intrusion from './Component/Intrusion.js'
import Login from './Component/Login.js'
import Traffic from './Component/Traffic.js'

const App = () => {
      return (
        <BrowserRouter>
        <div className="container">
            <Header />
            <Sidebar />
            <div className="content-box">
                <Switch>
                    <Route path="/index" component={Ind} />
                    <Route path="/login" component={Login} />
                    <Route path="/cpu" component={CPU}/>
                    <Route path="/intrusion" component={Intrusion} />
                    <Route path="/traffic" component={Traffic} />
                </Switch>
                <Redirect from="*" to="/index" />
            </div> 
        </div>
        </BrowserRouter>
        );
  }


export default App;
