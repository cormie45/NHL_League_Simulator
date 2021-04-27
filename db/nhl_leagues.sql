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
    home_team_id INT REFERENCES teams(id),
    home_first_goals INT,
    str_home_first_scorers VARCHAR(255),
    home_second_goals INT,
    str_home_second_scorers VARCHAR(255),
    home_third_goals INT,
    str_home_third_scorers VARCHAR(255),
    home_team_score INT,
    away_team_id INT REFERENCES teams(id),
    away_first_goals INT,
    str_away_first_scorers VARCHAR(255),
    away_second_goals INT,
    str_away_second_scorers VARCHAR(255),
    away_third_goals INT,
    str_away_third_scorers VARCHAR(255),
    away_team_score INT,
    winner VARCHAR(255),
    id SERIAL PRIMARY KEY
);

-- CREATE TABLE leagues (

-- );