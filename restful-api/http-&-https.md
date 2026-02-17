# HTTP & HTTPS — Quick Summary

## 1. What is HTTP?

HTTP (Hypertext Transfer Protocol) is the basic communication protocol used by web browsers and servers to exchange data.

* Client sends a request
* Server processes it
* Server returns a response

It is **stateless**: each request is independent.

---

## 2. HTTP vs HTTPS

| Feature         | HTTP               | HTTPS                        |
| --------------- | ------------------ | ---------------------------- |
| Security        | None               | Encrypted (SSL/TLS)          |
| Data visibility | Anyone can read it | Protected from eavesdropping |
| Tampering       | Possible           | Prevented (integrity check)  |
| URL             | http://            | https://                     |

**Key idea:** HTTPS = HTTP + encryption layer.

Used for sensitive data (logins, payments, personal information).

---

## 3. HTTP Request Structure

Example:

```
GET /users HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: application/json
```

**Parts:**

* Method → action to perform
* Path → resource requested
* Headers → metadata about the request
* Body → optional data (POST/PUT/PATCH)

---

## 4. HTTP Response Structure

Example:

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 85

{ "name": "Alice" }
```

**Parts:**

* Status Code → result of the request
* Headers → information about the response
* Body → returned data

---

## 5. Common HTTP Methods

| Method | Purpose          | Typical Use Case                 |
| ------ | ---------------- | -------------------------------- |
| GET    | Retrieve data    | Load a web page / fetch API data |
| POST   | Create data      | Submit a form / create a user    |
| PUT    | Replace data     | Update a full resource           |
| PATCH  | Modify partially | Update a field (email, name)     |
| DELETE | Remove data      | Delete an account                |

---

## 6. Common HTTP Status Codes

### 2xx — Success

| Code | Meaning | Example                  |
| ---- | ------- | ------------------------ |
| 200  | OK      | Page loaded successfully |
| 201  | Created | New resource created     |

### 3xx — Redirection

| Code | Meaning           | Example          |
| ---- | ----------------- | ---------------- |
| 301  | Moved Permanently | Page URL changed |

### 4xx — Client Errors

| Code | Meaning      | Example                |
| ---- | ------------ | ---------------------- |
| 400  | Bad Request  | Invalid input data     |
| 401  | Unauthorized | Not logged in          |
| 403  | Forbidden    | No permission          |
| 404  | Not Found    | Resource doesn't exist |

### 5xx — Server Errors

| Code | Meaning               | Example           |
| ---- | --------------------- | ----------------- |
| 500  | Internal Server Error | Server crashed    |
| 503  | Service Unavailable   | Server overloaded |

---

## Key Takeaways

* HTTP is the communication protocol of the web
* HTTPS secures it using encryption
* Requests ask for resources
* Responses return results
* Methods define actions
* Status codes describe outcomes
