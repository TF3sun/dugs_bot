import discord
import os

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True


class game_fac:
    def __init__(self, name, game_id, role_id, chat_id) -> None:
        self.name = name
        self.game_id = game_id
        self.role_id = role_id
        self.chat_id = chat_id

lol = game_fac('롤', 401518684763586560, 1024580671294931014, 1024582103909797939)
pubg = game_fac('배그', 530196305138417685, 1024580768204324905, 1024625771152683098)
valo = game_fac('발로', 700136079562375258, 1024580813171462144, 1024625650407047229)
losta = game_fac('로아', 0, 1024581467755528253, 1024625930183913502)

cmd_list = ['.안녕', '.명령', '.게임', '.게임 참가']

async def cmd_test(message):
    await message.channel.send('작동중입니다')

async def cmd_hello(message):
    await message.channel.send('안녕하세요!')

async def cmd_cmd(message):
    await message.channel.send(cmd_list)

async def cmd_give_role(message, game):
    role = message.guild.get_role(game.role_id)
    if message.author.roles == role:
        None
    else:
        await message.author.add_roles(role)

async def cmd_game_join(message, game):
    v_chn = message.guild.get_channel(game.chat_id)
    if message.author.voice == None:
        await message.channel.send('아무 음성채널에 들어간 후 사용해주세요')
        return
    else:
        None
    await message.author.move_to(v_chn)

async def cmd_not_cmd(message):
    send_msg = '올바른 명령어가 아닙니다\n명령어 목록 /명령 '
    await message.channel.send(send_msg)

#자동화#
async def auto_give_role(after, game):
    role = after.guild.get_role(game.role_id)
    await after.add_roles(role)



class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('.'):
            msg = message.content.split()
            None
        else:
            return

        if msg[0] == '.test':
            await cmd_test(message)

        elif msg[0] == '.안녕':
            await cmd_hello(message)

        elif msg[0] == '.명령':
            await cmd_cmd(message)

        elif msg[0] == '.롤':
            game = lol
            await cmd_give_role(message, game)
            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    await cmd_game_join(message, game)
                else:
                    None

        elif msg[0] == '.배그':
            game = pubg
            await cmd_give_role(message, game)
            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    await cmd_game_join(message, game)
                else:
                    None

        elif msg[0] == '.발로':
            game = valo
            await cmd_give_role(message, game)
            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    await cmd_game_join(message, game)
                else:
                    None

        elif msg[0] == '.로아':
            game = losta
            await cmd_give_role(message, game)
            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    await cmd_game_join(message, game)
                else:
                    None
        else:   #not command message
            await cmd_not_cmd

    async def on_presence_update(self, before, after):
        test_channel = discord.Client.get_channel(client, 1027540413919277066)
        await test_channel.send(after.activity)
        if after.activity.name == 'League of Legends':
            game = lol
            await auto_give_role(after, game)
        elif after.activity.name == 'VALORANT':
            game = valo
            await auto_give_role(after, game)
        elif after.activity.name == 'Lost Ark':
            game = losta
            await auto_give_role(after, game)
        elif after.activity.name == 'PUBG: BATTLEGROUNDS':
            game = pubg
            await auto_give_role(after, game)
        else:
            None



client = MyClient(intents=intents)
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
