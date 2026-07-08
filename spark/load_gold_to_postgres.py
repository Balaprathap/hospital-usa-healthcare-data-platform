from pyspark.sql import SparkSession
from pyspark.sql.functions import round, col

spark = (
    SparkSession.builder
    .appName("Load Gold KPIs to PostgreSQL")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

gold_df = spark.read.parquet("/opt/spark/work-dir/gold/state_kpis")

gold_df = gold_df.withColumn(
    "avg_hospital_rating",
    round(col("avg_hospital_rating"), 2)
)

(
    gold_df.write
    .format("jdbc")
    .option("url", "jdbc:postgresql://hospital360-postgres:5432/hospital360_dw")
    .option("dbtable", "gold_state_kpis")
    .option("user", "hospital360")
    .option("password", "hospital360")
    .option("driver", "org.postgresql.Driver")
    .mode("overwrite")
    .save()
)

print("Gold data loaded to PostgreSQL successfully")

spark.stop()