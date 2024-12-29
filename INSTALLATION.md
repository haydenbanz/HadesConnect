# Installation Guide

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Database Configuration](#database-configuration)
- [Running the PHP Server](#running-the-php-server)
- [Using the Application](#using-the-application)

## Introduction
This guide will walk you through the steps to set up a PHP server, configure the database, and run the necessary PHP scripts (`create_db.php`, `upload.php`, and `view.php`) to upload and view data.

## Prerequisites
Before you begin, ensure you have the following installed:
- PHP (version 7.0 or higher)
- MySQL or MariaDB
- Web server (e.g., Apache, Nginx)

## Installation Steps

1. **Download the Project Files**
   Download the project files and ensure you have the following PHP scripts:
   - `create_db.php`
   - `upload.php`
   - `view.php`

2. **Place Files in the Web Server Directory**
   Move the downloaded PHP files to your web server's root directory. For example, in Apache, this is typically `/var/www/html`.

3. **Edit Database Configuration**
   Open each PHP file (`create_db.php`, `upload.php`, `view.php`) and enter your database details:
   - Database name
   - Server name
   - Username
   - Password

   Example:
   ```php
   // Database configuration
   $servername = "your_server_name";
   $username = "your_username";
   $password = "your_password";
   $dbname = "your_database_name";


# Deploying to a VPS

## Upload Files to VPS

Use an FTP client or SCP to upload the PHP files (`create_db.php`, `upload.php`, `view.php`) to your VPS's web server directory (e.g., `/var/www/html`).

## Configure Web Server

Ensure your web server (e.g., Apache, Nginx) is configured to serve the PHP files. Restart the web server if necessary.

## Access the Application

Open your web browser and navigate to your VPS's IP address or domain name, followed by the PHP script name (e.g., `http://your_vps_ip/upload.php`).

That's it! You have successfully set up a PHP server, configured your database, and run the necessary scripts to upload and view data.

# HadesConnect

## Table of Contents
- [🛠️ Prerequisites](#️-prerequisites)
- [Getting Discord Token and Spotify Client Secret](#getting-discord-token-and-spotify-client-secret)
  - [Discord Token](#discord-token)
  - [Spotify Client Secret](#spotify-client-secret)
- [Installation Instructions](#installation-instructions)
  - [Download EXE and Environment](#download-exe-and-environment)
  - [Clone or Download the Repository](#clone-or-download-the-repository)
  - [Navigate to the Directory](#navigate-to-the-directory)
  - [Install Required Python Packages](#install-required-python-packages)
  - [Modify `bot.py` Configuration](#modify-botpy-configuration)
  - [Start HadesConnect](#start-hadesconnect)
  - [Check Discord Server](#check-discord-server)
- [Compile to Executable (Optional)](#compile-to-executable-optional)
  - [Install PyInstaller](#install-pyinstaller)
  - [Install PyWin32 (if not installed)](#install-pywin32-if-not-installed)
  - [Compile to Executable](#compile-to-executable)
- [🔧 Configuration](#-configuration)

## 🛠️ Prerequisites

- [![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&color=%230078D6&labelColor=%23e3e3e3&style=for-the-badge&logo=python)](https://www.python.org/downloads/)
- [![Discord.py library](https://img.shields.io/static/v1?label=Discord.py&message=Library&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://pypi.org/project/discord.py/)
- Other required Python packages listed in `requirements.txt`

## Getting Discord Token and Spotify Client Secret

### Discord Token

1. **Create a Discord Application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on **New Application** and give your application a name.
   - Navigate to the **Bot** tab on the left sidebar.
   - Click **Add Bot** and confirm.
   - Under the **Token** section, click **Copy** to get your bot token.

2. **Keep Your Token Secure**:
   - Treat your token like a password. Do not share it publicly or commit it to version control.

### Spotify Client Secret

1. **Create a Spotify Application**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Log in or sign up for a Spotify Developer account.
   - Click on **Create an App** and fill out the necessary details for your application.

2. **Retrieve Client ID and Client Secret**:
   - Once your application is created, you'll see your **Client ID** displayed.
   - Click on **Show Client Secret** to reveal and copy your **Client Secret**.

3. **Keep Your Client Secret Secure**:
   - Treat your Client Secret like a password. Do not share it publicly or commit it to version control.

4. **Use Tokens and Secrets in Your Application**:
   - Store your Discord Token and Spotify Client Secret securely in environment variables or a configuration file (e.g., `.env` file) not included in your code repository.

5. **References**:
   - [Discord Developer Portal](https://discord.com/developers/applications)
   - [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)

# HadesConnect

## Installation Instructions

### Download EXE and Environment

[![GitHub Download](https://img.shields.io/static/v1?label=Download&message=HadesConnect&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/releases/tag/HadesConnect_win)

<BR>

**OR**<BR>

1. **Clone or Download the Repository**:
   - Clone the repository using Git:
     ```bash
     git clone https://github.com/haydenbanz/HadesConnect.git
     ```
   - Alternatively, download the repository from [HadesConnect download](https://github.com/haydenbanz/HadesConnect/archive/refs/heads/main.zip).

2. **Navigate to the Directory**:
   - Open a terminal or command prompt.
   - Change directory to HadesConnect:
     ```bash
     cd HadesConnect
     ```

3. **Install Required Python Packages**:
   - Install the necessary packages using pip:
     ```bash
     pip install -r requirements.txt
     ```

4. **Modify `bot.py` Configuration**:
   - Open `bot.py` file in a text editor.
   - Add your Discord bot token, Spotify client ID, Spotify client secret:
     - Discord bot token: Update on line 1182.
     - Spotify client ID and client secret: Update on lines 74 & 75.
     - Channel ID for voice (if applicable): Update on line 520.

5. **Start HadesConnect**:
   - Launch HadesConnect by running:
     ```bash
     python bot.py
     ```

6. **Check Discord Server**:
   - Verify that the bot appears and functions correctly on your Discord server for remote access.

## Compile to Executable (Optional)

1. **Install PyInstaller**:
   - Install PyInstaller using pip:
     ```bash
     pip install pyinstaller
     ```

2. **Install PyWin32 (if not installed)**:
   - Install PyWin32 using pip:
     ```bash
     pip install pywin32
     ```

3. **Compile to Executable**:
   - Navigate to your project directory in the terminal or command prompt.
   - Run one of the following commands:
     - For Windows:
       ```bash
       pyinstaller --onefile --add-data "*.py;." bot.py
       ```
       or
       ```bash
       pyinstaller --onefile --exclude-module pythoncom bot.py
       ```
   - This will create a standalone executable file in the `dist` directory.

## 🔧 Configuration

-  Configure the bot by editing the `bot.py` file.
-   Replace with your Discord token by changing `text_channel_id =   # Replace with your desired text channel ID`.
-  Replace with your Discord token `bot.run('YOUR_TOKEN')`.


## Configure Web Server

Ensure your web server (e.g., Apache, Nginx) is configured to serve the PHP files. Restart the web server if necessary.

## Access the Application

Open your web browser and navigate to your VPS's IP address or domain name, followed by the PHP script name (e.g., `http://your_vps_ip/upload.php`).

That's it! You have successfully set up a PHP server, configured your database, and run the necessary scripts to upload and view data.
