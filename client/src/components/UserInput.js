import React, { Component } from "react";

export default class UserInput extends Component {
  constructor() {
    super();
    this.state = {
      data: null,
      userInput: "",
      suggestions: ""
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    //connect with Node backend
    this.callBackendAPI()
      .then(res => this.setState({ data: res.express }))
      .catch(err => console.log(err));
  }

  callBackendAPI = async () => {
    const response = await fetch(
      "http://ec2-18-191-151-183.us-east-2.compute.amazonaws.com:5000/express_backend"
    );
    const body = await response.json();

    if (response.status !== 200) {
      throw Error(body.message);
    }
    return body;
  };

  handleChange(e) {
    this.setState({ userInput: e.target.value });
  }

  handleSubmit = async e => {
    console.log("submit was clicked");
    e.preventDefault();
    const response = await fetch(
      "http://ec2-18-191-151-183.us-east-2.compute.amazonaws.com:5000/suggest",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ userInput: this.state.userInput })
      }
    );

    const body = await response.json();

    console.log(body.suggestions);
    this.setState({
      suggestions: body.suggestions
    });
  };
  render() {
    return (
      <div class="row container">
        <form class="col s12">
          <div class="row">
            <div class="input-field col s6">
              <i class="material-icons prefix">mode_edit</i>
              <input
                placeholder="Be patient after clicking the button. Still working on speed."
                value={this.state.userInput}
                onChange={this.handleChange}
                id="first_name"
                type="text"
                class="validate"
              />
              <button
                class="btn waves-effect waves-light"
                type="submit"
                name="action"
                onClick={this.handleSubmit}
              >
                Suggest Rhymes
                <i class="material-icons right">send</i>
              </button>
              <div>{this.state.suggestions}</div>
            </div>
          </div>
        </form>
      </div>
    );
  }
}
