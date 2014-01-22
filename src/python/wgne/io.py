import metrics
obs_dic = {'rlut':{'default':'CERES','alternate':'ERBE'},
           'rsut':{'default':'CERES','alternate':'ERBE'},
           'rsds':{'default':'CERES','alternate':'ERBE'},
           'rlus':{'default':'CERES','alternate':'ERBE'},
           'rsus':{'default':'CERES','alternate':'ERBE'},
           'rlutcs':{'default':'CERES','alternate':'ERBE'},
           'rsutcs':{'default':'CERES','alternate':'ERBE'},
           'rsutcre':{'default':'CERES','alternate':'ERBE'},
           'rlutcre':{'default':'CERES','alternate':'ERBE'},
           'pr':{'default':'GPCP','alternate':'TRMM'},
           'prw':{'default':'RSS'},
           'tas':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'psl':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'ua':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'va':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'uas':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'hus':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'vas':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'ta':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'zg':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'tauu':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'tauv':{'default':'ERAINT','ref3':'JRA25','alternate':'rnl_ncep'},
           'tos':{'default':'HadISST'},
           'zos':{'default':'CNES_AVISO_L4'},
           'sos':{'default':'WOA09'},
            }

### ADDED BY PJG
obs_period = {'ERAINT':{'period':'198901-201001'},
              'CERES':{'period': '200003-201206'},
              'GPCP':{'period': '197901-200909'},
              'TRMM':{'period': '200001-200912'},
              'RSS':{'period': '000001-000012'},
              'HadISST':{'period':'198001-200512'},
              'WOA09':  {'period':'177201-200812'},
              'CNES_AVISO_L4':{'period':'199201-200512'},
              'JRA25' : {"period":'000001-000012'},
              'rnl_ncep' : {"period":'000001-000012'},
              'ERBE': {"period":'000001-000012'}
          }


class OBS(metrics.io.base.Base):
    def __init__(self,root,var,reference="default",period="198001-200512"):
         
#       obsname = obs_dic[var][reference]
#       period = obs_period_dic[var][obsname]  ### ADDED BY PJG
        period = obs_period[obs_dic[var][reference]]['period']  ### ADDED BY PJG
#       template = "%s/%s/ac/%s_%s_%%(period)_ac.%%(ext)" % (var,obs_dic[var][reference],var,obs_dic[var][reference])
        template = "%s/%s/ac/%s_pcmdi-metrics_Amon_%s_%%(period)-clim.%%(ext)" % (var,obs_dic[var][reference],var,obs_dic[var][reference])

        metrics.io.base.Base.__init__(self,root,template)
        if var in ['tos','sos','zos']:
            self.realm = 'ocn'
        else:
            self.realm = 'atm'
        self.period = period
        self.ext = "nc"

