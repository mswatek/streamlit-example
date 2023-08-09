import streamlit as st
import pandas as pd
import numpy as np
from yahoofantasy import Context


ctx = Context()

st.title('fantasy baseball lets goooo')


# Get all baseball leagues I belonged to in 2019
#for league in ctx.get_leagues("mlb", 2023):
#   print("~~~~~~~~ LEAGUE ~~~~~~~~")
#    print(f"{league.id} - {league.name} ({league.league_type})")
#    print()

league = Context().get_leagues("mlb", 2023)[0]

df = pd.DataFrame({'team':[], 'cat':[], 'stat':[]})
df2 = pd.DataFrame({'team':[], 'cat':[], 'stat':[]})
week_18 = league.weeks()[17]
for matchup in week_18.matchups:
    for team1_stat, team2_stat in zip(matchup.team1_stats, matchup.team2_stats):
        df.loc[len(df)] = [matchup.team1.name, team1_stat.display, team1_stat.value]
        df2.loc[len(df2)] = [matchup.team2.name, team2_stat.display, team2_stat.value]

df_combined = pd.concat([df,df2])
df_wide = pd.pivot(df_combined, index='team', columns='cat', values='stat')

cols = ['H/AB', 'R', 'HR', 'RBI', 'SB', 'OBP', 'IP', 'ERA', 'WHIP', 'K', 'QS', 'SV+H']
df_new = df_wide[cols]

st.write(df_wide)
st.write(df_new)
