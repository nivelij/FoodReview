# SIMPLE FOOD RECOMMENDATION
This application is a simple food recommendation, and the purpose of this app is to demonstrate how [Elasticsearch](https://www.elastic.co/what-is/elasticsearch) can become really handy in generating list of results based on certain keyword(s).

## Getting Started
Clone this project to your machine. If you want to run this project in a VM, make sure you have your virtualization software installed. I developed this repository on Oracle VirtualBox 6.1.2

### Prerequisites

Make sure you have ```docker``` installed on your machine.

Install ```docker```:
```
# Setting up docker repository
$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Install docker
$ sudo apt-get update
$ sudo apt-get install docker-ce

# Verify that docker is installed
$ docker --version
```
### Running The Application Locally

1. Build database file into docker image and run it:
```
$ cd db
$ docker build -t foodreview_db .
Sending build context to Docker daemon  13.31kB
Step 1/7 : FROM mariadb:latest as builder
 ---> 37f5f0a258bf
Step 2/7 : RUN ["sed", "-i", "s/exec \"$@\"/echo \"not running $@\"/", "/usr/local/bin/docker-entrypoint.sh"]
 ---> Using cache
 ---> 4b3800c19b22
Step 3/7 : ENV MYSQL_ROOT_PASSWORD=root
 ---> Using cache
 ---> 19015835ee44
Step 4/7 : COPY foodreview.sql /docker-entrypoint-initdb.d/
 ---> Using cache
 ---> 7d5f37542706
Step 5/7 : RUN ["/usr/local/bin/docker-entrypoint.sh", "mysqld", "--datadir", "/initialized-db", "--aria-log-dir-path", "/initialized-db"]
 ---> Using cache
 ---> 6b0c239a1281
Step 6/7 : FROM mariadb:latest
 ---> 37f5f0a258bf
Step 7/7 : COPY --from=builder /initialized-db /var/lib/mysql
 ---> Using cache
 ---> 2a4bb4695adc
Successfully built 2a4bb4695adc
Successfully tagged foodreview_db:latest

$ docker run -d -p 3306:3306 --name=foodreview_db foodreview_db:latest
```

2. Build elastic docker image and run it:
```
$ cd elastic
$ docker build -t foodreview_elastic:latest .
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM docker.elastic.co/elasticsearch/elasticsearch:7.6.2
 ---> f29a1ee41030
Step 2/2 : ENV discovery.type=single-node
 ---> Using cache
 ---> 75376282ae51
Successfully built 75376282ae51
Successfully tagged foodreview_elastic:latest

$ docker run -d -p 9200:9200 -p 9300:9300 --name=foodreview_elastic foodreview_elastic:latest
```

3. Run init script to create elastic index, query all data inserted in DB and pump it to elasticsearch. Ideally this process should be done automatically via direct database - elasticsearch integration, but for the sake of simplicity, the process will be done manually. Hopefully the direct database - elasticsearch integration can be done in the future:
```
$ cd init
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ (env) pip install -r requirements
$ (env) python init.py
{"_index":"foodreview","_type":"_doc","_id":"CCcgeHEBZnDCW-3RSGKh","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"CScgeHEBZnDCW-3RSGKx","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"CicgeHEBZnDCW-3RSGLF","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":2,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"CycgeHEBZnDCW-3RSGLz","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":3,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"DCcgeHEBZnDCW-3RSGL-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":4,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"DScgeHEBZnDCW-3RSWII","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":5,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"DicgeHEBZnDCW-3RSWIS","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":6,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"DycgeHEBZnDCW-3RSWIl","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":7,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"ECcgeHEBZnDCW-3RSWJH","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":8,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"EScgeHEBZnDCW-3RSWJZ","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":9,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"EicgeHEBZnDCW-3RSWJs","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":10,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"EycgeHEBZnDCW-3RSWJ-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":11,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"FCcgeHEBZnDCW-3RSWKL","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":12,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"FScgeHEBZnDCW-3RSWKW","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":13,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"FicgeHEBZnDCW-3RSWKk","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":14,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"FycgeHEBZnDCW-3RSWK0","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":15,"_primary_term":1}
{"_index":"foodreview","_type":"_doc","_id":"GCcgeHEBZnDCW-3RSWLW","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":16,"_primary_term":1}
``` 

4. Finally, run your application:
```
$ cd app
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ (env) pip install -r requirements
$ (env) python main.py

# SEARCH ENGINE SIMULATION #
Hello! Type some food keyword you have in mind:
hot and spicy
=====================================
RESULTS
=====================================
Okonomiyaki - [SCORE 1.6]
Okonomiyaki is a Japanese savory pancake containing a variety of ingredients in a wheat-flour-based batter; it is an example of Konamon (flour-based Japanese cuisine). The name is derived from the word okonomi, meaning "how you like" or "what you like", and yaki meaning "cooked" (usually fried). Okonomiyaki is mainly associated with the Kansai or Hiroshima areas of Japan, but is widely available throughout the country. Toppings and batters tend to vary according to region. In Tokyo, there is a semi-liquid okonomiyaki called monjayaki.
=====================================
Cheesecake - [SCORE 1.58]
Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese (typically cream cheese or ricotta), eggs, and sugar. If there is a bottom layer, it often consists of a crust or base made from crushed cookies (or digestive biscuits), graham crackers, pastry, or sometimes sponge cake. It may be baked or unbaked (usually refrigerated). Cheesecake is usually sweetened with sugar and may be flavored in many different ways. It may be flavored by adding vanilla, spices, lemon, chocolate, pumpkin, or other flavors to the cheese layer. Additional flavors and visual appeal may be added by topping the finished pie with fruit, whipped cream, nuts, cookies, fruit sauce, chocolate syrup, or other toppings.
=====================================
Retrieved in 3 ms

Hello! Type some food keyword you have in mind:
grill chicken and pork
=====================================
RESULTS
=====================================
Roast chicken - [SCORE 5.37]
Roast chicken is chicken prepared as food by roasting whether in a home kitchen, over a fire, or with a rotisserie (rotary spit). Generally, the chicken is roasted with its own fat and juices by circulating the meat during roasting, and therefore, are usually cooked exposed to fire or heat with some type of rotary grill so that the circulation of these fats and juices is as efficient as possible. Roast chicken is a dish that appears in a wide variety of cuisines worldwide.
=====================================
Tonkatsu - [SCORE 1.97]
Tonkatsu is a Japanese dish that consists of a breaded, deep-fried/tempura pork cutlet. It involves cutting the pig's back center into 2-3 centimeter thick slices, coating with panko (bread crumbs), frying them in oil, and then serving with Japanese Worcestershire sauce, rice, and vegetable salad (mainly cabbage). The two main types are fillet and loin. Tonkatsu is often served with shredded cabbage, or on a bed of rice (making it a donburi dish, called Katsudon).
=====================================
Shish taouk - [SCORE 1.85]
Shish taoukis a traditional marinated chicken shish kebab of Middle Eastern cuisine. It is widely eaten in Armenia, Turkey, Azerbaijan, Lebanon, Egypt, Jordan, Syria, Palestine, Iraq, and Israel. A similar dish in Persian cuisine is the traditional jujeh kabab. It is also served in kebab houses in many cities around the world.
=====================================
Shawarma - [SCORE 1.61]
Shawarma is a dish in Middle Eastern cuisine consisting of meat cut into thin slices, stacked in a cone-like shape, and roasted on a slowly-turning vertical rotisserie or spit. Originally made of lamb or mutton, today's shawarma may also be chicken, turkey, beef, or veal. Thin slices are shaved off the cooked surface as it continuously rotates. Shawarma is one of the world's most popular street foods, especially in Egypt and the countries of the Levant, the Arabian Peninsula, and beyond.
=====================================
Filet mignon - [SCORE 1.4]
Filet mignon is a steak cut of beef taken from the smaller end of the tenderloin, or psoas major of the cow carcass, usually a steer or heifer. In French, this cut is always called filet de bÅ“uf ("beef fillet"), as filet mignon refers to pork tenderloin. The tenderloin runs along both sides of the spine, and is usually harvested as two long snake-shaped cuts of beef. The tenderloin is sometimes sold whole. When sliced along the short dimension, creating roughly round cuts, and tube cuts, the cuts (fillets) from the small forward end are considered to be filet mignon. Those from the center are tournedos; however, some butchers in the United States label all types of tenderloin steaks "filet mignon". In fact, the shape of the true filet mignon may be a hindrance when cooking, so most restaurants sell steaks from the wider end of the tenderloin â€“ it is both cheaper and much more presentable.
=====================================
Retrieved in 7 ms
```