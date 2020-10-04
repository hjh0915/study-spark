from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

def main():
    conf = SparkConf()
    conf.set("spark.cassandra.connection.host", "localhost")
    conf.set("spark.cassandra.auth.username", "cassandra")
    conf.set("spark.cassandra.auth.password", "cassandra")

    spark = SparkSession \
        .builder \
        .config(conf=conf) \
        .appName("计算cassandra数据") \
        .getOrCreate()

    df = spark.read \
            .format("org.apache.spark.sql.cassandra") \
            .options(table="brch_qry_dtl", keyspace="finance") \
            .load()

    df.createOrReplaceTempView("qry_dtl")
    
    sqlDF = spark.sql("""
        select rpt_sum, sum(amt) from qry_dtl 
        where tran_date='2019-11-27' and dr_cr_flag='2'
        group by rpt_sum
    """)

    sqlDF.show()

    spark.stop()

if __name__ == "__main__":
    main()