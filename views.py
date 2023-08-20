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

    async def callbacker(self, interaction: discord.Interaction):
        if not isinstance(interaction.user, discord.Member):
            return await interaction.response.send_message(
                "サーバーの取得に失敗しました。もう一度ボタンを押してください。"
            )
        huyo = True
        for r in interaction.user.roles:
            if r.id == int(self.custom_id):
                huyo = False
        try:
            if huyo:
                await interaction.user.add_roles(
                    discord.Object(int(self.custom_id))
                )
            else:
                await interaction.user.remove_roles(
                    discord.Object(int(self.custom_id))
                )
        except discord.Forbidden:
            embed = discord.Embed(description="役職の設定に失敗しました。\nBOTの一番上の役職よりも高い役職をつけようとしてるかも？")
        except discord.HTTPException:
            embed = discord.Embed(description="役職が存在しないか、見つかりませんでした。")
        else:
            x = "付与" if huyo else "解除"
            embed = discord.Embed(description=f"<@&{self.custom_id}>の役職を{x}しました。")
        await interaction.response.send_message(embed=embed, ephemeral=True)
