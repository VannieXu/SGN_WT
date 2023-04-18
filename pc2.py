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

df['time'] = round(adata.obs['PC2'],1).to_list()
df_p = df.groupby('time',as_index = False).mean()

plt.plot()
sns.scatterplot(data=df_p, x="time", y='Ttn',label = 'Ttn',s = 5)
sns.regplot(
    data=df_p, x="time", y='Ttn',
    scatter=False, truncate=False, order=3,
)
sns.scatterplot(data=df_p, x="time", y="Lypd1",label = 'Lypd1',s = 5)
sns.regplot(
    data=df_p, x="time", y='Lypd1',
    scatter=False, truncate=False, order=3,
)
sns.scatterplot(data=df_p, x="time", y="Calb2",label = 'Calb2',s = 5)
sns.regplot(
    data=df_p, x="time", y='Calb2',
    scatter=False, truncate=False, order=3,
)
plt.xlabel('PC2')
plt.ylabel('log10(expression)')
