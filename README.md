# Creative Work Tax Manager

##  Running the Application

To start the app, open your console and use the following command:  

```bash
flask --app app run --debug
```
- This command starts the Flask application in debug mode, providing detailed error messages and automatic restarts when code changes are detected.

## Starting the Database
To initialize and run the database using Docker, execute the following command:
```bash
docker compose up -d
```

##  Sample Insert of Evidence
You can insert a sample piece of evidence using the following curl command:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Sample Evidence\",\"description\":\"This is a sample description.\",\"date\":\"2025-04-27\"}" http://127.0.0.1:5000/api/evidence/
```

- This command sends a POST request to the application’s API endpoint, adding a new piece of evidence with a name, description, and date.

##  Sample Deletion of Evidence
```bash
curl -X DELETE http://127.0.0.1:5000/api/evidence/4 
```

## Dependencies
Ensure you have the following installed:
- **Python 3.x**
- **Flask**
- **Docker and Docker Compose**