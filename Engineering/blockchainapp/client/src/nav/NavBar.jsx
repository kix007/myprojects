import React from 'react';
import './NavBar.css';

const NavBar = () => {
    return (
        <div className="container">
        <h1 className="heading">Helium BlockChain API - Example</h1>
        <strong><nav>
        <ul className="menu">
          <li><a href="/">Home</a></li>
          <li><a href="/accounts">Accounts</a></li>
          <li><a href="/rewards">Rewards Charts</a></li>
        </ul>
      </nav></strong>
    </div>
    )
};


export default NavBar;