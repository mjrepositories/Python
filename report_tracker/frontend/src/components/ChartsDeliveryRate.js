import React, { useEffect } from "react";
import { Bar } from "react-chartjs-2";
import "chartjs-plugin-annotation";
import { Chart } from "chart.js";
import annotationPlugin from "chartjs-plugin-annotation";
Chart.register(annotationPlugin);

const ChartsDeliveryRate = ({ results }) => {
  const { delivery_rate, target } = results;

  return (
    <div>
      <Bar
        data={{
          labels: ["Delivery Rate"],
          datasets: [
            // {
            //   label: "Target for delivery rate",
            //   data: [target],
            //   type: "line",
            //   // this dataset is drawn on top
            //   order: 2,
            //   borderColor: "#327da8",
            //   borderWidth: 4,
            // },
            {
              label: "Delivery rate",
              barPercentage: 0.2,
              data: [delivery_rate],
              backgroundColor: target <= delivery_rate ? ["green"] : ["red"],
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
              ticks: {
                beginAtZero: true,
                // callback allows to change to percentage on y-axis
                // callback: function (value) {
                //   return ((value / this.max) * 100).toFixed(0) + "%";
                // },
              },
            },
          },
          plugins: {
            autocolors: false,
            annotation: {
              annotations: {
                line1: {
                  type: "line",
                  yMin: 0.95,
                  yMax: 0.95,
                  borderColor: "blue",
                  borderWidth: 2,
                },
              },
            },
          },
        }}
      />
    </div>
  );
};

export default ChartsDeliveryRate;
