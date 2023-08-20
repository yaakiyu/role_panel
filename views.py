# RolePanel View
import discord


class RolePanelView(discord.ui.View):
    def __init__(self, roles: dict[str, str | int]):
        super().__init__(timeout=None)
        self.roles = roles
        for k, v in roles.items():
            self.add_item(RoleButton(emoji=k, custom_id=str(v)))

    @classmethod
    def hikitugi(cls, content: str) -> "RolePanelView":
        contents = [k.split(":") for k in content.splitlines()]
        return cls({k[0]: k[1].split("@")[1].split(">")[0] for k in contents})


class RoleButton(discord.ui.Button):
    custom_id: str

    async def callback(self, interaction: discord.Interaction):
        try:
            assert isinstance(interaction.user, discord.Member)
            await interaction.user.add_roles(
                discord.Object(int(self.custom_id))
            )
        except discord.Forbidden:
            embed = discord.Embed(description="役職の設定に失敗しました。\nBOTの一番上の役職よりも高い役職をつけようとしてるかも？")
        except discord.HTTPException:
            embed = discord.Embed(description="役職の設定に失敗しました。")
        else:
            embed = discord.Embed(description=f"<&@{self.custom_id}>の役職を付与しました。")
        await interaction.response.send_message(embed=embed, ephemeral=True)
