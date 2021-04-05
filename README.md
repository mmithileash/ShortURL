# **URL Shortener**
This is a FastAPI project that will take a given url and return a shorter indexed URL by
encoding the URL with a base66 encoding. With this approach we are using a counter to encode 
the incoming shorten url requests with valid url characters. By using a hashing mechanism here 
the given URL would not use up all of the valid URL characters and hashing could also potentially 
lead to lot of hash collisions. Using a counter will help with that issue but could potentially lead to 
problems when scaling the solution horizontally across multiple machines. Since we are using MongoDB
to store the index, we could possibly scale up the web service but the scaling-up will be bottle necked 
to MongoDB. An alternative approach would be to use a co-ordination service such as zookeeper to manage 
a range of counters for each horizontally scaled instance which will help scale up better. 

If I had more time I could have included a caching system such as Redis to
improve the response times. In addition the provided solution currently doesn't include 
any load balancers when this service is scaled horizontally; this is another thing I would
have liked to have included in this solution.


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
 