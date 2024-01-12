from CRABClient.UserUtilities import config
config = config()

mass = "M-1000"
lifetime = "CTau-30mm"

theTag = "StopStopbarTo2Dbar2D_"+mass+"_"+lifetime+ "_v2"
config.General.requestName = theTag

config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'DIGIRAWHLT.py'
config.JobType.maxMemoryMB = 5000

config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/StopStopbarTo2Dbar2D_M-1000_CTau-30mm_v2/tomei-CRAB3_MC_StopStopbarTo2Dbar2D_M-1000_CTau-30mm_v2-c074f2b82c44eec2875c7b1051c94c93/\
USER'
config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 1
config.Data.publication = True
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = theTag

# These values only make sense for processing data
#    Select input data based on a lumi mask
#config.Data.lumiMask = 'Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#    Select input data based on run-ranges
#config.Data.runRange = '190456-194076'

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_BR_SPRACE'
