# 如何安装
在*\hoshino\modules文件夹内，按住shift之后右键文件夹内空的地方，选择 `在此处打开powershell 窗口`，接着在窗口内输入 `git clone https://github.com/wosiwq/arena_route.git` ，最后在 `__bot__.py` 中添加arena_route 即可。

# 如何使用

只有一条命令
**击剑路径 排名**

> 示例：击剑路径 15001

~~空格**很重要**~~ 在这次正则匹配更新之后可以不添加空格

# 注意

此module默认不启用，启用请在群内发送 `启用 击剑路径计算`

想要默认启用，请将第五行的 `enable_on_default=False` 删除

想要回复的消息不at本人，请将21行的 `at_sender=True` 改为 `at_sender=False`