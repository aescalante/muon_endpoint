#include "CMSSWCiemat/Cosmics_plain/plugins/CMSTreeProducer.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/CommonDetUnit/interface/TrackingGeometry.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "CondFormats/AlignmentRecord/interface/GlobalPositionRcd.h"

CMSTreeProducer::CMSTreeProducer( const edm::ParameterSet & cfg ) :
  // Input collections
  muonTag_(cfg.getUntrackedParameter<edm::InputTag> ("MuonTag", edm::InputTag("muons"))),
  genTag_(cfg.getUntrackedParameter<edm::InputTag> ("GenTag", edm::InputTag("genParticles"))),
  pileupTag_(cfg.getUntrackedParameter<edm::InputTag> ("PileupTag", edm::InputTag("addPileupInfo")))
{
}

void CMSTreeProducer::beginJob() {

      edm::Service<TFileService> fs;
      printf(">>>>>> PATH: %s\n", fs->fullPath().data());
      htree_["hCMSTree"] = fs->make<TTree>("muonsReco","CIEMAT Muon Cosmic Tree");
      genBranchesOn_ = false;
       
       htree_["hCMSTree"]->Branch("trk1",&(trk1_.k),"k/F:eta:phi:ptErr");

      // Initialize pileup here ...
//      initializePileup();

}

void CMSTreeProducer::beginRun(edm::Run const&, edm::EventSetup const& setup){


      // Get magnetic field and tracker geometry for tracking/vertexing calculations
      setup.get<IdealMagneticFieldRecord>().get(_bFieldHandle);
      setup.get<GlobalTrackingGeometryRecord>().get(_globTkGeomHandle);
      setup.get<GlobalPositionRcd>().get(_globPosRcd);

      return;
}

void CMSTreeProducer::endJob() {
}

bool CMSTreeProducer::filter (edm::Event & ev, const edm::EventSetup & setup) {

      if (!fillMuons(ev, setup)) return false;

      return true;
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(CMSTreeProducer);
