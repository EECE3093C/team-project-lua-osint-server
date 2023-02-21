# OSINT Tool Platform

This is the backend server for Project Name, built using [FastAPI](https://fastapi.tiangolo.com/) framework.

## Requirements

- `Python 3.8` or higher
- `pip` package installer

## Installation

1. Clone the repository:

```bash
git clone git@github.com:EECE3093C/osint-server.git server
cd server
```

2. Install the dependencies:

```bash
source ./.vevn/bin/activate
pip install -r requirements.txt
```

## Usage

3. Start the server:

```bash
uvicorn main:app --reload
```

Open your web browser and navigate to http://localhost:8000/. You should see the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/) page.
