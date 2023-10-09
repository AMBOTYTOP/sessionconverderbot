import os
from pyrogram import Client
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    app = Client(
        ":memory:",
        api_id=os.environ.get("API_ID","12227067"),
        api_hash=os.environ.get("API_HASH","b463bedd791aa733ae2297e6520302fe"),
        bot_token=os.environ.get("BOT_TOKEN","5894209648:AAHHD6eCx8rDk-k624MBIC_as86Hh3zVjzQ"),
        plugins=dict(root="modules"),
    )
    app.run()
