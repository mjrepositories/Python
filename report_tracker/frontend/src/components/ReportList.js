import React, { useState, useEffect } from "react";
import ReportElement from "./ReportElement";
// creation of a component by function where as arguments we pass props we have from App.js. In this case we have reports and we are moving setReportUpdated functionality
const ReportList = ({ reports, setReportUpdated, reportingPeriods }) => {
  console.log("macius");
  useEffect(() => {
    document.title = `Status list | Report Tracker`;
  }, []);
  return (
    <table className="blueTable">
      <thead>
        <tr>
          <th>Report</th>
          <th>Reporting Period</th>
          <th>Executed</th>
          <th>Executed-On Date</th>
          <th>On Time</th>
          <th>Issues</th>
          <th>Issue Description</th>
          <th>UPDATE</th>
        </tr>
      </thead>
      <tbody>
        {/* we are looping over all reports we have and we generate ReportElement component and pass props to it */}
        {reports.map((report) => (
          <ReportElement
            key={report.id}
            report={report}
            reportingPeriods={reportingPeriods}
            setReportUpdated={setReportUpdated}
          />
        ))}
      </tbody>
    </table>

    // {reports.map((report) => (

    //   <h1 key={report.id}>
    //     {report.report} {report.reporting_period} {report.executed}{" "}
    //     {report.executed_on} {report.on_time} {report.issues}{" "}
    //     {report.issues_description}
    //   </h1>
    // ))}
  );
};

export default ReportList;
