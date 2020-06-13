import discord
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("작동중")
    game = discord.Game("배룹아 도움말")
    await  client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("배룹아 안녕"):
        await message.channel.send("ㅎㅇ!")
    if message.content.startswith("배룹아 허준상알려줘"):
        await message.channel.send("허준상 님은 카트라이더 고수 트위치 방송 하시는 분이에요! https://www.twitch.tv/eodud0925")
    if message.content.startswith("배룹아 도움말" or "배룹아 명령어"):
        embed = discord.Embed(title="파이썬으로 작동됨", description="이 봇은 파이썬으로 작성되었습니다", color=0x00ff56)
        embed.set_author(name="배룹봇 도움말", url="https://discord.gg/nbVn9wb",
                             icon_url="https://tr.rbxcdn.com/f10b9a970a51b6bbc106d411f83a8845/150/150/AvatarHeadshot/Png")
        embed.set_thumbnail(url="https://tr.rbxcdn.com/f10b9a970a51b6bbc106d411f83a8845/150/150/AvatarHeadshot/Png")
        embed.add_field(name="챗봇 명령", value="크시와 비슷하게 대화를 할수 있습니다!", inline=False)
        embed.add_field(name="시간확인", value="배룹아 현재 시각을 예기하면 현재 시각을 예기 해줘요!", inline=False)
        embed.add_field(name="준비중", value="#배룹이-추가-할것 에서 추가 할것을 얘기해주세요!", inline=False)
        embed.add_field(name="준비중", value="#배룹이-추가-할것 에서 추가 할것을 얘기해주세요!", inline=False)
        embed.set_footer(text="이것은 pyThon과 pyCharm으로 작성되었습니다")
        await  message.channel.send (embed=embed)
    if message.content.startswith("배룹아 현재 시각"):
        clockhour = datetime.datetime.today().hour
        clockminute = datetime.datetime.today().minute
        await message.channel.send("현재시각은 " + str(clockhour) + "시 " + str(clockminute) + "분 입니다!")



client.run("NzE1MzcwNjMxNTI4NTc5MTUy.Xs-oRQ.Z3jf6bUy5buGxNBGnej5CF2mPkk")