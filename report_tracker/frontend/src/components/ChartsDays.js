import React, { useEffect } from "react";
import { Bar } from "react-chartjs-2";

const ChartsDays = ({ results }) => {
  const { days_overview } = results;
  console.log(days_overview);
  const days = Object.keys(days_overview || []);
  const report_number = Object.values(days_overview || []);
  //   console.log(days);
  //   console.log(report_number);
  return (
    <div>
      <Bar
        data={{
          labels: days,
          datasets: [
            {
              label: "Number of reports",
              data: report_number,
              backgroundColor: "#add8e6",
            },
          ],
        }}
        height={400}
        width={600}
        options={{
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            y: {
              suggestedMin: 0,
              suggestedMax: 10,
              stepSize: 1,
              ticks: {
                beginAtZero: true,
              },
            },
          },
        }}
      />
    </div>
  );
};

export default ChartsDays;
