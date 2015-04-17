from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Cosmics2015_V3'
config.General.workArea = 'Cosmics2015_PROD'
config.General.transferOutputs=True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'Cosmic_data_inter.py'

config.Data.inputDataset = '/Cosmics/Commissioning2015-CosmicSP-CosmicsSP_07Feb2015-v2/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 175
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Cosmics15/cosmics15_CRAFT_238443_239517_json.txt'
config.Data.runRange = '238443-239517'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_ES_CIEMAT'

