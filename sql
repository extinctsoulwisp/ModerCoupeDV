CREATE TABLE rigel_color (
	rigel_id INTEGER NOT NULL,
	color_id INTEGER NOT NULL,
	PRIMARY KEY (rigel_id, color_id),
	FOREIGN KEY(rigel_id) REFERENCES rigel (id),
	FOREIGN KEY(color_id) REFERENCES color (id)
);

CREATE TABLE rigel_color_1c (
	rigel_id INTEGER NOT NULL,
	color_id INTEGER NOT NULL,
	one_c_id VARCHAR NOT NULL,
	PRIMARY KEY (rigel_id, color_id),
	FOREIGN KEY(rigel_id) REFERENCES rigel (id),
	FOREIGN KEY(color_id) REFERENCES color (id)
);

CREATE TABLE profile_color (
	id SERIAL NOT NULL,
	profile_id INTEGER,
	color_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(profile_id) REFERENCES profile (id),
	FOREIGN KEY(color_id) REFERENCES rigel (id)
);

