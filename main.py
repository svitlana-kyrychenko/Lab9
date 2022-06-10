from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName('SimpleSparkProject').getOrCreate()
    df = spark.read.format("csv").load("./data/PS_20174392719_1491204439457_log.csv")
    df.printSchema()
    num_rows = df.count()
    print(f'Number of rows: {num_rows}\n')

if __name__ == '__main__':
    main()