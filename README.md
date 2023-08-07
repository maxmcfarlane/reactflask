# React-Flask Application Template

A simple and efficient template for building web applications using React for the frontend and Flask for the backend.

## Features

- 📦 Integrated React + Flask setup.
- 🔄 Hot-reloading for both frontend and backend development.
- 🔒 Security configurations.
- 🌐 API route examples.
- 🎨 Styled with Bootstrap (or any other styling of choice).

## Prerequisites

- [Node.js](https://nodejs.org/) & [npm](https://www.npmjs.com/)
- [Python](https://www.python.org/) & [pip](https://pip.pypa.io/en/stable/)

## Setup

### Backend

1. Navigate to the oot directory:

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd client
   ```

2. Install the required node packages:
   ```bash
   npm install
   ```

## Running the Application

### Backend

1. In the root directory, run:
   ```bash
   flask run
   ```

### Frontend

1. In the frontend directory, run:
   ```bash
   npm start
   ```

Visit `http://localhost:3000` in your browser to see the React frontend. The Flask API will be running on `http://localhost:5000`.

