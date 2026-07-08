from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Hospital360 Kafka Stream")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "hospital360-kafka:29092")
    .option("subscribe", "hospital-data")
    .option("startingOffsets", "earliest")
    .load()
)

df.printSchema()

query = (
    df.writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()