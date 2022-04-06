import React, { useEffect, useState } from 'react';
import { fetchData, postData } from '../api';
import NavBar from '../nav/NavBar';
import './Accounts.css';


const Accounts = () => {
    const [accounts, setAccounts] = useState([]);
    const [accountsList, setAccountsList] = useState([]);
    const ApiURL = process.env.REACT_APP_BASE_API_URL;
    
      useEffect(() => {
        postData(`${ApiURL}/accounts`, setAccounts);
        fetchData(`${ApiURL}/accounts_list`, setAccountsList);
      }, [])
    
    return (
        <React.Fragment>
        <NavBar />
        <h2>List of Accounts</h2>
       
        <table id="tblAccounts">
            <thead>
                <tr>
                    <th>Address</th>
                    <th>Balance</th>
                    <th>Block</th>
                    <th>DC Balance</th>
                    <th>DC Nonce</th>
                    <th>Staked Balance</th>
                </tr>
            </thead>
            {accountsList.map((item, index) => (
            <tbody key={item.address}>
                <>
                <tr>
                  <td>{item.address}</td>
                  <td>{item.balance}</td>
                  <td>{item.block}</td>
                  <td>{item.dc_balance}</td>
                  <td>{item.dc_nonce}</td>
                  <td>{item.staked_balance}</td>
                </tr>
                </>
            </tbody>
            ))}
        </table>
        </React.Fragment>
    );
};

export default Accounts;