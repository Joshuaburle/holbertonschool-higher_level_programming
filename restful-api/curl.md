Consuming Data from an API using curl
Overview

curl (Client URL) is a command-line tool used to communicate with servers using protocols such as HTTP and HTTPS.
It is commonly used to test APIs, debug network requests, and inspect server responses.

Public API used: JSONPlaceholder

Check Installation
curl --version


Displays the installed version and supported protocols.

Basic Request

Fetch a webpage:

curl http://example.com


This sends a GET request and returns HTML content.

Fetch Data from an API

Retrieve posts from JSONPlaceholder:

curl https://jsonplaceholder.typicode.com/posts


Result:
Returns a JSON array containing posts with:

userId

id

title

body

View Only Response Headers
curl -I https://jsonplaceholder.typicode.com/posts


The -I option shows only metadata:

HTTP status code

Content-Type

Cache information

Server details

Send a POST Request
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts


Options:

-X → specify HTTP method

-d → send request data

Result:
The API simulates creation and returns a new resource (usually with id 101).

Optional: Format JSON Output
curl https://jsonplaceholder.typicode.com/posts | jq


Makes JSON readable in the terminal.

Expected Results
Command	Expected Output
curl --version	Shows curl version
GET request	JSON list of posts
-I	Only headers
POST request	Created resource response
Key Takeaway

curl allows direct interaction with APIs from the terminal by sending HTTP requests and inspecting responses, making it an essential tool for testing and debugging web services.