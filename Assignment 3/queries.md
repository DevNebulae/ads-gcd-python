```
CREATE TABLE users(id int, item_id int, rating int, ts int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE;
```

```
LOAD DATA INPATH '/user/cloudera/u.user' INTO TABLE users;
```

SELECT users.gender, items.title, AVG(ratings.rating) AS rat
FROM users, items, ratings
WHERE users.user_id = ratings.user_id AND ratings.item_id = items.movie_id
GROUP BY users.gender, items.title
ORDER BY users.gender, rat DESC
LIMIT 10;
