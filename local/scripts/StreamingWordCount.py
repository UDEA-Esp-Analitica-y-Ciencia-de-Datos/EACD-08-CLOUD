from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(appName = "Text Cleaning")
strc = StreamingContext(sc, 10)

text_data = strc.socketTextStream("34.238.252.238", 8083)

words = text_data.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint()

strc.start()
strc.awaitTermination()