#!/usr/bin/env python
# -*- coding:utf-8 -*-
    # WTeam: 比赛胜利队伍
    # LTeam: 失败队伍
    # WLoc: 胜利队伍一方所在的为主场或是客场 另外一个文件就是16-17Schedule.csv，也是经过我们加工处理得到的 NBA 在 2016~2017 年的常规赛的比赛安排，其中包括两个字段：
    # Vteam: 访问 / 客场作战队伍
    # Hteam: 主场作战队伍
import pandas as pd
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

# 回归训练时所需要用到的参数变量
# 当每支队伍没有elo等级分时赋予基础的elo等级分
base_elo = 1600
team_elos = {}
team_stats = {}
X = []
y = []
folder = 'D:\pydata\data' # 存放数据的目录
    # 在最开始需要初始化数据，从 T、O 和 M 表格中读入数据，
    # 去除一些无关数据并将这三个表格通过Team属性列进行连接：
def initialize_data(Mstat,Ostat,Tstat):
    new_Mstat =Mstat.drop(['Rk','Arena'], axis=1)
    new_Ostat = Ostat.drop(['Rk','G','MP'], axis=1)
    new_Tstat = Tstat.drop(['Rk','G','MP'], axis=1)
    team_stats1 = pd.merge(new_Mstat,new_Ostat,how='left',on='Team')
    team_stats1 = pd.merge(team_stats1,new_Tstat,how='left',on='Team')
    return team_stats1.set_index('Team',inplace=False,drop=True)

# 获取每支队伍的Elo Score等级分函数，当在开始没有等级分时，
# 将其赋予初始base_elo值：
def get_elo(team):
    try:
        return team_elos[team]
    except:
        # 当最初没有elo时，给每个队伍最初赋值base_elo
        team_elos[team] = base_elo
        return team_elos[team]

# 定义计算每支球队的Elo等级分函数
def calc_elo(win_team, lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)

    rank_diff = winner_rank - loser_rank
    exp = (rank_diff * -1)/400
    odds = 1 / (1 + math.pow(10,exp))
    # 根据rank级别修改K值
    if winner_rank < 2100:
        k = 32
    elif winner_rank >= 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16
    new_winner_rank = round(winner_rank+(k * (1 - odds)))
    new_rank_diff = new_winner_rank - winner_rank
    new_loser_rank = loser_rank - new_rank_diff

    return new_winner_rank, new_loser_rank
# 基于我们初始好的统计数据，及每支队伍的 Elo score 计算结果，
# 建立对应 2015~2016 年常规赛和季后赛中每场比赛的数据集
# （在主客场比赛时，我们认为主场作战的队伍更加有优势一点，因此会给主场作战队伍相应加上 100 等级分）
def build_dataSet(all_data):
    print 'Building data set...'
    X = []
    skip = 0
    for index, row in all_data.iterrows():
        Wteam = row['WTeam']
        Lteam = row['LTeam']

        # 获取最初的elo或是每个队伍最初的elo值
        team1_elo = get_elo(Wteam)
        team2_elo = get_elo(Lteam)

        # 给主场比赛的队伍加上100 的elo值
        if row ['WLoc'] == 'H':
         team1_elo += 100
        else:
         team2_elo += 100
        # 把elo当为评价每个队伍的第一个特征值
        team1_features = [team1_elo]
        team2_features = [team2_elo]
        # 添加我们从basketball reference.com获得的每个队伍的统计信息
        for key, value in team_stats.loc[Wteam].iteritems():
            team1_features.append(value)
        for key, value in team_stats.loc[Lteam].iteritems():
            team2_features.append(value)

        # 将两只队伍的特征值随机的分配在每场数据的左右两侧*******************************************对于X和y没有理解
        # 并将对应的0/1赋值给y
        if random.random() > 0.5:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)

        if skip == 0:
            print('X',X)
            skip = 1
        new_winner_rank, new_loser_rank = calc_elo(Wteam,Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank
    print '+++++'
    print len(np.nan_to_num(X))
    return np.nan_to_num(X),y
def predict_winner(team_1,team_2,model):
    features=[]
    # team1,客场队伍
    features.append(get_elo(team_1))
    for key, value in team_stats.loc[team_1].iteritems():
        features.append(value)
    features.append(get_elo(team_2)+100)
    for key,value in team_stats.loc[team_2].iteritems():
        features.append(value)
    features = np.nan_to_num(features)
    return model.predict_proba([features])
if __name__ == '__main__':
    Mstat = pd.read_csv(folder+'/15-16Miscellaneous_Stat.csv')
    Ostat = pd.read_csv(folder+'/15-16Opponent_Per_Game_Stat.csv')
    Tstat = pd.read_csv(folder+'/15-16Team_Per_Game_Stat.csv')
    team_stats = initialize_data(Mstat,Ostat,Tstat)
    result_data = pd.read_csv(folder+'/2015-2016_result.csv')
    X, y = build_dataSet(result_data)

    # 训练网络模型
    print 'Fitting on %d game samples..' %len(X)
    model = linear_model.LogisticRegression()
    model.fit(X,y)

    # 利用10折交叉验证计算训练正确率
    print 'Doing cross-validation.'
    print cross_val_score(model,X,y,cv = 10,scoring='accuracy',n_jobs=-1).mean()

    # 利用训练的model在16-17年的比赛中进行预测
    print 'Predicting on new schedule..'
    schedule1617 = pd.read_csv(folder+'/16-17Schedule.csv')
    result = []
    for index, row in schedule1617.iterrows():
        team1 = row['Vteam']
        team2 = row['Hteam']
        pred = predict_winner(team1,team2,model)
        prob = pred[0][0]
        if prob > 0.5:
            winner = team1
            loser = team2
            result.append([winner,loser,prob])
        else :
            winner = team2
            loser = team1
            result.append([winner,loser,prob])
    with open(folder+'/16-17Result.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(['win','lose','probability'])
        writer.writerows(result)
        print 'done.'