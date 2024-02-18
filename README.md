# govtech-gds-ta

Technical Assessment for GovTech, Government Digital Services, under CC4.0 - Data Engineer Role.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Follow these steps to set up your project environment.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x
- pip (Python package manager)

### Setup

Follow these steps to set up your development environment:

1. **Clone the Repository**

    Clone the project repository to your local machine using Git:

    ```bash
    git clone https://github.com/koiljat/govtech-gds-ta.git
    ```

2. **Create a Virtual Environment**

    Navigate to the project directory:

    ```bash
    cd govtech-gds-ta
    ```

    Then, create a virtual environment named `venv` (or any name you prefer):

    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

      ```cmd
      .\venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**

    With the virtual environment activated, install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    This command installs all the necessary Python packages listed in `requirements.txt`.

### Running the Project

After setting up the virtual environment and installing the dependencies, you're ready to run the project. Here's an overview of the project structure and how to execute it:

- **Jupyter Notebook**: For experimental code development, this outlines the development of the functions found in main.py.
- **main.py**: The executable script for the data pipeline, you will need to run this script to generate the results for task 1.
- **Helper Functions**: Located in the `task1` folder, with specific functions for each subtask in `task1a`, `task1b`, and `task1c`.
- **Data Retrieval**: Attempts to fetch JSON data from the provided URL. In case of errors, the JSON dataset is available in the `data` folder. See `main.py` for instructions on adjusting the data source.
- **Results**: You may find ther result for task 1 in the resutls folder. Alternatively, you may also run the main.py script and the csv files will be saved to the local folder.

## Task 1 part 3

The results for the ratings threshold can be found in the resutls folder.

Excellent: 4.5 to 4.9

Very Good: 4 to 4.4

Good: 3.5 to 3.9

Average: 2.5 to 3.4

Poor: 2.2 to 2.2 (Below 2.5)

## Task 2

![image](https://github.com/koiljat/govtech-gds-ta/assets/124496128/56852e6a-a4f4-4a42-92bd-8f48f020542c)

- Amazon API Gateway: Entry point for the Carpark Availability API, handling incoming requests.
- AWS Lambda: Serverless compute to process the requests and query the database.
- Amazon DynamoDB: To store and manage carpark details and availability data.
- Amazon CloudFront: CDN for caching API responses to reduce latency and load on the backend.

The use of serverless technologies like AWS Lambda and DynamoDB can handle the variable load during peak hours effectively and are cost-efficient due to the pay-as-you-go model.


A simple swagger documentation can be found here: https://koiljat.github.io/govtech-gds-ta/
