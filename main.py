from typing import Optional
import discord
import dotenv
import os

dotenv.load_dotenv()


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.typing = False
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = MyClient()

group = discord.app_commands.Group(name="rp")


@group.command(description="新しいパネルを作成し、そのパネルを選択します。")
async def create(
    interaction: discord.Interaction, role: discord.Role,
    color: Optional[str] = None, title: Optional[str] = None
):
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルをコピーします。")
async def copy(interaction: discord.Interaction):
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルを削除します。")
async def delete(interaction: discord.Interaction):
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="パネルに役職を追加します。")
async def add(
    interaction: discord.Interaction, role1: discord.Role, role2: Optional[discord.Role] = None,
    role3: Optional[discord.Role] = None, role4: Optional[discord.Role] = None, role5: Optional[discord.Role] = None,
    role6: Optional[discord.Role] = None, role7: Optional[discord.Role] = None, role8: Optional[discord.Role] = None,
    role9: Optional[discord.Role] = None, role10: Optional[discord.Role] = None, role11: Optional[discord.Role] = None,
    role12: Optional[discord.Role] = None, role13: Optional[discord.Role] = None, role14: Optional[discord.Role] = None,
    role15: Optional[discord.Role] = None, role16: Optional[discord.Role] = None, role17: Optional[discord.Role] = None,
    role18: Optional[discord.Role] = None, role19: Optional[discord.Role] = None, role20: Optional[discord.Role] = None,
    emoji1: Optional[discord.Role] = None, emoji2: Optional[discord.Role] = None,
    emoji3: Optional[discord.Role] = None, emoji4: Optional[discord.Role] = None, emoji5: Optional[discord.Role] = None,
    emoji6: Optional[discord.Role] = None, emoji7: Optional[discord.Role] = None, emoji8: Optional[discord.Role] = None,
    emoji9: Optional[discord.Role] = None, emoji10: Optional[discord.Role] = None, emoji11: Optional[discord.Role] = None,
    emoji12: Optional[discord.Role] = None, emoji13: Optional[discord.Role] = None, emoji14: Optional[discord.Role] = None,
    emoji15: Optional[discord.Role] = None, emoji16: Optional[discord.Role] = None, emoji17: Optional[discord.Role] = None,
    emoji18: Optional[discord.Role] = None, emoji19: Optional[discord.Role] = None, emoji20: Optional[discord.Role] = None,
):
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルのタイトルやカラーを変更します。")
async def edit(interaction: discord.Interaction, color: Optional[str] = None, title: Optional[str] = None):
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
    await interaction.response.send_message("開発中...", ephemeral=True)


@group.command(description="選択したパネルのリアクションをつけ直します。")
async def refresh(interaction: discord.Interaction):
    await interaction.response.send_message("開発中...", ephemeral=True)


client.tree.add_command(group)


@client.tree.context_menu(name="パネル引継ぎ")
async def hikitugi(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message("開発中...", ephemeral=True)


@client.tree.context_menu(name="パネル選択")
async def select(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message("開発中...", ephemeral=True)


client.run(token=os.environ["TOKEN"])