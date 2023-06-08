# pyspark
import argparse

from pyspark.ml.feature import StopWordsRemover, Tokenizer
from pyspark.sql import SparkSession
from pyspark.sql.functions import array_contains, lit
from pyspark.sql import types
from pyspark import SparkConf

from airflow.models import Connection


def random_text_classifier(input_loc: str, output_loc: str, run_id: str) -> None:
    """
    This is a dummy function to show how to use spark, It is supposed to mock
    the following steps
        1. clean input data
        2. use a pre-trained model to make prediction
        3. write predictions to a HDFS output

    Since this is meant as an example, we are going to skip building a model,
    instead we are naively going to mark reviews having the text "good" as
    positive and the rest as negative
    """

    # read input
    df_raw = spark.read.option("header", True).csv(input_loc, inferSchema=True)
    # perform text cleaning

    # Tokenize text
    tokenizer = Tokenizer(inputCol="review_str", outputCol="review_token")
    df_tokens = tokenizer.transform(df_raw).select("cid", "review_token")

    # Remove stop words
    remover = StopWordsRemover(inputCol="review_token", outputCol="review_clean")
    df_clean = remover.transform(df_tokens).select("cid", "review_clean")

    # function to check presence of good
    df_out = df_clean.select(
        "cid",
        array_contains(df_clean.review_clean, "good").alias("positive_review"),
    )
    df_fin = df_out.withColumn("insert_date", lit(run_id))
    df_fin = df_fin.withColumn("cid", df_fin["cid"].cast(types.StringType()))
    # parquet is a popular column storage format, we use it here
    df_fin.write.mode("overwrite").parquet(output_loc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bucket-name", type=str, help="S3 Bucket Name", default="sde-data-lake-"
    )
    parser.add_argument("--input", type=str, help="HDFS input", default="/movie")
    parser.add_argument("--output", type=str, help="HDFS output", default="/output")
    parser.add_argument("--run-id", type=str, help="run id")
    args = parser.parse_args()
    input_loc = "s3a://" + args.bucket_name + args.input
    output_loc = "s3a://" + args.bucket_name + args.output

    aws_credentials = Connection.get_connection_from_secrets("aws_credentials")
    conf = SparkConf()
    conf.set("spark.hadoop.fs.s3a.access.key", aws_credentials.login)
    conf.set("spark.hadoop.fs.s3a.secret.key", aws_credentials.password)
    conf.set(
        "spark.hadoop.fs.s3a.aws.credentials.provider",
        "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
    )
    conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.2")

    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    random_text_classifier(
        input_loc=input_loc, output_loc=output_loc, run_id=args.run_id
    )
