#!/bin/bash
# list allowed http verbs
curl -s -i -L -X OPTIONS $1 | tr -d '\r' | sed -En 's/^Allow: (.*)/\1/p'
