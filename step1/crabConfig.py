from CRABClient.UserUtilities import config
config = config()

massPoint = 200
CTau = 2.0

massPointString = str(int(massPoint))
CTauString = str(CTau).replace('.','p')

unit = ''
CTauForFileTag = CTau
if(CTau < 1.0):
    unit='um'
    CTauForFileTagString = str(int(CTau*1000))
else:
    unit='mm'
    CTauForFileTagString = str(int(CTau))
    
fileTag = 'StopStopbarTo2Dbar2D_M-'+massPointString+'_CTau-'+CTauForFileTagString+unit
fileVersion = '_v2'
fullTag = fileTag+fileVersion
psetName ='GENSIM-M'+massPointString+'ctau'+CTauString+'.py' 

print(fullTag)
print(psetName)

config.General.requestName   = fullTag
config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configuration file
config.JobType.psetName = psetName

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.outputPrimaryDataset = fullTag
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 30
config.Data.totalUnits = 30000
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'CRAB3_MC_'+fullTag

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_BR_SPRACE'
