from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimplePipeline").getOrCreate()

# Read data
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Clean data
df_clean = df.dropna()

# Aggregate
df_summary = df_clean.groupBy("product").sum("amount")

# Show result
df_summary.show()



