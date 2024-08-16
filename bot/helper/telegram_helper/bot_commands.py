from bot import CMD_SUFFIX as i


class _BotCommands:
    def __init__(self):
        self.StartCommand = "start"
        self.MirrorCommand = [f"mirror2{i}", f"m2{i}"]
        self.YtdlCommand = [f"ytdl2{i}", f"y2{i}"]
        self.LeechCommand = [f"leech2{i}", f"l2{i}"]
        self.YtdlLeechCommand = [f"ytdlleech2{i}", f"yl2{i}"]
        self.CloneCommand = [f"clone2{i}", f"c2{i}"]
        self.CountCommand = f"count2{i}"
        self.DeleteCommand = f"del2{i}"
        self.StopAllCommand = [f"stopall2{i}", "stopallbot2"]
        self.ListCommand = f"list2{i}"
        self.SearchCommand = f"search2{i}"
        self.StatusCommand = [f"status2{i}", "statusall2"]
        self.UsersCommand = f"users2{i}"
        self.AuthorizeCommand = f"authorize2{i}"
        self.UnAuthorizeCommand = f"unauthorize2{i}"
        self.AddSudoCommand = f"addsudo2{i}"
        self.RmSudoCommand = f"rmsudo2{i}"
        self.PingCommand = "ping2"
        self.RestartCommand = [f"restart2{i}", "restartall2"]
        self.StatsCommand = [f"stats2{i}", "statsall2"]
        self.HelpCommand = f"help2{i}"
        self.LogCommand = f"log2{i}"
        self.ShellCommand = f"shell2{i}"
        self.EvalCommand = f"eval2{i}"
        self.ExecCommand = f"exec2{i}"
        self.BotSetCommand = f"botsettings2{i}"
        self.UserSetCommand = f"settings2{i}"
        self.SpeedCommand = f"speedtest2{i}"
        self.AddImageCommand = f"addimg2{i}"
        self.ImagesCommand = f"images2{i}"
        self.MediaInfoCommand = f"mediainfo2{i}"
        self.BroadcastCommand = [f"broadcast2{i}", "broadcastall2"]


BotCommands = _BotCommands()
