-- Scripts that creates a table the enforces `id` field

-- Create table `id_not_null`
CREATE TABLE
	IF NOT EXISTS id_not_null(
		id INT DEFAULT 1,
		name VARCHAR(256)
		);
