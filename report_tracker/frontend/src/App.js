import "./App.css";
import React, { useState, useEffect } from "react";

// importing relevant components for my app
import Navbar from "./components/Navbar";
import ReportList from "./components/ReportList";
import DateInfo from "./components/DataInfo";
import UpdateBar from "./components/UpdateBar";
import Navigation from "./components/Navigation";
import Charts from "./components/Charts";
import Instruction from "./components/Instruction";
import History from "./components/ChartsHistory";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import ChartsHistory from "./components/ChartsHistory";

// function for rendering App - it is used to put the whole App in a web browser
function App() {
  // function for getting reporting Periods. Async function as we are calling API to get data there
  const getPeriods = async () => {
    // getting the response by using fetch and declaring end point responsible for generating the list of periods
    const response = await fetch(
      "http://localhost:8000/api/report_tracker/get-periods"
    );
    // putting response to JSON
    const periodsList = await response.json();
    // setting the state to generated JSON
    setReportingPeriods(periodsList);
    console.log(periodsList);
  };

  // function for getting Reports with statuses. Async function as we are calling API to get data there
  const getReports = async () => {
    // getting the response by using fetch and declaring end point responsible for generating the list of all relevant statuses
    const response = await fetch(
      "http://localhost:8000/api/report_tracker/all-statuses"
    );
    // putting response to JSON
    const reporting = await response.json();
    console.log(reporting);
    // setting the state to generated JSON
    setReports(reporting);
  };

  // function for pulling results
  const getResults = async () => {
    // getting the response from the endpoint
    const response = await fetch(
      "http://localhost:8000/api/report_tracker/graphs"
    );
    // converting to JavaSrcript Object (switching from JSON)
    const resulting = await response.json();
    setResults(resulting);
  };

  // function for creating new Statuses for current month. Async function as we are calling API to get data there
  const creatingStatuses = async () => {
    // getting the response by using fetch and declaring end point responsible for generating new statuses
    const response = await fetch(
      "http://localhost:8000/api/report_tracker/status-check"
    );
    // putting response to JSON
    const res = await response.json();
    // setting the state by pulling only values (keys are left)
    setInfo(Object.values(res));
  };

  // Declaring relevant states
  const [reports, setReports] = useState([]);

  const [info, setInfo] = useState([]);

  const [reportUpdated, setReportUpdated] = useState([]);

  const [reportingPeriods, setReportingPeriods] = useState([]);

  const [results, setResults] = useState({});

  // Declaring use effect for getting Periods from API only when App is loaded at the beginning
  // First element is a function we want to envoke, second is the parameter which is trigerring it
  // Having empty array there means that it is only executed once
  useEffect(getPeriods, []);

  useEffect(getResults, []);
  // Returning everything that we want in our App
  // We declare all components we want to render in our App by putting them in <componentName/>
  // Inside we can pass props which is data we want to pass to them and create some functionalities (like updating the data, rendering content)
  return (
    <div className="App">
      <h1 className="my-header">Report Tracker by MJ</h1>

      {/* Everything that we pass between Router will be able to use routing for rendering content on different urls */}
      <Router>
        <Navigation />
        {/* putting everyting inside Switch is making the program to stop looking for next routing with similar address
        More acceptable explanation - it checks the address first and when we have / encountered - it is not going forward
        But it is stoppping at the first occurence of the address matching and is rendering this specific component */}
        <Switch>
          {/* We declare Route and put inside all components we want to render. As path we specify what address is needed to render them */}
          <Route exact path="/">
            <div className="main-table">
              <h2>Report table and Update</h2>
              <UpdateBar
                reportingPeriods={reportingPeriods}
                reportUpdated={reportUpdated}
                setReportUpdated={setReportUpdated}
                setReports={setReports}
                reports={reports}
              />
              <Navbar
                gettingReports={getReports}
                creatingStatuses={creatingStatuses}
              />
              <ReportList
                reports={reports}
                setReportUpdated={setReportUpdated}
                reportingPeriods={reportingPeriods}
              />
              <DateInfo info={info} />
            </div>
          </Route>
          <Route path="/scoring">
            <h2 className="additional-header">Graphs with results</h2>
            <h2 className="additional-header">{`${results.month} ${results.year}`}</h2>
            <Charts results={results} />
          </Route>
          <Route path="/past">
            <h2 className="additional-header">
              History performance of reporting deliveries
            </h2>
            <ChartsHistory results={results} />
          </Route>
          <Route path="/instruction">
            <h2 className="additional-header">How app works</h2>
            <Instruction />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
