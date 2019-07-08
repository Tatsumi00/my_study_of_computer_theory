#程序怎样运行
#使查找更快

#哈希函数
def make_hashtable(nbuckets):
    table=[]
    for a in range(0,nbuckets):
        table.append([])
    return table

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

#!!!
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

#!!!
def hashtable_lookup(htable,key):
    bucket=hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

#my answer
def hashtable_update(htable,key,value):
    if hashtable_lookup(htable,key)==None:
        hashtable_add(htable,key,value)
    else:
        hashtable_lookup(htable,key)=value
    return htable

"""
def hashtable_upadate(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0]==key:
        entry[1] =value
        return
    bucket.append([key,value])
"""