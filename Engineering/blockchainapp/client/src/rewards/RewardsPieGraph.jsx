import React from 'react';
import { Chart as ChartJS, registerables } from 'chart.js';
import { Pie } from 'react-chartjs-2'
import './Rewards.css';

ChartJS.register(...registerables);

const RewardsGraphPieData = (data) => ({
  labels: data !== undefined ? data.data[0]?.data_labels : null,
  datasets: [
    {
      type: 'pie',
      label: 'Total',
      //data: ["Test"],
      data: data !== undefined ? data.data[1]?.chart_data.map((item) => item[2]) : null,
      fill: false,
      backgroundColor: 'rgba(61, 190, 255)',
      borderColor: 'rgba(33, 88, 217)',
      yAxisID: 'load_average"',
    },
    {
      type: 'pie',
      label: 'Average Amount',
      data: data !== undefined ? data.data[1]?.chart_data.map((item) => item[12]) : null,
      fill: false,
      backgroundColor: 'rgb(67, 11, 219)',
      borderColor: 'rgba(67, 11, 219)',
      yAxisID: 'load_average',
    },
    {
      type: 'pie',
      label: 'Average Amount',
      data: data !== undefined ? data.data[1]?.chart_data.map((item) => item[4]) : null,
      fill: false,
      backgroundColor: 'rgb(4, 8, 15)',
      borderColor: 'rgba(67, 11, 219)',
      yAxisID: 'load_average',
    },
  ],
});

const options = {
  responsive: false,
  maintainAspectRatio: false,
  scales: {
    yAxes: [
      {
        type: 'linear',
        display: true,
        position: 'left',
        id: "load_average",
        ticks: {
            beginAtZero: true,
        }
      },
    ],
  },
};

const RewardsPieGraph = (data) => (
  <>
    <div className='headerPie'>
      <h2 className='titlePie'>PieChart Stats</h2>
    </div>
    <div className='piechart'>
      <Pie data={RewardsGraphPieData(data !== undefined ? data : null )} options={options} height={500} width={500} />
    </div>
  </>
);

export default RewardsPieGraph;
