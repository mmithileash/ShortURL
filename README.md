# **URL Shortener**
This is a FastAPI project that will take a given url and return a shorter indexed URL by
encoding the URL with base66 encoding. 

# **Tech stack**
* Python 3.8
* FastAPI
* Docker
* MongoDB

# **Running the app**
1. Install docker
2. `CD` into this project folder (`/ShortUrl`)
3. Then run `docker-compose up`
4. The application can then be accessed on http://localhost:80
5. The docs can be accessed at: http://localhost:80/docs
5. To create short url please run: 
`curl --request POST \
  --url http://localhost:80/shorten_url/ \
  --header 'Content-Type: application/json' \
  --data '{
	"long_url": "http://www.example.com/"
}'`
6. To retrieve a url please run:
`curl --request GET \
  --url http://localhost:80/short_code \
  --header 'Content-Type: application/json'`
  
# **Running Tests**
1. Install docker
2. Run script under `bin\run_tests.sh`

# **Deploy script to AWS**
Running the script below will create an EC2 instance and run docker compose 
`ansible-playbook provision.yml -vv --private-key AnsibleEC2.pem` 
Note that we need to pass the key pair (.pem) file appropriately.
 