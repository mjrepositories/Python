import React, { useEffect } from "react";
import { Doughnut } from "react-chartjs-2";

const ChartsIssues = ({ results }) => {
  // destructuring prop
  const { issues, no_issues } = results;
  console.log(issues);
  console.log(no_issues);

  return (
    <div>
      <Doughnut
        data={{
          labels:
            issues === 0
              ? ["Reports without issues"]
              : ["Reports without issues", "Reports with issues"],
          datasets: [
            {
              label: "Number",
              data: issues === 0 ? [no_issues] : [no_issues, issues],
              backgroundColor: issues === 0 ? ["green"] : ["green", "red"],
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

export default ChartsIssues;
