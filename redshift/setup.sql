DROP TABLE IF EXISTS spectrum.user_purchase_staging;
CREATE EXTERNAL TABLE spectrum.user_purchase_staging (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(20),
    detail VARCHAR(1000),
    Quantity INTEGER,
    InvoiceDate TIMESTAMP,
    UnitPrice DECIMAL(8, 3),
    customerid INTEGER,
    Country VARCHAR(20)
) PARTITIONED BY (insert_date DATE) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS textfile LOCATION 's3://sde-data-lake-20230609072906277200000002/stage/user_purchase/' TABLE PROPERTIES ('skip.header.line.count' = '1');
DROP TABLE IF EXISTS spectrum.classified_movie_review;
CREATE EXTERNAL TABLE spectrum.classified_movie_review (
    cid VARCHAR(100),
    positive_review boolean,
    insert_date VARCHAR(12)
) STORED AS PARQUET LOCATION 's3://sde-data-lake-20230609072906277200000002/stage/movie_review/';
DROP TABLE IF EXISTS public.user_behavior_metric;
CREATE TABLE public.user_behavior_metric (
    customerid INTEGER,
    amount_spent DECIMAL(18, 5),
    review_score INTEGER,
    review_count INTEGER,
    insert_date DATE
);