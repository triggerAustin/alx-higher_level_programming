#!/bin/bash
#sends a DELETE request to URL and displays the body of the response
curl -sb /dev/null -X DELETE "$1"
