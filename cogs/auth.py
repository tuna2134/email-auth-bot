from smtplib import SMTP
import random, string
from email.mime.text import MIMEText
from email.utils import formatdate
from discord.ext import commands

class Email:
    def __init__(self, subject, to, from_, text = None):
        msg = MIMEText(text)
        msg["From"] = from_
        msg["To"] = to
        msg["Date"] = formatdate()
        msg["Subject"] = subject
        self.msg = msg


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.keyword = ""
        
    def randomname(n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)
        
    @commands.Cog.listener()
    async def on_full_ready(self):
        self.smtp = SMTP("smtp.gmail.com", 587)
        self.smtp.starttls()
        self.smtp.login(self.bot.data["address"], self.bot.data["passwd"])
        
    @commands.command()
    async def auth(self, ctx, address):
        if address in self.keyword:
            email = Email("サーバー認証", address, self.bot.data["address"], f"したで記載されているコードを認証で貼り付けてください")
