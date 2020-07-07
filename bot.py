import discord
import datetime
import os
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    bot_id = client.user.id
    print(str(bot_id) + "으로 연결됨")
    print("작동중")
    game = discord.Game("'배룹아 도움말' 으로 도움말 확인하기")
    await  client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("배룹아 안녕"):
        await message.channel.send("ㅎㅇ!")
    if message.content.startswith("배룹아 허준상알려줘"):
        await message.channel.send("허준상 님은 카트라이더 고수 트위치 방송 하시는 분이에요! https://www.twitch.tv/eodud0925")
    if message.content.startswith("배룹아 도움말"):
        embed = discord.Embed(title="파이썬으로 작동됨", description="이 봇은 파이썬으로 작성되었습니다", color=0x00ff56)
        embed.set_author(name="배룹봇 도움말", url="https://discord.gg/nbVn9wb",
                             icon_url="https://tr.rbxcdn.com/f10b9a970a51b6bbc106d411f83a8845/150/150/AvatarHeadshot/Png")
        embed.set_thumbnail(url="https://tr.rbxcdn.com/f10b9a970a51b6bbc106d411f83a8845/150/150/AvatarHeadshot/Png")
        embed.add_field(name="챗봇 명령", value="크시와 비슷하게 대화를 할수 있습니다!", inline=False)
        embed.add_field(name="시간확인", value="배룹아 현재 시각을 예기하면 현재 시각을 예기 해줘요!", inline=False)
        embed.add_field(name="b!sl", value="배룹봇이 소속돼어 있는 서버들을 예기합니다", inline=False)
        embed.add_field(name="b!초대", value="배룹봇 초대하기", inline=False)
        embed.set_footer(text="이것은 pyThon과 pyCharm으로 작성되었습니다")
        await  message.channel.send (embed=embed)
    if message.content.startswith("배룹아 현재 시각"):
        clockhour = datetime.datetime.today().hour
        clockminute = datetime.datetime.today().minute
        await message.channel.send("현재시각은 " + str(clockhour) + "시 " + str(clockminute) + "분 입니다!")
    if message.content.startswith("b!sl"):
        for server in client.guilds:
            await message.channel.send(server.name)
    if message.content.startswith("b!초대"):
        await  message.channel.send("배룹봇 초대하기 : https://bit.ly/2VTcNs1")
    if message.content.startswith("배룹아 배워"):
        await  message.channel.send("지금은 오류나 버그때문에 작동하지않는 것입니다")
        #file = openpyxl.load_workbook("학습.xlsx")
        #sheet = file.active
        #learn = message.content.split(" ")
        #for i in range(1,51):
        #    if sheet["A" + str(i)].value == "-" or sheet ["A" + str(i)].value == learn[1]:
        #        sheet["A" + str(i)].value = learn[1]
        #        sheet["B" + str(i)].value = learn[2]
        #        await message.channel.send("단어가 성공적으로 저장돼었습니다.")
        #        break
        #file.save("학습.xlsx")
    
        #if message.content.startswith("배룹아"):
        #    file = openpyxl.load_workbook("학습.xlsx")
        #    sheet = file.active
        #    memory = message.content.split(" ")
        #    for i in range(1,51):
        #        if sheet["A"+ str(i)].value == memory[1]:
        #           await  message.channel.send(message.channel, sheet["B" + str(i)].value)
        #           break

client.run('NzE1MzcwNjMxNTI4NTc5MTUy.XwR0cw.jH9URo8QYbsHWxl8QHiYQPL7h8E')
