import ROOT

import Analysis
import AnalysisHelpers as AH
import Constants

#======================================================================

class ZAnalysis(Analysis.Analysis):
  """Analysis searching for events where Z bosons decay to two leptons of same flavour and opposite charge.
  """
  def __init__(self, store):
    super(ZAnalysis, self).__init__(store)
  
  def initialize(self):
      self.invMass              =  self.addStandardHistogram("invMass")

      self.hist_njets           =  self.addStandardHistogram("n_jets")       
      self.hist_jetspt          =  self.addStandardHistogram("jet_pt")       
      self.hist_jetm            =  self.addStandardHistogram("jet_m")      
      self.hist_jeteta          =  self.addStandardHistogram("jet_eta")      
      self.hist_jetphi          =  self.addStandardHistogram("jet_phi")      

      self.hist_etmiss          = self.addStandardHistogram("etmiss")

  
  def analyze(self):
      # retrieving objects
      eventinfo = self.Store.getEventInfo()
      weight = 1 #set to 1
      self.countEvent("no cut", weight)
      
      # apply standard event based selection
      #if not AH.StandardEventCuts(eventinfo): return False
      self.countEvent("EventCuts", weight)

      # Lepton Requirements
      #GoodLeptons = AH.selectAndSortContainer(self.Store.getLeptons(), AH.isGoodLepton, lambda p: p.pt())
      #if not (len(GoodLeptons) == 2): return False
      self.countEvent("2 high pt Leptons", weight)


      # Missing Et Histograms
      etmiss    = self.Store.getEtMiss()
      self.hist_etmiss.Fill(etmiss.et(),weight)

      # Jet Histograms
      jet    = self.Store.getJets()
      self.hist_jetspt.Fill(jet.pt(), weight)
      self.hist_jeteta.Fill(jet.eta(), weight)
      self.hist_jetphi.Fill(jet.phi(), weight)
      
      return True
  
  def finalize(self):
      pass
