import React, { useEffect } from "react";
import { Doughnut } from "react-chartjs-2";
import ChartsDays from "../components/ChartsDays";
import ChartsDeliveryCounter from "../components/ChartsDeliveryCounter";
import ChartsDeliveryRate from "../components/ChartsDeliveryRate";
import ChartsIssues from "../components/ChartsIssues";

const Charts = ({ results }) => {
  useEffect(() => {
    document.title = `Results | Report Tracker`;
  }, []);
  console.log(results);
  return (
    <div className="ChartsGrid">
      <ChartsDeliveryRate key={1} results={results} />
      <ChartsDeliveryCounter key={2} results={results} />
      <ChartsIssues key={3} results={results} />
      <ChartsDays key={4} results={results} />
    </div>
  );
};

export default Charts;
