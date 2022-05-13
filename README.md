# verklegt-namskei--2
TITLE:
Tombola - It is a website similar to the US based website Craigslist.com where people auction their own items and bid on other peoples items.

PROJECT DESCRIPTION:
For this assignment we had to create a platform on which users can purchase and sell items between them selves. 
On the site users are able to create an account through whicvh they will be able to put up items, along with 
details of the item such as images and condition as well as the requested price. Other users will be able to bid 
for the item upon which the seller of the item can accept the bid. The buyer then gives his information and the 
two parties are able to make an exchange.

HOW TO INSTALL AND RUN THE PROJECT:
Clone the repo.
https://github.com/jonsteinar20/verklegt-namskei--2
https://github.com/jonsteinar20/verklegt-namskei--2.git
Run pip freeze > requirements.txt
Run pip install -r requirements.txt
Run this for population of sql:
INSERT INTO item_itemcategory (name) VALUES('Electronics');
INSERT INTO item_itemcategory (name) VALUES('Shoes');
INSERT INTO item_itemcategory (name) VALUES('Clothes');
INSERT INTO item_itemcategory (name) VALUES('Accessories');
INSERT INTO item_itemcategory (name) VALUES('Books');
INSERT INTO item_itemcategory (name) VALUES('Toys and Games');
INSERT INTO item_itemcategory (name) VALUES('Home supplies');
INSERT INTO item_itemcategory (name) VALUES('Other');

Credits:
Jón Steinar - jonsteinar20
Unnur Sóley Lindudóttir - unnursoley
Unnur Ósk Gunnlaugsdóttir - unnuroskg10
Andri Freysson - andrifreys

HOW TO CONTRIBUTE TO THE PROJECT (flaws):
There is no flow in the checkout process.
There is no flow in accepting an existing bid.
Highest offer never changes.

ALL REQUIREMENTS:
Arpeggio==1.10.2
asgiref==3.5.0
astroid==2.4.2
backports.zoneinfo==0.2.1
colorama==0.4.3
coverage==5.5
Django==4.0.4
django-appconf==1.0.5
django-compressor==4.0
django-libsass==0.9
flake8==3.8.3
isort==4.3.21
Jinja2==3.0.1
lazy-object-proxy==1.4.3
libsass==0.21.0
MarkupSafe==2.0.1
mccabe==0.6.1
Pillow==9.1.0
psycopg2-binary==2.9.3
pycodestyle==2.6.0
pyflakes==2.2.0
pylint==2.5.3
rcssmin==1.1.0
rjsmin==1.2.0
six==1.16.0
sortedcontainers==2.3.0
sqlparse==0.4.2
textX==2.3.0
toml==0.10.1
tzdata==2022.1
websockets==10.0
wrapt==1.12.1