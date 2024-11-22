# Flask Web Application

This repository contains a simple Flask web application that provides several routes to render HTML templates, calculate scores based on form input, and handle JSON-based API requests.

## Features

1. **Home Page**:
   - Route: `/`
   - Method: `GET`
   - Displays a welcome message.

2. **Index Page**:
   - Route: `/index`
   - Method: `GET`
   - Displays a secondary message.

3. **Score-based Result Calculation**:
   - Route: `/calculate`
   - Methods: `GET`, `POST`
   - Functionality:
     - On `GET`: Displays an HTML form (`form.html`) where users can input scores for three subjects.
     - On `POST`: Processes the form data, calculates the total and average scores, and redirects to either a "success" or "fail" page based on the following conditions:
       - **Success**: `average_score >= 50` and `total_score >= 150`
       - **Fail**: Otherwise

4. **Dynamic Routes**:
   - **Success Message**:
     - Route: `/success/<int:total_score>/<float:average_score>`
     - Displays a congratulatory message with the calculated total and average scores.
   - **Failure Message**:
     - Route: `/fail/<int:total_score>/<float:average_score>`
     - Displays a failure message with the calculated total and average scores.

5. **API Endpoint**:
   - Route: `/api`
   - Method: `POST`
   - Accepts a JSON payload with two numbers (`a` and `b`), calculates their sum, and returns the result in JSON format.

## Installation and Usage

1. **Clone the repository**:
   ```bash
   cd <your-repository-folder>
   git clone https://github.com/PrashantMali07/first-flask-app.git
