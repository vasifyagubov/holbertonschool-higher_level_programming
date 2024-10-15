:::RESTful API:::

1. Introduction
A RESTful API (Representational State Transfer) is an architectural style for web-based applications that facilitates data exchange between client and server. REST is based on standard principles that operate over the HTTP protocol. This document outlines the key components, usage, and examples of RESTful APIs.

2. Key Concepts
Resources: In RESTful APIs, everything is represented as a resource. Resources are typically identified by URLs.

HTTP Methods:

GET: Used to retrieve resources.
POST: Used to create new resources.
PUT: Used to update existing resources.
DELETE: Used to remove resources.
Statelessness: Each request must contain all the information needed to understand and process it. The server does not store any client context between requests.

3. URL Structure
Base URL: https://api.example.com/
Example Resources:
All users: /users
Specific user: /users/{id}
4. Response Format
RESTful APIs typically respond in JSON format. An example response might look like this:

json
Copy code
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
5. Example Endpoints
Get All Users:

Request: GET /users
Response: A list of users in JSON format.
Get a Specific User:

Request: GET /users/{id}
Response: Information about the specified user.
6. Error Handling
API responses often include HTTP status codes for error handling. Example status codes:

200 OK: The request was successful.
201 Created: A new resource was created.
404 Not Found: The resource was not found.
500 Internal Server Error: There was a server error.
