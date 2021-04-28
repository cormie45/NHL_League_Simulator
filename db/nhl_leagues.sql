DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

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
    home_second_goals INT,
    home_third_goals INT,
    home_team_score INT,
    away_team_id INT REFERENCES teams(id),
    away_first_goals INT,
    away_second_goals INT,
    away_third_goals INT,
    away_team_score INT,
    winner VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    match_id SERIAL REFERENCES matches(id),
    player_id SERIAL REFERENCES players(id),
    period INT
);

-- );