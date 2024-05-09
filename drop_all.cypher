MATCH (n)
DETACH DELETE n

   CALL db.indexes()
   YIELD name
   CALL db.index.fulltext.drop(name)
   RETURN count(*)
   
   CALL db.constraints()
   YIELD name
   CALL db.constraints.drop(name)
   RETURN count(*)