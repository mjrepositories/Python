import React, { useState, useEffect } from "react";
// creating a component by declaring a function and passing inside all relevant props for updating the statuses
const Update = ({
  reportUpdated,
  setReportUpdated,
  setReports,
  reports,
  reportingPeriods,
}) => {
  // creating a selection array so that dropdown can be used
  const selection = ["", "YES", "NO"];

  // function for updating indicated post. We pass there ID to know which report has to be updated
  const updateDatabase = async (id) => {
    // testing a change in reportUpdated
    // setReportUpdated((previousState) => ({ ...previousState, executed_on: 4 }));
    console.log(reportUpdated);
    // function is async as we call API so we await fetching the data from the declared endpoint
    const res = await fetch(
      `http://localhost:8000/api/report_tracker/status-update/${id}`,
      // we put all relevant information to our request like POST method, content-type
      // we pass which is json and body of the request which is data we want to POST
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(reportUpdated),
      }
    );
    // Once we have the report updated - we updated all reports we have in report overview by keeping all
    // non-adjusted reports as they were and we pass the status we corrected with relevant changes
    setReports(
      reports.map((report) =>
        report.id === id
          ? {
              ...reportUpdated,
              executed_on: parseInt(reportUpdated.executed_on),
            }
          : report
      )
    );
    // we set currently updated status to nothing
    setReportUpdated([]);
  };

  // function for handling changes when values are updated
  const handleDating = (e) => {
    // indicating the name of field
    const naming = "executed_on";
    // indicating the value of a field
    const value = e.target.value;
    // setting up the value for updated report which are present in state
    setReportUpdated({
      ...reportUpdated,
      [naming]: value === "" ? null : value,
    });
  };

  // function for handling changes when values are updated
  const handleInput = (e) => {
    // indicating the name of field
    const naming = "issues_description";
    // indicating the value of a field
    const value = e.target.value;
    // setting up the value for updated report which are present in state
    setReportUpdated({
      ...reportUpdated,
      [naming]: value === "" ? null : value,
    });
  };

  // function for handling changes when values are updated
  const handleExecuted = (e) => {
    // indicating the name of field
    const naming = "executed";
    // indicating the value of a field
    const value = e.target.value;
    // setting up the value for updated report which are present in state
    setReportUpdated({
      ...reportUpdated,
      [naming]: value === "" ? null : value,
    });
  };

  // function for handling changes when values are updated
  const handleOnTime = (e) => {
    // indicating the name of field
    const naming = "on_time";
    // indicating the value of a field
    const value = e.target.value;
    // setting up the value for updated report which are present in state
    setReportUpdated({
      ...reportUpdated,
      [naming]: value === "" ? null : value,
    });
  };

  // function for handling changes when values are updated
  const handleIssues = (e) => {
    // indicating the name of field
    const naming = "issues";
    // indicating the value of a field
    const value = e.target.value;
    // setting up the value for updated report which are present in state
    setReportUpdated({
      ...reportUpdated,
      [naming]: value === "" ? null : value,
    });
  };

  // for (const [key, value] of Object.entries(reportingPeriods)) {
  //   return (
  //     <option key={key} value={value}>
  //       {key}
  //     </option>
  //   );
  // }
  // returning the component
  return (
    <div>
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
            <th>SAVE</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            {/* passing read-only data to table cell */}
            <td>{reportUpdated.report}</td>
            <td>{reportUpdated.reporting_period}</td>
            {/* create a selection which has onChange handler function and values for dropdown are from declared array */}
            {/* It is also being updated by the values that status already has */}
            <td>
              <select
                onChange={handleExecuted}
                name="executed"
                id="executed"
                value={
                  reportUpdated.executed == null ? "" : reportUpdated.executed
                }
              >
                {selection.map((sel) => {
                  return (
                    <option key={sel} value={sel}>
                      {sel}
                    </option>
                  );
                })}
              </select>
            </td>
            <td>
              {/* create a selection which has onChange handler function and values for dropdown are from declared array */}
              {/* It is also being updated by the values that status already has */}
              <select
                name="onTime"
                id="onTime"
                onChange={handleDating}
                value={
                  reportUpdated.executed_on == null
                    ? ""
                    : reportUpdated.executed_on
                }
              >
                {Object.entries(reportingPeriods).map(([key, value], i) => (
                  <option key={key} value={value}>
                    {key}
                  </option>
                ))}
                {/* {reportingPeriods.keys.map((sel) => {
                  return (
                    <option key={sel} value={sel}>
                      {sel}
                    </option>
                  );
                })} */}
              </select>
            </td>
            <td>
              {/* create a selection which has onChange handler function and values for dropdown are from declared array */}
              {/* It is also being updated by the values that status already has */}
              <select
                name="onTime"
                id="onTime"
                onChange={handleOnTime}
                value={
                  reportUpdated.on_time == null ? "" : reportUpdated.on_time
                }
              >
                {selection.map((sel) => {
                  return (
                    <option key={sel} value={sel}>
                      {sel}
                    </option>
                  );
                })}
              </select>
            </td>
            <td>
              {/* create a selection which has onChange handler function and values for dropdown are from declared array */}
              {/* It is also being updated by the values that status already has */}
              <select
                name="issues"
                id="issues"
                onChange={handleIssues}
                value={reportUpdated.issues == null ? "" : reportUpdated.issues}
              >
                {selection.map((sel) => {
                  return (
                    <option key={sel} value={sel}>
                      {sel}
                    </option>
                  );
                })}
              </select>
            </td>
            <td>
              {/* create an input field which has handler function for adding text */}
              {/* It is also being updated by the value that status already has */}
              <input
                type="text"
                onChange={handleInput}
                value={
                  reportUpdated.issues_description == null
                    ? ""
                    : reportUpdated.issues_description
                }
              />
            </td>
            <td>
              <button
                className="update-status"
                onClick={() => updateDatabase(reportUpdated.id)}
              >
                CONFIRM
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Update;
