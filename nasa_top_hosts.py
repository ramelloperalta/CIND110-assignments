# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:32:02 2021

@author: Ramello
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

def main(sparkSession):
    df_nasa_data = sparkSession.read.format('csv')\
        .option('delimiter',',')\
            .option('quote','')\
                .option('header','true')\
                    .schema('host string, method string, status integer, bytes integer')\
                        .load('/home/cu/data/nasa_data.csv')
    df_top_10_hosts = df_nasa_data.groupBy('host')\
        .avg('bytes')\
            .withColumnRenamed('avg(bytes)','avgBytes')\
                .sort(desc('avgBytes'))\
                    .limit(10)
    df_top_10_hosts.show()

if __name__ == '__main__':
    sparkSession = SparkSession\
        .builder\
            .appName('NASA top hosts')\
                .getOrCreate()
    main(sparkSession)
    sc.stop()
                    

