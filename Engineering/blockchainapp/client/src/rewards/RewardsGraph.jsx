import React from 'react';
import { Chart as ChartJS, registerables } from 'chart.js';
import { Bar } from 'react-chartjs-2'

ChartJS.register(...registerables);

const RewardsGraphData = (data) => ({
  labels: data !== undefined ? data.data[0]?.data_labels : null,
  datasets: [
    {
      type: 'bar',
      label: 'Total',
      data: data !== undefined ? data.data[1]?.chart_data.map((item) => item[2]) : null,
      fill: false,
      backgroundColor: 'rgba(61, 190, 255)',
      borderColor: 'rgba(33, 88, 217)',
      yAxisID: 'load_average"',
    },
    {
      type: 'bar',
      label: 'Average Amount',
      data: data !== undefined ? data.data[1]?.chart_data.map((item) => item[12]) : null,
      fill: false,
      backgroundColor: 'rgb(67, 11, 219)',
      borderColor: 'rgba(67, 11, 219)',
      yAxisID: 'y-axis-1',
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

const RewardsGraph = (data) => (
  <>
    <div className='header'>
      <h2 className='title'>Bar Stats</h2>
    </div>
    <Bar data={RewardsGraphData(data !== undefined ? data : null )} options={options} height={500} width={500} />
  </>
);

export default RewardsGraph;
