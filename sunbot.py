import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('/'):
            msg = message.content.split()
            None
        else:
            return

        #[게임id, 역할id, 음성채널id]
        lol = [356869127241072640,1024580671294931014,1024582103909797939]
        pubg = [0, 1024580768204324905, 1024625771152683098]
        valo = [0, 1024580813171462144, 1024625650407047229]
        losta = [0, 1024581467755528253, 1024625930183913502]


        if msg[0] == '/test':
            await message.channel.send('Im workong!')
        elif msg[0] == '/안녕':
            await message.channel.send('안녕하세요!')

        elif msg[0] == '/롤':
            game = lol
            role = message.guild.get_role(game[1])

            if message.author.roles == role:
                None
            else:
                await message.author.add_roles(role)

            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    v_chn = message.guild.get_channel(game[2])
                    if message.author.voice == None:
                        await message.channel.send('아무 음성채널에 들어간 후 사용해주세요')
                        return
                    else:
                        None
                    await message.author.move_to(v_chn)
                else:
                    None

        elif msg[0] == '/배그':
            game = pubg
            role = message.guild.get_role(game[1])

            if message.author.roles == role:
                None
            else:
                await message.author.add_roles(role)

            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    v_chn = message.guild.get_channel(game[2])
                    if message.author.voice == None:
                        await message.channel.send('아무 음성채널에 들어간 후 사용해주세요')
                        return
                    else:
                        None

                    await message.author.move_to(v_chn)
                else:
                    None

        elif msg[0] == '/발로':
            game = valo
            role = message.guild.get_role(game[1])

            if message.author.roles == role:
                None
            else:
                await message.author.add_roles(role)

            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    v_chn = message.guild.get_channel(game[2])
                    if message.author.voice == None:
                        await message.channel.send('아무 음성채널에 들어간 후 사용해주세요')
                        return
                    else:
                        None
                    await message.author.move_to(v_chn)
                else:
                    None

        elif msg[0] == '/로아':
            game = losta
            role = message.guild.get_role(game[1])

            if message.author.roles == role:
                None
            else:
                await message.author.add_roles(role)

            if len(msg) == 1:
                return
            else:
                if msg[1] == '참가':
                    v_chn = message.guild.get_channel(game[2])
                    if message.author.voice == None:
                        await message.channel.send('아무 음성채널에 들어간 후 사용해주세요')
                        return
                    else:
                        None
                    await message.author.move_to(v_chn)
                else:
                    None

        else:   #not command message
            None

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
access_token = os.environ["BOT_TOEKN"]
client.run(access_token)
