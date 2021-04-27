DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

-- DROP TABLE IF EXISTS leagues;

CREATE TABLE teams (
    name VARCHAR(255),
    coach VARCHAR(255),
    stadium VARCHAR(255),
    city VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE players (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    team_id INT REFERENCES teams(id),
    position VARCHAR(255),
    points INT,
    id SERIAL PRIMARY KEY
);

CREATE TABLE matches (
    home_team INT REFERENCES teams(id),
    home_first_goals INT,
    home_first_scorers SET,
    home_second_goals INT,
    home_second_scorers SET,
    home_third_goals INT,
    home_third_scorers SET,
    home_team_score INT,
    away_team INT REFERENCES teams(id),
    away_first_goals INT,
    away_first_scorers SET,
    away_second_goals INT,
    away_second_scorers SET,
    away_third_goals INT,
    away_third_scorers SET,
    away_team_score INT,
    winner VARCHAR(255),
    id SERIAL PRIMARY KEY
);

-- CREATE TABLE leagues (

-- );