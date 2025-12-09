# ==== 必要なモジュールのインポート ====
import discord                     # Discord Botを作るための道具箱を持ってくるコードです。(Discord Botを制作するために必須です。)
from discord.ext import commands   # 上の道具箱からcommandsっていう取り出すコードです。(スラッシュコマンドを実装するのに使います。)
import requests                    # Webからデータを持ってくるのに使うコードです。(天気情報を持ってくるのに使います。)

# ==== ボットの基本設定 ====
TOKEN = ""  # プログラムにDiscord Botの命を宿らせるコードです（⚠️‼️ここのコードは絶対に他人に教えてはいけません。他の人のコードに命が宿ってしまいます；；‼️⚠️）

# intents はBotがどんな情報を読み取るかを設定するコードです。defaultなので基本的な情報だけ読み取るという意味のコードです。
# commands.Botで本体オブジェクトを作っています。後に続くコードで「"/"から始まるコマンドに反応する」というコードになります。
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# ==== スラッシュコマンド（ハイブリッドコマンド）の定義 ====
@bot.hybrid_command(name="tenki", description="福岡県の天気予報を表示します")  #nameにBotを動かしたいコマンドを入力します。 descriptionにはコマンドの説明を入力できるコードです。
async def weather(ctx):
    # 気象庁の天気予報Webデータ(API)を持ってくるコードです。
    url = "ここは調べて入力しよう！"        　#ここに調べた気象庁のWebデータのURLを入力するコードです。
    response = requests.get(url)        # APIに天気のデータを送ってもらうコードです。
    data = response.json()             # 帰ってきたファイル(JSONファイル)をPythonの時点型に変換するコードです。
    # 送ってもらったファイルの、data[0]["timeSeries"][0]["areas"][0]["weathers"][0] という部分に今日の天気が入っているのでその部分を読み込むコードです。
    weather_text = data[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    weather_text = weather_text.replace('　', '')  # ファイルにスペースがある場合があるのでそれを削除するコードです。
    # 最後にデータを集めてメッセージを送るコードです。
    message = f"福岡県の今日の天気は: {weather_text} です。"
    await ctx.send(message)  # 天気予報メッセージを送信

# ==== Botを起動した時のログ ====
@bot.event
async def on_ready():
    """
    Botが起動してDiscordに接続されたときに1度だけ実行される処理。
    """
    print(f"Botログイン完了: {bot.user}")  # ターミナルにBotが正常に起動したことを表示させるためのコードです。
    # スラッシュコマンドが正常に同期されたこと表示させるためのコードです。
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンド同期完了（{len(synced)}個のコマンド）")
    except Exception as e:
        print(f"コマンド同期時にエラー: {e}")

# ==== Botの起動 ====
bot.run(TOKEN)
