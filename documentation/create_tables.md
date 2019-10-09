```
CREATE TABLE account (
	id SERIAL NOT NULL, 
	date_created TIMESTAMP WITHOUT TIME ZONE, 
	date_modified TIMESTAMP WITHOUT TIME ZONE, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE category (
	id SERIAL NOT NULL, 
	date_created TIMESTAMP WITHOUT TIME ZONE, 
	date_modified TIMESTAMP WITHOUT TIME ZONE, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE task (
	id SERIAL NOT NULL, 
	date_created TIMESTAMP WITHOUT TIME ZONE, 
	date_modified TIMESTAMP WITHOUT TIME ZONE, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144), 
	deadline TIMESTAMP WITHOUT TIME ZONE, 
	possible_after TIMESTAMP WITHOUT TIME ZONE, 
	done BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	category_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
)
```