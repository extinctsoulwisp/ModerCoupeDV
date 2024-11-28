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
	one_c_id VARCHAR NULL,
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

CREATE TABLE profile_color_1c (
	profile_id INTEGER NOT NULL,
	color_id INTEGER NOT NULL,
	top_guide_2 VARCHAR,
	bottom_guide_2 VARCHAR,
	top_guide_1 VARCHAR,
	bottom_guide_1 VARCHAR,
	top_movable_guide VARCHAR,
	decorative_guide VARCHAR,
	plug VARCHAR,
	top_horizontal VARCHAR,
	bottom_horizontal VARCHAR,
	vertical VARCHAR,
	sealant VARCHAR,
	shlegel VARCHAR,
	wheels VARCHAR,
	PRIMARY KEY (profile_id, color_id),
	FOREIGN KEY(profile_id) REFERENCES profile (id),
	FOREIGN KEY(color_id) REFERENCES color (id)
);