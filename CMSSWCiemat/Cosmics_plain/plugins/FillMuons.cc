#include "CMSSWCiemat/Cosmics_plain/plugins/CMSTreeProducer.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

bool CMSTreeProducer::fillMuons (const edm::Event & ev, const edm::EventSetup & setup) {

      // We need muons
      edm::Handle<std::vector<reco::Muon> > muonCollectionHandler;
      if (!ev.getByLabel(muonTag_, muonCollectionHandler)) {
            edm::LogError("") << ">>> Muon collection does not exist !!!";
            return false;
      }
      unsigned int muonCollectionSize = muonCollectionHandler->size();
      if (muonCollectionSize==0) return true;
 
      int nmu = 0;

      // Loop over muons
      for (unsigned int im=0; im<muonCollectionSize; ++im) {
            const reco::Muon& mu = muonCollectionHandler->at(im);
            reco::MuonRef muRefinPfCandidates(muonCollectionHandler,im);

            // Require at least that the muon is loose

            //if (!mu.isGlobalMuon()) continue;
            //if (!mu.isTrackerMuon()) continue;

            const reco::TrackRef& muref = mu.tunePMuonBestTrack();
            if (muref.isNull()) continue;

//            std::cout << "pt, q, k" << muref->pt() << " " << muref->charge() << " " << muref->charge()/muref->pt() << std::endl;  

            trk1_.k = muref->charge()/muref->pt();
            trk1_.ptErr = muref->ptError();
            trk1_.eta = muref->eta();
            trk1_.phi = muref->phi();

            nmu++;

            htree_["hCMSTree"]->Fill();      

      }

      return true;
}
