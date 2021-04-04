docker rm tests
docker-compose build short_url \
  && echo 'Running tests' \
  && docker-compose run --name tests short_url python -m unittest \
  && echo 'Test run complete'
