import React, { Component } from "react";
import "./Attendance.css";
import AttendanceTable from "./components/AttendanceTable";

export default class Attendance extends Component {
  render() {
    return (
      <AttendanceTable
        eventId={this.props.event ? this.props.event.id : 0}
        location={this.props.location && this.props.location.search}
      />
    );
  }
}
