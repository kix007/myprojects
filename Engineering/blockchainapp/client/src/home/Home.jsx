import React from 'react';
import NavBar from '../nav/NavBar';
import logo from '../logo.png';


const Home = () => {
    return (
        <React.Fragment>
        <NavBar />
        <div align="center">
            <p>Written program in React framework to query a API endpoint and retrieve data.</p>
            <br />
            <br />
            <img src={logo} alt="logo" width={500} height={250} />
        </div>
        </React.Fragment>
    );
};

export default Home;