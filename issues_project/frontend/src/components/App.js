import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import axios from "axios";
import ResultsTable from "./ResultsTable";

class App extends Component {
  state = {
    url: "",
    totalOpenIssues: 0,
    last24Hours: 0,
    In24HoursTo7Days: 0,
    before7Days: 0,
    isLoading: false
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });
  onSubmit = e => {
    this.setState({ isLoading: true });
    e.preventDefault();
    const { url } = this.state;
    axios
      .post("http://localhost:8000/issues/api/", { url })
      .then(response => response.data)
      .then(data =>
        this.setState({
          isLoading: false,
          totalOpenIssues: data.total,
          In24HoursTo7Days: data.In24HoursTo7Days,
          last24Hours: data.last24Hours,
          before7Days: data.before7Days
        })
      );
    // .catch()
  };
  render() {
    const {
      totalOpenIssues,
      last24Hours,
      In24HoursTo7Days,
      before7Days
    } = this.state;
    let props = {
      totalOpenIssues,
      last24Hours,
      In24HoursTo7Days,
      before7Days
    };
    return (
      <div className="container" style={{ marginTop: 60 }}>
        <div>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Enter Github Url:</label>
              <input
                className="form-control"
                type="text"
                name="url"
                onChange={this.onChange}
                value={this.state.url}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
          </form>
        </div>
        {this.state.isLoading ? <p>Loading...</p> : null}
        <ResultsTable {...props} />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
