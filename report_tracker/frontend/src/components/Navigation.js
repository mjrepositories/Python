import React, { useEffect } from "react";
import { Link } from "react-router-dom";

const Navigation = () => {
  return (
    <div>
      <nav>
        <ul className="nav-links">
          <Link className="format-link" to="/">
            <li>Status Table</li>
          </Link>
          <Link className="format-link" to="/scoring">
            <li>Graphs</li>
          </Link>
          <Link className="format-link" to="/past">
            <li>Past Performance</li>
          </Link>
          <Link className="format-link" to="/instruction">
            <li>Instruction</li>
          </Link>
        </ul>
      </nav>
    </div>
  );
};

export default Navigation;
