from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    sc = SparkContext(conf = SparkConf().setMaster("local"))
    Input = sc.textFile("turned_to_text.txt")
    words = Input.flatMap(lambda x: [i[0] for i in x.split()])
    d = words.countByValue()
    for i in range(1536, 1791):
        try:
            if d[chr(i)]:
                print(chr(i), ' : ', d[chr(i)])
        except:
            pass
