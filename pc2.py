from numpy.lib.stride_tricks import sliding_window_view

x = sliding_window_view(df['time'], window_shape = 80)[::70].mean(axis = 1)
y = sliding_window_view(df['Calb2'], window_shape = 80)[::70].mean(axis = 1)

df_p = pd.DataFrame(sliding_window_view(df['time'], window_shape = 20)[::15].mean(axis =1))
df_p.columns = ['pc2']

df_p['Calb2'] = sliding_window_view(df['Calb2'], window_shape = 20)[::15].mean(axis =1)

g_ = 'B3gat1'
df_p[g_] = sliding_window_view(df[g_], window_shape = 20)[::15].mean(axis =1)

sns.scatterplot(data=df_p, x="pc2", y="Calb2",label = 'Calb2',s = 5)
sns.regplot(
    data=df_p, x="pc2", y="Calb2",
    scatter=False, truncate=False, order=3,
)
sns.scatterplot(data=df_p, x="pc2", y=g_,label = g_,s = 5)
sns.regplot(
    data=df_p, x="pc2", y=g_,
    scatter=False, truncate=False, order=3,
)
