#!/bin/bash
# display size of the fetched response
curl -Is $1 | tr -d '\r' | sed -En 's/^Content-Length: (.*)/\1/p';
