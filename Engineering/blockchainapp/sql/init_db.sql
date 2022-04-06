CREATE TABLE IF NOT EXISTS accounts_list (
    id serial not null,
    address varchar, 
    staked_balance float, 
    block varchar, 
    dc_balance float, 
    nonce float, 
    dc_nonce float, 
    balance float,
    PRIMARY KEY(id),
    UNIQUE(address)
);


CREATE TABLE IF NOT EXISTS rewards_charts (
    id serial not null,
    min_time timestamp,
    max_time timestamp,
    total float,
    sum_amt float, 
    stddev float, 
    min_amt float, 
    median float, 
    max_amt float, 
    avg_amt float,
    created_date timestamp default now()
);

INSERT INTO rewards_charts (
    min_time, max_time, sum_amt, stddev, min_amt, median, max_amt, avg_amt, created_date 
)
VALUES (NOW(), NOW(), 1, 1, 1, 1, 1, 1, NOW());


INSERT INTO rewards_charts (
    min_time, max_time, sum_amt, stddev, min_amt, median, max_amt, avg_amt, created_date 
)
VALUES (NOW(), NOW(), 2, 3, 3, 1, 6, 8, NOW());