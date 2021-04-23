DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS players;
-- DROP TABLE IF EXISTS leagues;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    coach VARCHAR(255),
    stadium VARCHAR(255),
    city VARCHAR(255)
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    team_id INT REFERENCES teams(id),
    position VARCHAR(255),
    points INT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    home_team INT REFERENCES teams(id),
    home_team_score INT,
    away_team INT REFERENCES teams(id),
    away_team_score INT,
    winner VARCHAR(255)
);

-- CREATE TABLE leagues (

-- );