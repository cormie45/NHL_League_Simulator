DROP TABLE IF EXISTS team_results;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
-- DROP TABLE IF EXISTS leagues;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY;
    name VARCHAR(255);
    coach VARCHAR(255);
    city VARCHAR(255)
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY;
    team_id INT REFERENCES teams(id);
    age INT;
    position VARCHAR(255);
    points INT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY;
    date VARCHAR(255);
    team_a_score INT;
    team_b_score INT;
    winner VARCHAR(255)
);

-- CREATE TABLE leagues (

-- );

CREATE TABLE team_results (
    id SERIAL PRIMARY KEY;
    matches_id SERIAL REFERENCES matches(id);
    team_a INT REFERENCES teams(id);
    team_b INT REFERENCES teams(id)
);

