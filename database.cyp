CREATE (Fernando:Person {name:'Fernando Jackson', age: 14 })
CREATE (Pete:Person {name:'Pete Morrison', age: 24 })
CREATE (Mario:Person {name:'Mario Kennedy', age: 17 })
CREATE (Bethany:Person {name:'Bethany Hamilton', age: 21 })
CREATE (Alicia:Person {name:'Andy Synthesis', age: 18 })
CREATE (Michelle:Person {name:'Michelle Cobain', age: 24 })

CREATE (Computer:System {title:'Laptop Gaming', year: 2003, brand:'Razer' })
CREATE (Console:System {title:'PS4', year: 2013, brand:'Sony' })
CREATE (Smartphone:System {title:'Iphone X', year: 2017, brand:'Apple' })

CREATE (Action:Genre{title:"Action" })
CREATE (Strategy:Genre{title:"Strategy" })
CREATE (Shooter:Genre{title:"Shooter" })
CREATE (Platform:Genre{title:"Platform" })

CREATE (Warcraft:Game{title:"Warcarft", company: "Blizzard" })
CREATE (Uncharted:Game{title:"Uncharted 4", company: "Naughty Dog" })
CREATE (Halo:Game{title:"Halo 5", company: "343 Industries" })
CREATE (Supermario:Game{title:" Super Mario Odyssey", company: "Nintendo "})


CREATE
	(Fernando)-[:PLAYS_WITH]->(Computer),
	(Fernando)-[:LIKES]->(Action),
	(Alicia)-[:PLAYS_WITH]->(Computer),
	(Alicia)-[:LIKES]->(Strategy),
	(Alicia)-[:LIKES]->(Action),
	(Mario)-[:PLAYS_WITH]->(Console),
	(Mario)-[:LIKES]->(Shooter),
	(Pete)-[:PLAYS_WITH]->(Console),
	(Pete)-[:LIKES]->(Strategy),
	(Pete)-[:LIKES]->(Action),
	(Michelle)-[:PLAYS_WITH]->(Smartphone),
	(Michelle)-[:LIKES]->(Platform),
	(Bethany)-[:PLAYS_WITH]->(Console),
	(Bethany)-[:LIKES]->(Shooter),
	(Action)-[:RECOMMENDATION]->(Halo),
	(Action)-[:RECOMMENDATION]->(Uncharted),
	(Action)-[:RECOMMENDATION]->(Warcraft),
	(Strategy)-[:RECOMMENDATION]->(Warcraft),
	(Shooter)-[:RECOMMENDATION]->(Halo),
	(Platform)-[:RECOMMENDATION]->(Supermario)
