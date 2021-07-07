# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**✨ Welcome [{}](tg://user?id={})!**\n\nZer0Byte 2.0 is a **project** designed for play music in your **group's voice Chat**, as simple as possible\n\n❓ **How to use it?/nSend /help Command To Get Every Possible Commands/n**"
      HELP_MSG = [
        ".",
f"""
**Hello 👋 This is Zer0Byte 2.0

>> Zer0Byte 2.0 can play music in your group's voice chat as well as channel voice chats

>> Add Assistant - @Zer0ByteAssistant2
""",

f"""
**Setting up Zer0Byte 2.0**
 >> **For Groups**

1. Make bot admin (Group and in channel if use cplay)
2. Start a voice chat
3. Try /play [song name] for the first time by an admin
4. If Zer0Byte Assistant joined enjoy music, If not add @Zer0ByteAssistant2 to your group and retry

**For Channel**
1. Make me admin of your channel 
2. Send /userbotjoinchannel in linked group
3. Now send commands in linked group
""",
f"""
**Commands**

**>> Commands For Groups**

• /play: Play the requestd song
• /play [yt url] : Play the given yt url
• /play [reply yo audio]: Play replied audio
• /dplay: Play song via deezer
• /splay: Play song via jio saavn
• /ytplay: Directly play song via Youtube Music

**>> Playback ⏯**

• /player: Open Settings menu of player
• /skip: Skips the current track
• /pause: Pause track
• /resume: Resumes the paused track
• /end: Stops media playback
• /current: Shows the current Playing track
• /playlist: Shows playlist

*Player **Command** and all other Commands except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**>> Commands For Channels**

>> For linked group admins only:

• /cplay [song name] - play song you requested
• /cdplay [song name] - play song you requested via deezer
• /csplay [song name] - play song you requested via jio saavn
• /cplaylist - Show now playing list
• /cccurrent - Show now playing
• /cplayer - open music player settings panel
• /cpause - pause song play
• /cresume - resume song play
• /cskip - play next song
• /cend - stop music play
• /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

>> If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @Zer0ByteAssistant2 to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**>> More tools**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @Zer0ByteAssistant2 Userbot to your chat
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**>> Commands for Sudo Users**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
