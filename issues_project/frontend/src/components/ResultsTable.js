import React from "react";

export default function ResultsTable(props) {
  return (
    <table className="table table-bordered">
      <tr>
        <th>Total Number of Open Issues</th>
        <th>Issues opened in last 24 hours</th>
        <th>Issues opened in 24 hours to 7 days</th>
        <th>Issues opened before 7 days</th>
      </tr>
      <tr>
        <td>{props.totalOpenIssues}</td>
        <td>{props.last24Hours}</td>
        <td>{props.In24HoursTo7Days}</td>
        <td>{props.before7Days}</td>
      </tr>
    </table>
  );
}
