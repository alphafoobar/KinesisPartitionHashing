# Kinesis PartitionKey Hashing

What is a [partition key all about](https://stackoverflow.com/questions/48399903/what-is-partition-key-in-aws-kinesis-all-about)?

The code in this repository comes from this excellent blog: https://willhaley.com/blog/key-space-partitioning/

The PartitionKey used when a producer puts/publishes to Kinesis is hashed like so int128(md5sum(<PartitionKey>)). That derived hash of the PartitionKey will determine where data 
lands on the stream. So if we shard (split) the stream into multiple even segments, the hashed key we generate determines which shard data will land on.

    Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash 
    function is used to map partition keys to 128-bit integer values and to map associated data records to shards

A simple python script based on that description and a [couple](https://stackoverflow.com/questions/44593533/how-to-use-explicithashkey-for-round-robin-stream-assignment-in-aws-kinesis) 
[other](https://github.com/mhart/kinesalite/blob/master/db/index.js) sources illustrates how a predictable incremental integer PartitionKey value will result in a distinct skew for 
a relatively small set set of keys.

The minimum hash key in Kinesis is 0 and the max is 340282366920938463463374607431768211455.

For a stream with two shards, any data with a hash key < 170141183460469231731687303715884105728 (half the key space) will be in shard one. Anything greater will be in shard two. 
See here that with two shards being used to distribute keys for 14 unique inputs all but three will end up in shard two.