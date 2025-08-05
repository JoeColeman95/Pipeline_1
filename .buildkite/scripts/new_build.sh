echo "~~~ Uploading pipeline"
cat .buildkite/test1.yml

# Handle duplicate key errors gracefully
if ! upload_output=$(buildkite-agent pipeline upload .buildkite/test1.yml 2>&1); then
  if echo "$upload_output" | grep -q "already been used by another step"; then
    echo "Pipeline upload failed due to duplicate keys, ignoring error"
    echo "$upload_output"
  else
    echo "Pipeline upload failed: $upload_output"
    exit 1
  fi
else
  echo "Pipeline upload successful"
fi