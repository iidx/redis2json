# -*- coding: utf-8 -*-
import redis, json

def redis2json(save_to):

	server_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
	rdb = redis.Redis(connection_pool=server_pool)

	jlist = []
	keys  = rdb.keys()

	for key in keys:
		jdict = {}
		jdict['key'] = key
		jdict['value'] = int(rdb.get(key))
		jlist.append(jdict)

	f = open(save_to, "wb")
	f.write(str(json.dumps(jlist)))
	f.close()