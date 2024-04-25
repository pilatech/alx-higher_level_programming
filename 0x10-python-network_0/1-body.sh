#!/bin/bash
# display size of the fetched response
code=$(curl -s -o /dev/null -w "%{http_code}" $1);
if [[ $code -eq 200 ]]; then
	curl -s $1;
fi
