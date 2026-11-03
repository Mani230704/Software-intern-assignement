-- SQL example for machine failure monitoring
-- This script is intended to demonstrate the kind of feature checks and risk screening used in the project.

CREATE TABLE IF NOT EXISTS machine_status (
    machine_id INTEGER,
    machine_type TEXT,
    air_temp_k REAL,
    process_temp_k REAL,
    rotational_speed_rpm REAL,
    torque_nm REAL,
    tool_wear_min INTEGER,
    machine_failure INTEGER
);

INSERT INTO machine_status (machine_id, machine_type, air_temp_k, process_temp_k, rotational_speed_rpm, torque_nm, tool_wear_min, machine_failure) VALUES
(1, 'H', 298.6, 308.7, 1551, 42.5, 120, 0),
(2, 'M', 300.9, 311.2, 1420, 48.0, 180, 1),
(3, 'L', 301.8, 312.4, 1610, 55.7, 145, 0),
(4, 'H', 305.1, 315.0, 1280, 61.2, 220, 1),
(5, 'M', 299.2, 309.8, 1500, 44.0, 110, 0);

-- 1. Check class balance
SELECT machine_failure, COUNT(*) AS total_rows
FROM machine_status
GROUP BY machine_failure;

-- 2. Find risk-prone machines based on operating conditions
SELECT machine_id, machine_type, torque_nm, rotational_speed_rpm, tool_wear_min
FROM machine_status
WHERE torque_nm > 50 OR rotational_speed_rpm < 1400 OR tool_wear_min > 180
ORDER BY torque_nm DESC;

-- 3. View recent failure candidates
SELECT *
FROM machine_status
WHERE machine_failure = 1
ORDER BY machine_id;
