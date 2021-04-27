import React, { useEffect } from "react";

const Instruction = () => {
  useEffect(() => {
    document.title = `Instruction | Report Tracker`;
  }, []);
  return (
    <div className="instruction-container">
      <div className="explanation">
        <h3>
          To fetch data on reports for current month - press "Fetching data"
          button so that request to database will be triggered.
        </h3>
        <h3>
          "Creating Statuses" button can be used every month to generate
          statuses for current month
        </h3>
      </div>
      <div className="image-instruction">
        <img src="/fetching.jpg" alt="" />
      </div>
      <div className="explanation">
        <h3>
          Once data is received from the database - it will be presented in the
          table
        </h3>
        <h3>
          If you decide to update the report with data - press "Update Status"
          which will enable editing in Update Bar
        </h3>
      </div>
      <div className="image-instruction">
        <img src="/fetched_data.jpg" alt="" />
      </div>
      <div className="explanation">
        <h3>
          Data is now available for editing. You can select relevant fields with
          selection or edit text
        </h3>
        <h3>
          Once your data is as you wanted to have - press "Confirm" so that
          input will be saved in the database and table will be updated with you
          entries
        </h3>
      </div>
      <div className="image-instruction">
        <img src="/saving.jpg" alt="" />
      </div>
    </div>
  );
};

export default Instruction;
