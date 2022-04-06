import React, { useEffect, useState } from 'react';
import { fetchData, postData } from '../api';
import NavBar from '../nav/NavBar';
import RewardsGraphData from './RewardsGraph';
import RewardsPieGraph from './RewardsPieGraph';

const Rewards = () => {
    const [rewards, setRewards] = useState([]);
    const [rewardsChart, setRewardsChart] = useState([]);
    const ApiURL = process.env.REACT_APP_BASE_API_URL;
  
      useEffect(() => {
        
        if (rewards !== undefined) {
          postData(`${ApiURL}/insert_rewards`, setRewards);
        }
        if (rewardsChart !== undefined) {
          fetchData(`${ApiURL}/rewards`, setRewardsChart);
        }
      }, [])

    return (
        <React.Fragment>
        <NavBar />
        {rewardsChart ?
          <React.Fragment>
            <RewardsGraphData data={rewardsChart} />
            <RewardsPieGraph data={rewardsChart} />
          </React.Fragment>
        : null
        }
        </React.Fragment>
    );
};

export default Rewards;