"""  
API Endpoints and Making API Calls 

International Space Station Current Location
The International Space Station is moving at close to 28,000 km/h so its location changes really fast! Where is it right now?

Overview
This is a simple api to return the current location of the ISS. It returns the current latitude and longitude of the space station with a unix timestamp for the time the location was valid. This API takes no inputs.

Output
JSON
http://api.open-notify.org/iss-now.json

{
  "message": "success", 
  "timestamp": UNIX_TIME_STAMP, 
  "iss_position": {
    "latitude": CURRENT_LATITUDE, 
    "longitude": CURRENT_LONGITUDE
  }
}
The data payload has a timestamp and an iss_position object with the latitude and longitude.

https://www.webfx.com/web-development/glossary/http-status-codes/


1xx Informational
100 Continue
101 Switching Protocols
102 Processing
2×× Success
200 OK
201 Created
202 Accepted
203 Non-authoritative Information
204 No Content
205 Reset Content
206 Partial Content
207 Multi-Status
208 Already Reported
226 IM Used
3×× Redirection
300 Multiple Choices
301 Moved Permanently
302 Found
303 See Other
304 Not Modified
305 Use Proxy
307 Temporary Redirect
308 Permanent Redirect
4×× Client Error
400 Bad Request
401 Unauthorized
402 Payment Required
403 Forbidden
404 Not Found
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required
408 Request Timeout
409 Conflict
410 Gone
411 Length Required
412 Precondition Failed
413 Payload Too Large
414 Request-URI Too Long
415 Unsupported Media Type
416 Requested Range Not Satisfiable
417 Expectation Failed
418 I’m a teapot
421 Misdirected Request
422 Unprocessable Entity
423 Locked
424 Failed Dependency
426 Upgrade Required
428 Precondition Required
429 Too Many Requests
431 Request Header Fields Too Large
444 Connection Closed Without Response
451 Unavailable For Legal Reasons
499 Client Closed Request
5×× Server Error
500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported
506 Variant Also Negotiates
507 Insufficient Storage
508 Loop Detected
510 Not Extended
511 Network Authentication Required
599 Network Connect Timeout Error

https://www.latlong.net/Show-Latitude-Longitude.html#google_vignette

https://pypi.org/project/requests/


1XX: Hold On

2XX: Here you go

3XX: Go Away

4XX: You Screwed Up

5XX: I screwed up

"""

ISS_API_URL = "http://api.open-notify.org/iss-now.json"

import requests

response = requests.get(url=ISS_API_URL)

print(response.raise_for_status)

# API resonse code
print(response.status_code)

# API Response Code in Object
print(response)

# API Response in JSON
data = response.json()
print(data)

iss_position_data = data["iss_position"]
print(iss_position_data)

iss_position_latitude_data = data["iss_position"]["latitude"]
print(iss_position_latitude_data)

iss_position_longitude_data = data["iss_position"]["longitude"]
print(iss_position_longitude_data)

iss_position = (iss_position_latitude_data, iss_position_longitude_data)
print(iss_position)