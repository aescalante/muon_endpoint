import FWCore.ParameterSet.Config as cms

import sys

## Choose the mode (DATA or MC)
mode="MC"
#mode="DATAMU"

# Process name
process = cms.Process("CMSTree")

# Source, events to process
process.source = cms.Source("PoolSource",
      fileNames = cms.untracked.vstring (
             '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/08F4E8D1-B3D6-E411-AD4F-02163E00F31D.root', 
#             '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/0C03AE04-BECB-E411-B5F3-02163E00EAFF.root',
            '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/10D12712-85D3-E411-AE63-02163E00E9F7.root',
#            '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/20423280-D5D4-E411-9F95-02163E0114B1.root',
#            '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/307D07EF-12C7-E411-B138-02163E011533.root',
            '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/32462354-F6D3-E411-8BE1-02163E00F1E5.root',
            '/store/data/Commissioning2015/Cosmics/RAW-RECO/CosmicSP-CosmicsSP_07Feb2015-v2/10000/3853245F-F2DB-E411-B489-02163E00EA0D.root'
      ),
      inputCommands = cms.untracked.vstring(
            'keep *',
            'drop *_MEtoEDMConverter_*_*',
            'drop *_lumiProducer_*_*'
      )
)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(40) )

# Log information
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.suppressWarning = cms.untracked.vstring('secondaryVertexTagInfos')
process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 2000
#process.MessageLogger.cerr.FwkReport.reportEvery = -1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


## Geometry and Detector Conditions (needed for a few patTuple production steps)
#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')



### if mode=="MC":
process.load("Configuration.StandardSequences.MagneticField_38T_PostLS1_cff")
process.load('Configuration.StandardSequences.ReconstructionCosmics_cff')

# Define output
process.out = cms.OutputModule("PoolOutputModule"
      , cms.PSet(outputCommands=cms.untracked.vstring('keep *'))
      , dropMetaData = cms.untracked.string("DROPPED")
      , SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('MyPath'))
      , fileName = cms.untracked.string('CMSTree_CosmicAOD.root')
)

# Add appropriate "keep" statements in your output for AOD even if this is PF2PAT
process.out.outputCommands = [ 'keep *', 
                               'drop *_secondaryVertexTagInfos*_*_*',
                               'drop *_impactParameterTagInfos*_*_*',                      
]


# Root tree
process.TFileService = cms.Service("TFileService", 
      fileName = cms.string('CMSTree_cosmic_data.root') 
)

# Selector and parameters
process.CMSTREE = cms.EDFilter("CMSTreeProducer",
      # Input collections
      MuonTag = cms.untracked.InputTag("muons"),
      GenTag = cms.untracked.InputTag("prunedGenParticles"),
      PileupTag = cms.untracked.InputTag("addPileupInfo"),
)

# Paths
if mode=="MC": # do not filter, prune generator information
      process.MyPath = cms.Path( 
            process.CMSTREE 
      )
else: # just leptons
      process.MyPath = cms.Path( 
            process.CMSTREE 
      )

# End path (uncomment only if you want to write out a pat-tuple)
#process.outpath = cms.EndPath(process.out)
