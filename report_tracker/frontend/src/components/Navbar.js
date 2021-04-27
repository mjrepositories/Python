import React, { useEffect, useState } from "react";

const Navbar = ({ gettingReports, creatingStatuses }) => {
  return (
    <div>
      <button onClick={gettingReports}>Fetching data</button>
      <button onClick={creatingStatuses}>Creating Statuses</button>
    </div>
  );
};

export default Navbar;
