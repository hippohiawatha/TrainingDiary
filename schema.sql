--Backup given by pgadmin 4

CREATE TABLE benchsets (
    weight numeric,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);

ALTER TABLE benchsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME benchsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);

CREATE TABLE deadliftsets (
    weight integer,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);


ALTER TABLE deadliftsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME deadliftsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);


CREATE TABLE maxlifts (
    "Bench" integer,
    "Squat" integer,
    "Deadlift" integer,
    "UserID" integer NOT NULL
);

CREATE TABLE squatsets (
    weight integer,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);

ALTER TABLE squatsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME squatsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);

CREATE TABLE users (
    id integer NOT NULL,
    username text,
    password text
);

CREATE SEQUENCE users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE users_id_seq OWNED BY users.id;

CREATE TABLE userworkouts (
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);

ALTER TABLE userworkouts ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME userworkouts_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);

ALTER TABLE ONLY benchsets
    ADD CONSTRAINT benchsets_pkey PRIMARY KEY (db_id);

ALTER TABLE ONLY userworkouts
    ADD CONSTRAINT db_id PRIMARY KEY (db_id);

ALTER TABLE ONLY deadliftsets
    ADD CONSTRAINT deadliftsets_pkey PRIMARY KEY (db_id);

ALTER TABLE ONLY squatsets
    ADD CONSTRAINT squatsets_pkey PRIMARY KEY (db_id);

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);

ALTER TABLE ONLY users
    ADD CONSTRAINT users_uniquename UNIQUE (username);

ALTER TABLE ONLY deadliftsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY benchsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;

ALTER TABLE ONLY squatsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;

ALTER TABLE ONLY userworkouts
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;