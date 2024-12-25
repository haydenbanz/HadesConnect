<?php
$servername = "SERVER_ADDR";
$username = "YOUR_USERNAME";
$password = "YOUR_PASSWORD";
$dbname = "DB_NAME";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create database
$sql = "CREATE DATABASE IF NOT EXISTS $dbname";  // Corrected SQL syntax
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully\n";
} else {
    echo "Error creating database: " . $conn->error;
}

// Select the database
$conn->select_db($dbname);

// Create table
$sql = "CREATE TABLE IF NOT EXISTS system_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bot_name VARCHAR(255),
    system_name VARCHAR(255),
    public_ip VARCHAR(45),
    system_ip VARCHAR(45),
    status VARCHAR(50),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if ($conn->query($sql) === TRUE) {
    echo "Table created successfully\n";
} else {
    echo "Error creating table: " . $conn->error;
}

// Close connection
$conn->close();
?>
