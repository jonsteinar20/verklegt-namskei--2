# verklegt-namskei--2
TITLE:
Fire Sale - It is a website similar to the US based website Craigslist.com where people auction their own items and bid on other peoples items.

PROJECT DESCRIPTION:
In this application you can view all items that have been put up to auction by people of the site.
You can create an account and from there you can auction off your very own items.
Every item has an image of itself and a detailed description along with a condition state of the item.

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