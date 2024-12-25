<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection parameters
$servername = "your_server"; // Update with your server name
$username = "your_username"; // Update with your database username
$password = "your_password"; // Update with your database password
$dbname = "your_dbname";     // Update with your database name

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die(json_encode(['message' => "Connection failed: " . $conn->connect_error]));
}

// Check for the 'auth' parameter in the URL
$auth_code = isset($_GET['auth']) ? $_GET['auth'] : '';

// Define your authentication code
define('AUTH_CODE', 'ENTER_AUTH_CODE'); // Ensure this matches the code you want to use for authentication

// Verify the authentication code
if ($auth_code !== AUTH_CODE) {
    echo json_encode(['message' => 'Unauthorized access']);
    exit;
}

// SQL query to retrieve data from the database
$sql = "SELECT bot_name, system_name, public_ip, system_ip, status, date FROM system_info";
$result = $conn->query($sql);

// Check if there are results
if ($result->num_rows > 0) {
    // Fetch all rows and return as a JSON array
    $data = [];
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    echo json_encode(['data' => $data]);
} else {
    echo json_encode(['message' => 'No data found']);
}

// Close the connection
$conn->close();
?>

