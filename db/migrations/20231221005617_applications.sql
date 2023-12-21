-- migrate:up
CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    uw_name VARCHAR(255) NOT NULL,
    premium FLOAT NOT NULL,
    state VARCHAR(10) NOT NULL,
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    sic VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    deal_stage VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN NOT NULL DEFAULT TRUE
);

-- migrate:down
DROP TABLE applications;
