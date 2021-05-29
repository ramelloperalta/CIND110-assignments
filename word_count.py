# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:23:38 2021

@author: Ramello
"""

from pyspark import SparkConf, SparkContext
def main(sc):
    text = 'an apple is an apple and an orange is an orange'
    list_of_words = text.split()
    words_rdd = sc.parallelize(list_of_words)
    words_kv_rdd = words_rdd.map(lambda word: (word, 1))
    word_count_rdd = words_kv_rdd.reduceByKey(lambda acum, count: acum+count)
    word_count = word_count_rdd.collect()
    print(word_count)
if __name__ == "__main__":
    conf = SparkConf().setAppName("WordCounter")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()
