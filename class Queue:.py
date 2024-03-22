def ipl_points_table(sequence_list):
    table = {team: {"wins": 0, "losses": 0, "points": 0} for team in "CSK DC KKR MI PK RR RCB SH".split()}
    for sequence in sequence_list:
        teams = sequence.split(",")
        first_team = teams[0]
        other_teams = teams[1:]
        table[first_team]["wins"] += 1
        for other_team in other_teams:
            table[other_team]["losses"] += 1
    for team, stats in table.items():
        stats["points"] = stats["wins"]
    for team1, stats1 in table.items():
        for team2, stats2 in table.items():
            if stats1["points"] == stats2["points"] and stats1["wins"] == stats2["wins"] and team1 > team2:
                stats1["points"] -= 1
                stats2["points"] += 1
    table = sorted(table.items(), key=lambda x: (-x[1]["points"], x[0]))
    for team, stats in table:
        print(team + ":" + str(stats["wins"]))

sequence_list = [
    "CSK,DC,KKR,MI,PK,RR,RCB,SH",
    "DC,KKR,MI,PK,RR,RCB,SH",
    "KKR,MI,PK,RR,RCB,SH",
    "MI,PK,RR,RCB,SH",
    "PK,RR,RCB,SH",
    "RR,RCB,SH",
    "RCB,SH",
    "SH",
]
ipl_points_table(sequence_list)