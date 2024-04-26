#!/bin/bash
# send a post request with params
curl -s -d '{"name":"John","age":"33"}' $1;
