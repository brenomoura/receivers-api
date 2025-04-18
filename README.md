# receivers-api

This project is an application developed using Domain-Driven Design (DDD) concepts, where the structure is divided into domain, application, and infrastructure layers to ensure a high level of decoupling.

## Project Structure

- **Domain**: This layer contains the business entities and domain rules of the application.
- **Application**: Here you will find the application services that orchestrate business operations using domain elements.
- **Infrastructure**: Responsible for integrating the application with external resources, such as databases, and also providing endpoints to handle requests.

## Technologies Used
The programming language used was Python, version 3.12. Additionally, the following technologies were employed:

- **Django-Ninja**: A framework for building RESTful APIs in Python, enabling fast and efficient API development. [link](https://github.com/vitalik/django-ninja).
- **PostgreSQL**: A relational database used to store application data.
- **Docker and Docker Compose**: Used to containerize the application and its services, ensuring a consistent and portable development environment.

## How to Run

To run the application via Docker, follow the steps below:
1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project's root directory.
4. Run the following command to build and start the Docker containers:
```
docker-compose up --build
```
or
```
./run-containers.sh
```
5. Wait until all services are initialized. Once completed, the application will be available and ready for use. NOTE: The database will be pre-populated with 30 test records. Additionally, for testing purposes, you can populate it with different values using the following command (to run this command, ensure your local environment is configured [as explained in the testing section](#running-tests)):
```
python manage.py pre_populate_receivers -n <desired number of records>
```
6. Access the application at [http://localhost:8000](http://localhost:8000) and start exploring its features.

## Running Tests
This project includes comprehensive test coverage, including unit tests and integration tests, to ensure the correct functionality of implemented features.
To run the tests using Pytest, follow the steps below:

### 1. Setting Up the Local Development Environment

Ensure Python is installed on your machine (Python version 3.12 was used in this project). Next, follow the steps below to set up the development environment:

#### Creating and Activating a Virtual Environment

```bash
python3.12 -m venv venv
source venv/bin/activate
```

#### Installing Development Dependencies

```bash
pip install -r src/dev_requirements.txt
```

### 2. Configuring Environment Variables
Create the `.env` file. A template file named `.env_template` is provided for reference. For running tests, set the `DEBUG` variable to `False` and `ENV` to `dev`.

### 3. Setting Up the Database
Ensure the PostgreSQL database is configured and running according to the settings specified in the `docker-compose.yaml` file. Additionally, run the migrations if you haven't already:
```bash
python src/manage.py migrate
```

### 4. Running the Tests
With the development environment configured and the database running, execute the following command to run the tests with Pytest:
```bash
pytest
```
This will run all tests in the current directory and subdirectories, displaying results in the terminal.
To run specific tests or customize test execution, refer to the [Pytest documentation](https://docs.pytest.org/en/stable/contents.html) for more details.

## API Documentation

The API includes Swagger documentation, where you can view and interact with the available endpoints. The documentation can be accessed at:
[http://localhost:8000/api/docs](http://localhost:8000/api/docs)
