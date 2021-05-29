# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:02:50 2021

@author: Ramello
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main(sparkSession):
    schema = "InvoiceNo string, StockCode string, Description string, Quantity int, "+\
    "InvoiceDate date, UnitPrice float, CustomerID int, Country string"

    #Read
    df_online = sparkSession.read.schema(schema)\
        .format("csv")\
            .option("header","true").load("/home/cu/data/online_retail/*.csv")

    #Query
    df_country_sales = df_online\
        .selectExpr("Country","(UnitPrice*Quantity) as Amount", "InvoiceDate")\
            .groupBy(window(col("InvoiceDate"),"1 day"), col("Country"))\
                .sum("Amount")\
                    .withColumnRenamed("sum(Amount)","DailySales")
    df_country_sales.show()


if __name__ == "__main__":
    sparkSession = SparkSession\
        .builder\
            .appName("Daily Sales Data")\
                .getOrCreate()
    main(sparkSession)
    sc.stop()
