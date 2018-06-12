import psycopg2


conn = psycopg2.connect("host=localhost dbname=jobstreet user=postgres password=rooney723")

cur = conn.cursor()
cur.execute("""
CREATE TABLE candidate_info
(
    global_candidate_id bigint,
    candidate_id bigint,
    server_id integer,
    account_id bigint,
    login_id character varying(250) COLLATE pg_catalog."default",
    password character varying(250) COLLATE pg_catalog."default",
    password_version_code integer,
    account_status_code integer,
    first_name character varying(250) COLLATE pg_catalog."default",
    last_name character varying(250) COLLATE pg_catalog."default",
    country_code integer,
    email character varying(250) COLLATE pg_catalog."default",
    email_status_code integer,
    last_update timestamp without time zone,
    create_date timestamp without time zone,
    candidate_personal_id bigint,
    birth_date timestamp without time zone,
    marital_status_code integer,
    race_code integer,
    religion_code integer,
    alt_email character varying(250) COLLATE pg_catalog."default",
    alt_email_status_code integer,
    identification_type_code integer,
    identification_no character varying(100) COLLATE pg_catalog."default",
    nationality_code integer,
    permanent_residence_csv character varying(250) COLLATE pg_catalog."default",
    work_authorization_csv character varying(250) COLLATE pg_catalog."default",
    state_code integer,
    state_other integer,
    city character varying(250) COLLATE pg_catalog."default",
    location_code integer,
    country_code1 integer,
    postcode character varying(250) COLLATE pg_catalog."default",
    address1 character varying(250) COLLATE pg_catalog."default",
    address2 character varying(250) COLLATE pg_catalog."default",
    tel_country_code integer,
    tel_area_code integer,
    tel_no character varying(250) COLLATE pg_catalog."default",
    handphone_country_code integer,
    handphone_no character varying(250) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.candidate_info
    OWNER to postgres;
""")
conn.commit()