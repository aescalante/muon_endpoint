#ifndef CMSSWCiemat_CMSTree_H
#define CMSSWCiemat_CMSTree_H

#include "TROOT.h"
#include "TMath.h"
#include <vector>
#include <string>

namespace ciemat {
  /// Global information at generator level

  /// Information on generated particles

  /// Muon information, are sorted by decreasing pt
  class Muon {
    public:
      Float_t k; ///< q/pt [GeV-1]
      Float_t eta; ///< eta
      Float_t phi; ///< phi
      Float_t ptErr; ///< pt error [GeV]

      /// Constructor
      Muon(){};
      /// Destructor
      virtual ~Muon(){};

      ClassDef(Muon,1)
  };

  /// Global event information
  class Event {
    public:
      Int_t runNumber; ///< run number
      Int_t luminosityBlockNumber; ///< luminosity block number
      Int_t eventNumber; ///< event number
      UInt_t nMuons; ///< Number of muons
      Bool_t isMC; ///< True if this is a MC event

      /// Constructor
      Event(){};
      /// Destructor
      virtual ~Event(){};

      /// True if the event is a real data event
      bool IsData() const {return (!isMC);};
      /// True if the event is a MC event
      bool IsMC() const {return (isMC);};

      ClassDef(Event,1)
  };

}
#endif
