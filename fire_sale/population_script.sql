INSERT INTO user_profile (name, bio, profile_image) VALUES('unnur gunnlaugsdottir', 'vegan, 20 plants, 10 cats.', 'https://i2-prod.mirror.co.uk/incoming/article14276690.ece/ALTERNATES/s1200b/1_Susan-Boyle.jpg');
INSERT INTO user_profile (name, bio, profile_image) VALUES('unnur@ru.is', 'i like mimosas on the beach, im a tanist, yay springbreak', 'https://www.spicinfoods.com/pub/media/magefan_blog/shaq-hot-ones-6_1.jpg');
INSERT INTO user_profile (name, bio, profile_image) VALUES('jon steinar', '300 pounds of pure muscle', 'https://cdn.images.express.co.uk/img/dynamic/1/750x445/1573810.jpg');
INSERT INTO user_profile (name, bio, profile_image) VALUES('andri freysson', 'curly boy, i like to watch the sun set and dream about a brighter tomorrow', 'https://dynaimage.cdn.cnn.com/cnn/q_auto,h_600/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F160822143039-redhead-convention-1.jpg');
INSERT INTO user_profile (name, bio, profile_image) VALUES('jon jonsson', 'i like turtles', 'https://cdn.cnn.com/cnnnext/dam/assets/220428123119-weightlifter-forced-to-remove-hair-beads-orig-mg-jk-00001523-large-169.png');

INSERT INTO item_itemcategory (name) VALUES('Electronics');
INSERT INTO item_itemcategory (name) VALUES('Shoes');
INSERT INTO item_itemcategory (name) VALUES('Clothes');
INSERT INTO item_itemcategory (name) VALUES('Accessories');
INSERT INTO item_itemcategory (name) VALUES('Books');
INSERT INTO item_itemcategory (name) VALUES('Toys and Games');
INSERT INTO item_itemcategory (name) VALUES('Home supplies');
INSERT INTO item_itemcategory (name) VALUES('Other');

INSERT INTO item_item (id, name, description, price, category_id, condition, seller_username) VALUES (1, 'iPhone 13 pro 64GB', 'phone in good condition bought 1 year ago', 399.99, 1, 'excellent', 'unnurosk123');
INSERT INTO item_item (id, name, description, price, category_id, condition, seller_username) VALUES (2, 'Designer glasses', 'Glasses from the 60s very antique', 1300.99, 4, 'good', 'jonjons');
INSERT INTO item_item (id, name, description, price, category_id, condition, seller_username) VALUES (3, 'Red GUCCI sweater', 'Size Large good condition', 299.99, 3, 'great', 'andri12');
INSERT INTO item_item (id, name, description, price, category_id, condition, seller_username) VALUES (4, 'Harry Potter books collection', 'All books', 99.99, 5, 'medium', 'jonni44');


INSERT INTO item_itemimage (image, item_id) VALUES('https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/iphone-13-pro-family-hero?wid=940&hei=1112&fmt=png-alpha&.v=1644969385433', 1);
INSERT INTO item_itemimage (image, item_id) VALUES('https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6487/6487447_sd.jpg;maxHeight=640;maxWidth=550', 1);
INSERT INTO item_itemimage (image, item_id) VALUES('https://vintageopticalshop.com/pub/media/catalog/product/cache/35f0af62944548dabfe95b26fc51f959/i/m/img_7510_3.jpg', 2);
INSERT INTO item_itemimage (image, item_id) VALUES('https://cdn.childrensalon.com/media/catalog/product/g/u/gucci-red-cotton-logo-sweatshirt-281471-37f042d59b20aad21f573f5c7b468555f5374830.jpg', 3);
INSERT INTO item_itemimage (image, item_id) VALUES('https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/auto_image/cache=expiry:max/rotate=deg:exif/resize=height:335/output=quality:90/compress/x56uKgHORXCMZJDCBEOF', 3);
INSERT INTO item_itemimage (image, item_id) VALUES('https://images-na.ssl-images-amazon.com/images/I/51FOjToUEkL.jpg', 4);
INSERT INTO item_itemimage (image, item_id) VALUES('https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1534298934i/862041._SS1200_.jpg', 4);


