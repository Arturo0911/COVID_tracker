import React from 'react';
import { BrowserRouter as Router, Switch, Link, Route } from 'react-router-dom';



/**
 * Router Modules
 * 
 */

import {Chart} from '../router/chart';
import {Map} from '../router/map';

/**
 * Import images
 */

import chart from './img/chart.png'





export const Navbar = () => {
    return (
        <div>
            <Router>
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <Link className="navbar-brand" to="/"><img src = {chart}/>   Navbar</Link>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav mr-auto">
                            <li className="nav-item active">
                                <Link to = "/home" className="nav-link">Home <span className="sr-only">(current)</span></Link>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    Dropdown</a>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <Link className="dropdown-item" to="/map">Maping</Link>
                                    <a className="dropdown-item" href="#">Another action</a>
                                    <div className="dropdown-divider"></div>
                                    <a className="dropdown-item" href="#">Something else here</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                </nav>
                <Switch>
                    <Route exact path= "/" >
                        <Chart/>
                    </Route>
                    <Route exact path = "/map">
                        <Map/>
                    </Route>
                </Switch>
            </Router>
        </div>
    )
};
