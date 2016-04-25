import numpy as np
import matplotlib.pyplot as plt

def plot_metrics(reg,mods):

  x=np.linspace(0,len(stdv[reg])-1,len(stdv[reg]))
  y=np.array(stdv[reg])
  labels = mods

  yave=np.mean(y)
  ystd=np.std(y)
  ymin=np.amin(y)
  ymax=np.amax(y)

  test = True

  if test == True:
    plt.ion()

  fig, ax = plt.subplots(figsize=(18,5))

  ax.plot(x,y,'o',c='red')
  ax.set_title('SSTA std. dev. '+reg)
  ax.set_xlabel('Models')
  #ax.set_ylabel('C degree')
  ax.set_ylabel('$^\circ$C') # Print Celcius symbol
  ax.set_xlim([-1.,len(y)-0.5])
  ax.set_ylim([-0.1,2.1])
  ax.grid(True)

  #ax.xaxis.set_ticks(np.arange(0, len(y), 1)) ## Label x-axis as numbers
  plt.xticks(x,labels,rotation='vertical') ## Label x-axis as model names
  ax.yaxis.set_ticks(np.arange(0, 2.5, 0.5))

  ax.plot(-0.5,yave,'x',c='red') # ave
  ax.plot(-0.5,ymin,'+',c='red') # min
  ax.plot(-0.5,ymax,'+',c='red') # max
  ax.errorbar(-0.5,yave,yerr=ystd,ls='solid',color='red') # inter-model std. dev.

  plt.tight_layout()
  plt.show()

  fig.savefig('test_enso_'+reg+'_v0.3.png',dpi=300)
