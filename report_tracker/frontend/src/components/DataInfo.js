import React, { useEffect, useState } from "react";

// creating Component which is getting info prop
// We then pass info prop inside component and we are using map to return an array of elements which in this case is array of h1
const DataInfo = ({ info }) => {
  return (
    <div>
      {info.map((report) => (
        <h1 key={Math.random()}>{report}</h1>
      ))}
    </div>
  );
};

export default DataInfo;
