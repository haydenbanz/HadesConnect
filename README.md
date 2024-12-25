# HadesConnect 🌑 V 2.1


![HadesConnect Logo](https://github.com/haydenbanz/haydenbanz.github.io/blob/main/images/%20gitimage/hades23vfsd.png?raw=true)

[![Python - HadesConnect](https://img.shields.io/static/v1?label=Python&message=HadesConnect&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge&&logo=python)](https://github.com/haydenbanz/HadesConnect/tree/main)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=%233DA639&labelColor=%23e3e3e3&style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/blob/main/LICENSE)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&color=%230078D6&labelColor=%23e3e3e3&style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![Discord.py library](https://img.shields.io/static/v1?label=Discord.py&message=Library&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://pypi.org/project/discord.py/)
[![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/HadesConnect?style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/HadesConnect?style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/haydenbanz/HadesConnect?style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/stargazers)
![Profile Views](https://komarev.com/ghpvc/?username=haydenbanz&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)
[![GitHub Download](https://img.shields.io/static/v1?label=Download&message=HadesConnect&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/releases)

# HadesConnect: Emergency Switch & Remote Desktop Control via Discord

## 📖 Description

HadesConnect is a software solution designed to enable emergency switch activation and remote desktop control through Discord. It integrates seamlessly with Discord's platform, allowing users to manage emergency procedures and access remote desktops directly from their Discord server. Ideal for swift response teams and remote support scenarios, HadesConnect ensures efficient communication and action during critical situations.

## Key Features

- **Emergency Switch Activation:** Trigger emergency procedures instantly via Discord commands.
- **Remote Desktop Control:** Access and control remote desktops securely through Discord.
- **Real-time Communication:** Facilitate swift response and coordination with team members.
- **Customizable Settings:** Configure permissions and settings to suit specific operational needs.

## Updates

- 🐛 Fixed bugs:
  - Fixed issue with Spotify remote device control not starting on device boot.
  - Fixed issues with voice recording and streaming voice to Discord channel.
- 🚀 Added new features:
  - 🔥 Deactivate antivirus firewall.
  - 🖼️ Fixed screenshot and screen share.
  - 🎵 Spotify remote device control: Start, stop, and control Spotify playback remotely.
  - 🌐 Web and webhook-based control: Start a web server and utilize WebSocket (ws://) for real-time interactions.
  - 🔋 Get battery status: Monitor and display device battery status.
  - 🚨 Self-destruction of application: Implement a feature to self-destruct the application securely.
  - 📜 Clear logs: Provide functionality to clear application logs securely.
  - 🎤 Streaming Voice: Stream voice from voice channels.

## Feature List

- 🖥️ **/!streamscreen:** Sends the screenshot and sends.
- 💻 **/powershell:** Executes commands using PowerShell.
- 🤖 **/bot_commmand:** Executes a command related to a bot.
- 📝 **/sys_log:** Logs system activities.
- 🔒 **/lock_sys:** Locks the system.
- 📦 **/set_payload:** Sets a payload for execution.
- 📶 **/grab_wifi:** Grabs WiFi information.
- ⬇️ **/download:** Downloads a specified file.
- 🎥 **/cam_list:** Lists connected cameras.
- 🔄 **/list_process:** Lists running processes.
- ⛔ **/kill_process:** Terminates a specified process.
- 📡 **/rat_down:** Initiates a remote access tool download.
- 🔄 **/sys_restart:** Restarts the system.
- 🗑️ **/clear:** Clears the current operation.
- ### Voice Commands
- Use `!join` to make the bot join your current voice channel.
- Use `!voice_start` to start streaming audio from your microphone to the voice channel.
- Use `!voice_stop` to stop streaming.
- Use `!leave` to make the bot leave the voice channel.
- 🖥️ **/recscreen [duration]:** Records the screen. (Invalid duration. Please specify a valid number after '!recscreen')
- 🛡️ **/disableantivirus:** Disables antivirus protection.
- 🛡️ **/disablefirewall:** Disables firewall protection.
- 🌐 **/start_server:** Starts a server.
- 🌐 **/websocket_server:** Starts a WebSocket server.
- 🎵 **/now_playing:** Gets the current song playing in Spotify.
- ▶️ **/play [song]:** Plays a song in Spotify. (Example: /play faded)
- ⏸️ **/pause:** Pauses the current song in Spotify.
- ▶️ **/resume:** Resumes playback of the current song in Spotify.
- ⏭️ **/next:** Plays the next song in the Spotify playlist.
- ⏮️ **/previous:** Plays the previous song in the Spotify playlist.
- ❤️ **/like:** Likes the current song in Spotify.
- 🔋 **/battery:** Retrieves battery status.
- 🗑️ **/cleartracks:** Clears tracks and logs.
- 💣 **/self_destruct:** Initiates self-destruction.
- 📶 **/ping:** Sends a ping to check status.
- ℹ️ **/sys_info:** Retrieves system information.
- 🖥️ **/screen_share:** Shares the screen.
- 📝 **/start_logging:** Starts logging activities.
- 📸 **/camic [cam_id]:** Takes a shot with the default webcam or the specified webcam ID.

## ⚠️ Unauthorized Use Alert ⚠️

Unauthorized use of this software is strictly prohibited. This includes but is not limited to:

- Unauthorized access or control of systems.
- Use of commands without proper authorization.
- Any activity not explicitly permitted by the software's intended use.

Violations will be subject to legal action and may result in severe penalties.

Please ensure all usage complies with applicable laws and regulations.

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

## Commands

- **/!streamscreen:** Sends the screenshot and sends.
- **/powershell:** Executes commands using PowerShell.
- **/bot_command:** Executes a command related to a bot.
- **/sys_log:** Logs system activities.
- **/lock_sys:** Locks the system.
- **/set_payload:** Sets a payload for execution.
- **/grab_wifi:** Grabs WiFi information.
- **/download:** Downloads a specified file.
- **/cam_list:** Lists connected cameras.
- **/list_process:** Lists running processes.
- **/kill_process:** Terminates a specified process.
- **/rat_down:** Initiates a remote access tool download.
- **/sys_restart:** Restarts the system.
- **/clear:** Clears the current operation.
- **/voice_rec [duration]:** Initiates voice recognition. (Duration must be a positive integer.)
- **/recscreen [duration]:** Records the screen. (Invalid duration. Please specify a valid number after '!recscreen')
- **/disableantivirus:** Disables antivirus protection.
- **/disablefirewall:** Disables firewall protection.
- **/start_server:** Starts a server.
- **/websocket_server:** Starts a WebSocket server.
- **/now_playing:** Gets the current song playing in Spotify.
- **/play [song]:** Plays a song in Spotify. (Example: /play faded)
- **/pause:** Pauses the current song in Spotify.
- **/resume:** Resumes playback of the current song in Spotify.
- **/next:** Plays the next song in the Spotify playlist.
- **/previous:** Plays the previous song in the Spotify playlist.
- **/like:** Likes the current song in Spotify.
- **/battery:** Retrieves battery status.
- **/cleartracks:** Clears tracks and logs.
- **/self_destruct:** Initiates self-destruction.
- **/ping:** Sends a ping to check status.
- **/sys_info:** Retrieves system information.
- **/screen_share:** Shares the screen.
- **/start_logging:** Starts logging activities.
- **/camic [cam_id]:** Takes a shot with the default webcam or the specified webcam ID.

## Contribution

We welcome contributions to HadesConnect! If you have suggestions for improvements, found a bug, or have a new feature request, feel free to contribute.

- [![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/HadesConnect?style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/issues)
- [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/HadesConnect?style=for-the-badge)](https://github.com/haydenbanz/HadesConnect/pulls)

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page to create your own copy of the repository.

2. **Clone Your Fork**: Clone your forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/your-username/HadesConnect.git
    ```

3. **Create a New Branch**: Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Make your changes or add your new feature.

5. **Commit Your Changes**: Commit your changes with a clear and concise commit message:
    ```bash
    git commit -m "Description of the changes"
    ```

6. **Push to Your Fork**: Push your changes to your forked repository:
    ```bash
    git push origin feature-or-bugfix-name
    ```

7. **Submit a Pull Request**: Go to the original repository and submit a pull request from your forked repository. Provide a detailed description of your changes in the pull request.

### Guidelines

- Follow the existing code style.
- Write clear and concise commit messages.
- Test your changes thoroughly before submitting a pull request.
- Ensure that your changes do not introduce new bugs or break existing functionality.
- Be respectful and open to feedback during the code review process.

Thank you for contributing to HadesConnect!

## 🌐 Support

[![Discord](https://img.shields.io/badge/Discord-CODE%20GLITCH%20Bot%20DISCORD%20SERVER%20NAME-%237289DA?style=for-the-badge&logo=discord)](https://discord.gg/ZFTCpAU53U)

Join our Discord server (Update Soon) for support, discussions, and updates related to DiscordGloom.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

**Unauthorized use is strictly prohibited.**

📧 Email: cubedimension@protonmail.com  



### Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haydenbanz">](https://github.com/haydenbanz)  
[<img src="https://avatars.githubusercontent.com/u/116929670?s=64&v=4" width="64" height="64" alt="AldrinCode">](https://github.com/AldrinCode)  
[<img src="https://avatars.githubusercontent.com/u/108749445?s=64&v=4" width="64" height="64" alt="0x_varadacode">](https://github.com/0x_varadacode)  
[<img src="https://avatars.githubusercontent.com/u/144106684?s=64&v=4" width="64" height="64" alt="Glitchesminds">](https://github.com/Glitchesminds)

## ☕ Support

If you find this project helpful, consider buying us a coffee with cookies:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/codeglitch)

## 🚫 Disclaimer

The creators of this project are not responsible
