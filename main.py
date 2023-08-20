from typing import Optional
import discord
from discord import app_commands
import dotenv
import os
import utils
import views

dotenv.load_dotenv()


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.typing = False
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        self.selecting: dict[int, discord.Message] = {}

    async def setup_hook(self):
        print("sync commands...")
        await self.tree.sync()


client = MyClient()


@client.event
async def on_ready():
    print("discord bot 役職パネルTest1 Ready.")


# rpコマンドたち
group = app_commands.Group(name="rp", description="役職パネル関連のコマンドです。")


@group.command(description="パネルを新しく作成します。")
@app_commands.describe(
    role="パネルに最初に追加する役職です。",
    emoji="最初に追加する役職の絵文字です。指定しなければABC絵文字が使用されます。",
    title="パネルのタイトルです。指定しなければ「役職パネル」になります。",
    color="パネルのカラーです。指定しなければ黒になります。"
)
async def create(
    interaction: discord.Interaction, role: discord.Role, emoji: Optional[str] = None,
    color: Optional[str] = None, title: Optional[str] = None
):
    if not isinstance(interaction.channel, discord.TextChannel):
        return await interaction.response.send_message(
            "テキストチャンネルで実行してください！", ephemeral=True
        )

    emoji = emoji or "\U0001f1e6"
    desc = f"{emoji}:{role.mention}"
    cl = utils.get_color(color or "Default")
    if not 0 <= cl <= 16777215:
        return await interaction.response.send_message(
            "色引数のパースに失敗しました。", ephemeral=True
        )

    embed = discord.Embed(
        title=title or "役職パネル", description=desc, color=cl
    )
    embed.set_footer(text="役職パネル")
    await interaction.response.defer()
    view = views.RolePanelView({emoji: role.id})
    try:
        message = await interaction.followup.send(embed=embed, view=view, wait=True)
    except discord.HTTPException:
        return await interaction.followup.send(
            "この絵文字はボタンとして使用できません。\n別の絵文字を指定してください。"
        )
    client.add_view(view, message_id=message.id)

    # パネルを選択
    client.selecting[interaction.user.id] = message


@group.command(description="選択したパネルをコピーします。")
async def copy(interaction: discord.Interaction):
    if interaction.user.id not in client.selecting:
        return await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルを削除します。")
async def delete(interaction: discord.Interaction):
    if interaction.user.id not in client.selecting:
        return await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="パネルに役職を追加します。")
async def add(
    interaction: discord.Interaction, role1: discord.Role, role2: Optional[discord.Role] = None,
    role3: Optional[discord.Role] = None, role4: Optional[discord.Role] = None, role5: Optional[discord.Role] = None,
    role6: Optional[discord.Role] = None, role7: Optional[discord.Role] = None, role8: Optional[discord.Role] = None,
    role9: Optional[discord.Role] = None, role10: Optional[discord.Role] = None,
    emoji1: Optional[discord.Role] = None, emoji2: Optional[discord.Role] = None,
    emoji3: Optional[discord.Role] = None, emoji4: Optional[discord.Role] = None, emoji5: Optional[discord.Role] = None,
    emoji6: Optional[discord.Role] = None, emoji7: Optional[discord.Role] = None, emoji8: Optional[discord.Role] = None,
    emoji9: Optional[discord.Role] = None, emoji10: Optional[discord.Role] = None
):
    if interaction.user.id not in client.selecting:
        return await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルのタイトルやカラーを変更します。")
async def edit(interaction: discord.Interaction, color: Optional[str] = None, title: Optional[str] = None):
    if interaction.user.id not in client.selecting:
        return await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="パネルから役職を削除します。")
async def remove(
    interaction: discord.Interaction, role1: discord.Role, role2: Optional[discord.Role] = None,
    role3: Optional[discord.Role] = None, role4: Optional[discord.Role] = None, role5: Optional[discord.Role] = None,
    role6: Optional[discord.Role] = None, role7: Optional[discord.Role] = None, role8: Optional[discord.Role] = None,
    role9: Optional[discord.Role] = None, role10: Optional[discord.Role] = None, role11: Optional[discord.Role] = None,
    role12: Optional[discord.Role] = None, role13: Optional[discord.Role] = None, role14: Optional[discord.Role] = None,
    role15: Optional[discord.Role] = None, role16: Optional[discord.Role] = None, role17: Optional[discord.Role] = None,
    role18: Optional[discord.Role] = None, role19: Optional[discord.Role] = None, role20: Optional[discord.Role] = None,
):
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="現在選択しているパネルのリンクを返します。")
async def selected(interaction: discord.Interaction):
    if interaction.user.id not in client.selecting:
        await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
        return
    await interaction.response.send_message(
        f"あなたは以下のパネルを選択しています。\n{client.selecting[interaction.user.id].jump_url}", ephemeral=True
    )


@group.command(description="選択したパネルのリアクションをつけ直します。")
async def refresh(interaction: discord.Interaction):
    if interaction.user.id not in client.selecting:
        return await interaction.response.send_message("あなたは現在パネルを選択していません。", ephemeral=True)
    await interaction.response.send_message("開発中...", ephemeral=True)


client.tree.add_command(group)

# メッセージメニューコマンド

@client.tree.context_menu(name="パネル引継ぎ")
async def hikitugi(interaction: discord.Interaction, message: discord.Message):
    if not (message.embeds and message.embeds[0].description):
        return await interaction.response.send_message(
            "これはパネルではないか、パネルのデータが失われています。", ephemeral=True
        )
    if message.author == client.user:
        return await interaction.response.send_message(
            "パネルはこのbotのものなので引き継ぐ必要がありません。", ephemeral=True
        )
    await interaction.response.defer()
    raw_data = message.embeds[0].description.splitlines()
    panel_data = {}
    for item in raw_data:
        if len(item.split(":")) != 2:
            return await interaction.followup.send(
                "正しいパネル形式ではありません。", ephemeral=True
            )
        emoji, role_mention = item.split(":")
        role_id = role_mention.split("&")[1].replace(">", "")
        if not role_id.isdigit():
            return await interaction.followup.send(
                "正しいパネル形式ではありません。", ephemeral=True
            )
        panel_data[emoji] = role_id
    embed = discord.Embed(
        title=message.embeds[0].title,
        description="\n".join(f"{k}:{v}" for k, v in panel_data.items())
    )
    view = views.RolePanelView(panel_data)
    try:
        message = await interaction.followup.send(embed=embed, view=view, wait=True)
    except discord.HTTPException:
        return await interaction.followup.send(
            "絵文字が対応していないなどの理由で役職パネルの引継ぎに失敗しました。"
        )
    client.add_view(view, message_id=message.id)

    # パネルを選択
    client.selecting[interaction.user.id] = message


@client.tree.context_menu(name="パネル選択")
async def select(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.defer()
    if message.author != client.user or not message.embeds or not message.components:
        return await interaction.response.send_message("これは役職パネルではありません。", ephemeral=True)

    client.selecting[interaction.user.id] = message
    await interaction.followup.send(
        f"以下のパネルを選択しました。\n{message.jump_url}", ephemeral=True
    )


# 実際の役職付与はview.pyで行っています。

@client.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type != discord.InteractionType.component:
        return
    if not interaction.data or "custom_id" not in interaction.data:
        return
    button = views.RoleButton(custom_id=interaction.data["custom_id"])
    await button.callbacker(interaction)


client.run(token=os.environ["TOKEN"])
