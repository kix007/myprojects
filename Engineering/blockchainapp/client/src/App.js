import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Accounts from './accounts/Accounts';
import Rewards from './rewards/Rewards';
import Home from './home/Home';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route exact path="/accounts" element={<Accounts />} />
        <Route exact path="/rewards" element={<Rewards />} />
      </Routes>
    </BrowserRouter>
  );
};