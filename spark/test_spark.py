from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Hospital360 Spark Test")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

data = [
    ("010001", "SOUTHEAST HEALTH MEDICAL CENTER", "AL"),
    ("670340", "METHODIST CELINA MEDICAL CENTER", "TX")
]

columns = ["facility_id", "facility_name", "state"]

df = spark.createDataFrame(data, columns)

df.show()

spark.stop()