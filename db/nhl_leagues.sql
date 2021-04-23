DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS players;
-- DROP TABLE IF EXISTS leagues;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    coach VARCHAR(255),
    stadium VARCHAR(255)
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id),
    age INT,
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

DELETE FROM teams;
DELETE FROM matches;

INSERT INTO teams (name, coach, stadium) VALUES ('Colorado Avalanche', 'Jared Bednar', 'Pepsi Center');
INSERT INTO teams (name, coach, stadium) VALUES ('Anahiem Ducks', 'Dallas Eakins', 'Honda Center');
INSERT INTO teams (name, coach, stadium) VALUES ('St. Louis Blues', 'Craig Berube', 'Enterprise Center');

INSERT INTO matches (date, home_team, home_team_score, away_team, away_team_score, winner) VALUES ('23/04/2021', 1, 4, 2, 0, 'Colorado Avalance');
INSERT INTO matches (date, home_team, home_team_score, away_team, away_team_score, winner) VALUES ('23/04/2021', 1, 4, 3, 0, 'Colorado Avalance');
INSERT INTO matches (date, home_team, home_team_score, away_team, away_team_score, winner) VALUES ('23/04/2021', 2, 3, 3, 2, 'Anahiem Ducks');
