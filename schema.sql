--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2022-02-02 15:26:55

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 212 (class 1259 OID 16441)
-- Name: benchsets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.benchsets (
    weight numeric,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);


ALTER TABLE public.benchsets OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16469)
-- Name: benchsets_db_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.benchsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.benchsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);


--
-- TOC entry 219 (class 1259 OID 16506)
-- Name: deadliftsets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deadliftsets (
    weight integer,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);


ALTER TABLE public.deadliftsets OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16505)
-- Name: deadliftsets_db_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.deadliftsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.deadliftsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);


--
-- TOC entry 209 (class 1259 OID 16420)
-- Name: maxlifts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maxlifts (
    "Bench" integer,
    "Squat" integer,
    "Deadlift" integer,
    "UserID" integer NOT NULL
);


ALTER TABLE public.maxlifts OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16499)
-- Name: squatsets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.squatsets (
    weight integer,
    sets integer,
    reps integer,
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);


ALTER TABLE public.squatsets OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16498)
-- Name: squatsets_db_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.squatsets ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.squatsets_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 16426)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text,
    password text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16425)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 210
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 213 (class 1259 OID 16451)
-- Name: userworkouts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userworkouts (
    workout_id integer NOT NULL,
    user_id integer NOT NULL,
    db_id integer NOT NULL
);


ALTER TABLE public.userworkouts OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16477)
-- Name: userworkouts_db_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.userworkouts ALTER COLUMN db_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.userworkouts_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 10000
    CACHE 1
);


--
-- TOC entry 3188 (class 2604 OID 16429)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3194 (class 2606 OID 16476)
-- Name: benchsets benchsets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.benchsets
    ADD CONSTRAINT benchsets_pkey PRIMARY KEY (db_id);


--
-- TOC entry 3196 (class 2606 OID 16482)
-- Name: userworkouts db_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userworkouts
    ADD CONSTRAINT db_id PRIMARY KEY (db_id);


--
-- TOC entry 3200 (class 2606 OID 16510)
-- Name: deadliftsets deadliftsets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deadliftsets
    ADD CONSTRAINT deadliftsets_pkey PRIMARY KEY (db_id);


--
-- TOC entry 3198 (class 2606 OID 16503)
-- Name: squatsets squatsets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.squatsets
    ADD CONSTRAINT squatsets_pkey PRIMARY KEY (db_id);


--
-- TOC entry 3190 (class 2606 OID 16433)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3192 (class 2606 OID 16435)
-- Name: users users_uniquename; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_uniquename UNIQUE (username);


--
-- TOC entry 3204 (class 2606 OID 16511)
-- Name: deadliftsets user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deadliftsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3201 (class 2606 OID 16516)
-- Name: benchsets user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.benchsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3203 (class 2606 OID 16521)
-- Name: squatsets user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.squatsets
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3202 (class 2606 OID 16526)
-- Name: userworkouts user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userworkouts
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id) NOT VALID;


-- Completed on 2022-02-02 15:26:55

--
-- PostgreSQL database dump complete
--

