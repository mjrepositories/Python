import React, { useState, useEffect } from "react";

// we are creating a component by function where we declare props passed from previous parent components
const ReportElement = ({ report, setReportUpdated, reportingPeriods }) => {
  // creating a function for mapping values to keys
  // we pass there the whole object of retrieved dates and relevant value we want to look for
  const getKey = (object, value) => {
    // and then we ar returning this value by first getting array of keys of the object and using find function to get matching
    return Object.keys(object).find((key) => object[key] === value);
  };

  // we declare function for setting the report to be updated by passing it to state
  const reportForUpdated = () => {
    setReportUpdated(report);
    console.log(report);
  };

  // we return a component with relevant data for indicated report and we add functionality to a button
  return (
    <tr key={report.id}>
      <td>{report.report}</td>
      <td>{report.reporting_period}</td>
      <td>{report.executed}</td>
      <td key={report.executed_on}>
        {getKey(reportingPeriods, report.executed_on)}
      </td>
      <td>{report.on_time}</td>
      <td>{report.issues}</td>
      <td> {report.issues_description}</td>
      <td>
        <button className="update-status" onClick={reportForUpdated}>
          UPDATE STATUS
        </button>
      </td>
    </tr>
  );
};

export default ReportElement;
