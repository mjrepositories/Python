import React, { useEffect } from "react";
import { Bar } from "react-chartjs-2";
import "chartjs-plugin-annotation";
import { Chart } from "chart.js";
import annotationPlugin from "chartjs-plugin-annotation";
Chart.register(annotationPlugin);

const ChartsHistory = ({ results }) => {
  const { target, year_results } = results;
  console.log(target);
  console.log(year_results);
  const y_results = Object.keys(year_results || []);
  const y_values = Object.values(year_results || []);
  return (
    <div className="ChartsFlex">
      <Bar
        data={{
          labels: y_results,
          datasets: [
            {
              label: "Delivery rate",
              barPercentage: 0.2,
              data: y_values,
              backgroundColor: y_values.map((result) =>
                result >= target ? "green" : "red"
              ),
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

export default ChartsHistory;
