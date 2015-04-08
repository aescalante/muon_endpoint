#ifndef CMSSWCiemat_Cosmics_plain_plugins_CMSTreeProducer_h
#define CMSSWCiemat_Cosmics_plain_plugins_CMSTreeProducer_h

/////////////////////////////////////////////////////////////////////////////
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CMSTree.h"
#include "TTree.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "CondFormats/AlignmentRecord/interface/GlobalPositionRcd.h"


namespace edm { 
      class LumiReWeighting; 
}
class MagneticField;
class GlobalTrackingGeometry;
class GlobalPositionRcd;

class CMSTreeProducer : public edm::EDFilter {
public:
  CMSTreeProducer (const edm::ParameterSet &);
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void beginJob();
  virtual void endJob();
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
private:

  void initializePileup();
  bool fillMuons(const edm::Event&, const edm::EventSetup&);

  edm::InputTag muonTag_;
  edm::InputTag genTag_;
  edm::InputTag pileupTag_;

  edm::LumiReWeighting* LumiWeights_69300_;
  edm::LumiReWeighting* LumiWeights_73500_;

  const MagneticField* _bField;
  edm::ESHandle<MagneticField> _bFieldHandle;
  edm::ESHandle<GlobalTrackingGeometry> _globTkGeomHandle;
  edm::ESHandle<GlobalPositionRcd> _globPosRcd;

  ciemat::Event event_;
  ciemat::Muon trk1_;

  std::map<std::string,TTree*> htree_;
  bool genBranchesOn_;

  template<class T> static bool PtOrdered(const T& t1, const T& t2){ return (t1.k<t2.k);} 

};
#endif
