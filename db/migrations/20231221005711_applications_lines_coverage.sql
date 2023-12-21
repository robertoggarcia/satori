-- migrate:up
CREATE TABLE application_lines_coverage (
    application_id INT,
    lines_coverage_id INT,
    PRIMARY KEY (application_id, lines_coverage_id),
    FOREIGN KEY (application_id) REFERENCES applications(application_id),
    FOREIGN KEY (lines_coverage_id) REFERENCES lines_coverage(lines_coverage_id)
);

-- migrate:down

