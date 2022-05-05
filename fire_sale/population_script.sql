INSERT INTO user_user (username, firstname, lastname, password, email) VALUES('unnurosk123', 'unnur', 'gunnlaugsdottir', 'Sk9999', 'unnurosk@ru.is')
INSERT INTO user_user (username, firstname, lastname, password, email) VALUES('unnursoley', 'unnur', 'soley', 'La8m134', 'unnur@ru.is')
INSERT INTO user_user (username, firstname, lastname, password, email) VALUES('jonni44', 'jon', 'steinar', 'P00mbbl', 'jonni@gmail.com')
INSERT INTO user_user (username, firstname, lastname, password, email) VALUES('andri12', 'andri', 'freysson', 'Andri991', 'andri@hotmail.com')
INSERT INTO user_user (username, firstname, lastname, password, email) VALUES('jonjons', 'jon', 'jonsson', 'Jj123456', 'jonjonsson@gmail.com')

INSERT INTO item_itemcategory (id, name) VALUES(1, 'Electronics');
INSERT INTO item_itemcategory (id, name) VALUES(2, 'Shoes');
INSERT INTO item_itemcategory (id, name) VALUES(3, 'Clothes');
INSERT INTO item_itemcategory (id, name) VALUES(4, 'Accessories');
INSERT INTO item_itemcategory (id, name) VALUES(5, 'Books');
INSERT INTO item_itemcategory (id, name) VALUES(6, 'Toys and Games');
INSERT INTO item_itemcategory (id, name) VALUES(7, 'Home supplies');
INSERT INTO item_itemcategory (id, name) VALUES(8, 'Other');

INSERT INTO item_item (id, name, description, price, category_id, seller_username) VALUES (1, 'iPhone 13 pro 64GB', 'phone in good condition bought 1 year ago', 399.99, 1, 'unnurosk123')
INSERT INTO item_item (id, name, description, price, category_id, seller_username) VALUES (2, 'Designer glasses', 'Glasses from the 60s very antique', 1300.99, 4, 'jonjons')
INSERT INTO item_item (id, name, description, price, category_id, seller_username) VALUES (3, 'Red GUCCI sweater', 'Size Large good condition', 299.99, 3, 'andri12')
INSERT INTO item_item (id, name, description, price, category_id, seller_username) VALUES (4, 'Harry Potter books collection', 'All books', 99.99, 5, 'jonni44')


INSERT INTO item_itemimage (image, item_id) VALUES('https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/iphone-13-pro-family-hero?wid=940&hei=1112&fmt=png-alpha&.v=1644969385433', 1)
INSERT INTO item_itemimage (image, item_id) VALUES('https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6487/6487447_sd.jpg;maxHeight=640;maxWidth=550', 1)
INSERT INTO item_itemimage (image, item_id) VALUES('https://vintageopticalshop.com/pub/media/catalog/product/cache/35f0af62944548dabfe95b26fc51f959/i/m/img_7510_3.jpg', 2)
INSERT INTO item_itemimage (image, item_id) VALUES('https://cdn.childrensalon.com/media/catalog/product/g/u/gucci-red-cotton-logo-sweatshirt-281471-37f042d59b20aad21f573f5c7b468555f5374830.jpg', 3)
INSERT INTO item_itemimage (image, item_id) VALUES('https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/auto_image/cache=expiry:max/rotate=deg:exif/resize=height:335/output=quality:90/compress/x56uKgHORXCMZJDCBEOF', 3)
INSERT INTO item_itemimage (image, item_id) VALUES('https://images-na.ssl-images-amazon.com/images/I/51FOjToUEkL.jpg', 4)
INSERT INTO item_itemimage (image, item_id) VALUES('https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1534298934i/862041._SS1200_.jpg', 4)

