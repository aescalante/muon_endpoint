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
             'root://eoscms//eos/cms/store/caf/user/battilan/MuonPOG/CosmicTest_MC_CMSSW_733/step3.root' 
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
#process.MessageLogger.cerr.FwkReport.reportEvery = 5
process.MessageLogger.cerr.FwkReport.reportEvery = -1
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
      fileName = cms.string('CMSTree_MC.root') 
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
