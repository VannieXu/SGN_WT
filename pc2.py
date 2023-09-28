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


gene_dict = {'Axon Guidance (GO:0007411)':'ROBO2,LGI1,SEMA4D,DCC,SEMA3A,NRXN3,CNTN2,EMB,SEMA3F',
'Neuron Projection Guidance (GO:0097485)':'SEMA3D,LRTM2,SEMA4F,BOC,TNR,SLIT2,EPHA3',
'Actin-Based Cell Projection (GO:0098858)':'TENM2,GRXCR2,LRRK2,USH1C,CD302,ESPN,MYO1H,CLRN1',
'Neuron Projection Development (GO:0031175)':'BTG2,RASGRF1,STMN4,BHLHE22,POU4F1,DCLK1'}

for i in gene_dict.keys():
    gene_dict[i] = [x[0] + x[1:].lower() for x in gene_dict[i].split(',')]
