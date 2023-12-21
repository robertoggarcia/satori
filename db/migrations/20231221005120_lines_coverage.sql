-- migrate:up
CREATE TABLE lines_coverage (
    lines_coverage_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN NOT NULL DEFAULT TRUE
);

-- migrate:down
DROP TABLE lines_coverage;