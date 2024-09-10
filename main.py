# def for take top n player   
def limit(n,dicty):
    ct=0
    Top = {}
    for i in dicty:
        ct += 1
        if ct<n+1:
            Top[i]=dicty[i]
        else:
            break
    return Top


# batsman selection 
def batsman():
    import csv
    
    with open("ipl-stats.csv", "r") as ipl:
        csvreader=csv.DictReader(ipl)
        batsman_runs={}
        for ball in csvreader:
            if ball["batsman"] in batsman_runs:
                batsman_runs[ball["batsman"]] += int(ball["batsman_runs"])
            else:
                batsman_runs[ball["batsman"]] = int(ball["batsman_runs"])
                
    with open("ipl-stats.csv","r") as ipl:
        csvreader=csv.DictReader(ipl)
        balls_faced={}
        for ball in csvreader:
            if (ball["extras_type"] != "wides"):
                if ball["batsman"] in balls_faced:
                    balls_faced[ball["batsman"]] += 1
                else:
                    balls_faced[ball["batsman"]] = 1
    
    strike_rate={}
    for i in batsman_runs:
        strike_rate[i]=(batsman_runs[i] / balls_faced[i]) * 100
        
        
    strike_rate= dict(sorted(strike_rate.items(),key=lambda x:float(x[1]),reverse=True))
    batsman_runs= dict(sorted(batsman_runs.items(),key=lambda x:float(x[1]),reverse=True))


    # best batsmans
    best={}
    for i in strike_rate:
        if i in batsman_runs:
            best[i] = (strike_rate[i] * batsman_runs[i])
    best= dict(sorted(best.items(),key=lambda x:float(x[1]),reverse=True))
    return best
    def bowlers():
    	import csv
    
    	# runs given by bowlers
    	with open("ipl-stats.csv") as stats_ipl:
		stats = csv.DictReader(stats_ipl)
       		b_runs = {}
        for row in stats:
            if row["bowler"] not in b_runs.keys():
                b_runs[row["bowler"]] = int(row["total_runs"])
            else:
                b_runs[row["bowler"]] += int(row["total_runs"])
                
    
    # balls by bowlers
    with open("ipl-stats.csv") as stats_ipl:
        stats = csv.DictReader(stats_ipl)
        b_balls = {}
        for row in stats:
            balls = 0
            if row["extras_type"] != 'wides' and row["extras_type"] != 'noballs':
                if row["bowler"] not in b_balls.keys():
                    b_balls[row["bowler"]] = 1
                else:
                    b_balls[row["bowler"]] += 1
                        
    
    # wickets taken by bowlers
    with open("ipl-stats.csv") as stats_ipl:
        stats = csv.DictReader(stats_ipl)
        b_wickets = {}
        wicket_type=('bowled','caught','caught and bowled','hit wicket', 'lbw','stumped')
        for row in stats:
            if row["dismissal_kind"] in wicket_type:
                if row["bowler"] not in b_wickets.keys():
                    b_wickets[row["bowler"]] = 1
                
                else:
                    b_wickets[row["bowler"]] +=1
    b_wickets= dict(sorted(b_wickets.items(),key=lambda x:float(x[1]),reverse=True))
                      
    
                        
    # economy rate of bowlers
    bowlers_eco = {}
    for i in b_runs.keys():
        if b_balls[i] > 500:
            bowlers_eco[i] =  (b_runs[i]/(b_balls[i]/6)) 
    bowlers_eco=dict(sorted(bowlers_eco.items(),key=lambda x:float(x[1])))


    # eff bowlers

    best={}
    for i in bowlers_eco:
        best[i] = (b_wickets[i] / bowlers_eco[i])
    best=dict(sorted(best.items(),key=lambda x:float(x[1]),reverse=True))

    return best
def wk():
    import csv
    with open("ipl-stats.csv") as ipl:
        stats = csv.DictReader(ipl)
        wk = {}
        for row in stats:
            if row["dismissal_kind"] == "stumped":
                if row["fielder"] in wk:
                    wk[row["fielder"]] += 1
                else:
                    wk[row["fielder"]] = 1

        wk = dict(sorted(wk.items(),key=lambda x:float(x[1]),reverse=True))

    return wk
def all_rounders():
    bt=batsman()
    bw=bowlers()

    bt1= limit(6,bt)
    bw1= limit(6,bw)

    for i in bt1:
        bt.pop(i)
    for i in bw1:
        bw.pop(i)

    best={}
    for i in bt:
        if i in bw:
            best[i] = bt[i] * bw [i]
    best= dict(sorted(best.items(),key=lambda x:float(x[1]),reverse=True))
    return best
def Dream_18():

    bt=[x for x in limit(6,batsman())]
    bw=[x for x in limit(6,bowlers())]
    wt=[x for x in limit(2,wk())]
    ar=[x for x in limit(4,all_rounders())]
    
    players={"Batsman":bt,"Bowlers":bw,"Wicket Keepers":wt,"All Rounders":ar}
    return players
Dream_18()

def reduce(n,player,p):
    for i in range(n,len(p[player])):
        p[player].pop()
    return p

def Dream_11():
    p=Dream_18()
    p=reduce(4,"Batsman",p)
    p=reduce(4,"Bowlers",p)
    p=reduce(1,"Wicket Keepers",p)
    p=reduce(2,"All Rounders",p)
    return p

Dream_11()