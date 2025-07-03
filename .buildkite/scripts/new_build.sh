#!/bin/bash

RELEASE_NAME=$(buildkite-agent meta-data get release-name)

curl -H "Authorization: Bearer $BUILDKITE_API_TOKEN" \
  -X POST "https://api.buildkite.com/v2/organizations/joe-playground/pipelines/pipeline-1/builds" \
  -H "Content-Type: application/json" \
  -d "{
    \"message\": \"$RELEASE_NAME\"
  }"