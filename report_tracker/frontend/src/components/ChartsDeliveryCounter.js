import React, { useEffect } from "react";
import { Doughnut } from "react-chartjs-2";

const ChartsDeliveryCounter = ({ results }) => {
  // destructuring prop
  const { executed, missing } = results;
  return (
    <div>
      <Doughnut
        data={{
          labels: ["Delivered", "Pending delivery"],
          datasets: [
            {
              label: "Percentage",
              data: [executed, missing],
              backgroundColor: ["green", "red"],
              hoverOffset: 7,
            },
          ],
        }}
        height={400}
        width={600}
        options={{
          responsive: false,
          maintainAspectRatio: false,
          // scales: {
          //   yAxes: [
          //     {
          //       ticks: {
          //         beginAtZero: true,
          //       },
          //     },
          //   ],
          // },
        }}
      />
    </div>
  );
};

export default ChartsDeliveryCounter;
