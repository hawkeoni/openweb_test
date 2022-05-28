CREATE TABLE TWITTER_DATA(
    TWEET_ID TEXT PRIMARY KEY NOT NULL,
    USERNAME TEXT NOT NULL,
    COUNTRY TEXT NOT NULL,
    TEXT TEXT NOT NULL,
    TIME INT NOT NULL,
    VERIFIED BOOLEAN NOT NULL,
    FOLLOWERS INT NOT NULL,
    TRUE_LABEL INT
);