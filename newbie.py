import discord

client = discord.Client()

@client.event
async def on_ready(): 
    print(client.user.id) 
    print("뉴비도우미 전용 재인증 신청봇 | Made by : ! 에어#5285")

@client.event
async def on_message(message):  
    if message.content.startswith("/인증"):
        user = message.author
        mention = message.author.mention
        author = message.guild.get_member(message.mentions[0].id)
        if discord.utils.get(user.roles, name="🌼ㆍ뉴비도우미"):
            role = discord.utils.get(message.guild.roles, name="🙋‍♂️ㆍ시민")
            await message.mentions[0].add_roles(role)
            await message.channel.send("> 인증이 정상적으로 처리 되었습니다.\n> 담당 뉴비도우미 : " + str(mention) + "\n> 인증 유저 : <@" + str(message.mentions[0].id) + ">")
        else:
            await message.channel.send("권한이 없습니다. | Made by : ! 에어#5285")

    if message.content.startswith("/삭제"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[4:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("관리자 권한이 없습니다. | Made by : ! 에어#5285")


client.run("토큰")