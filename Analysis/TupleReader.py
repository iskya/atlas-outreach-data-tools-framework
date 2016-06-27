import ROOT
from array import array

#======================================================================

class TupleReader(object):
    """ This class implements the rules that govern the readout of the ROOT tuples and and provide a caching facility.
    Caching improves the readout by eliminating the need for branch address lookup each time the variable is accessed.
    """

    def __init__(self):
        super(TupleReader, self).__init__()
        self.Tree = None
        
    def initializeTuple(self,tree):
        """The initial setup of the caching is done here. Branches in the TTree may be deactivated using SetBranchStatus to
        increase readout speed. Only necessary branches are activated and their contents are bound to datamembers of the
        tuple reader.
        """
        self.Tree = tree
        self.Tree.SetBranchStatus("*",0)
        
        #EventInfo 
        self.eventInfo_nom_Nominal__eventNumber     = self.activate("i", "eventInfo_nom_Nominal__eventNumber",            1)
        self.eventInfo_nom_Nominal__runNumber       = self.activate("i", "eventInfo_nom_Nominal__runNumber" ,             1)
        self.eventInfo_nom_Nominal__MCEventWeight   = self.activate("f", "eventInfo_nom_Nominal__MCEventWeight",               1)
        self.eventInfo_nom_Nominal__Pileupweight    = self.activate("f", "eventInfo_nom_Nominal__Pileupweight",     1)
        self.eventInfo_nom_Nominal__ZPV             = self.activate("f", "eventInfo_nom_Nominal__ZPV",    1)
        self.EventInfo = EventInfo(self)
        
         
        #EtMissInfo
        self.met_nom_Nominal__met   = self.activate( "f", "met_nom_Nominal__met",  1)
        self.EtMiss = EtMiss(self)
                
                
    def activate(self, vartype,  branchname, maxlength):
        variable = array(vartype,[0]*maxlength)
        self.Tree.SetBranchStatus(branchname,1)
        self.Tree.SetBranchAddress( branchname, variable)   
        return variable
    
    # Used for a quick scan to get the largest value encountered in the tuple
    def GetMaximum(self,branchname):
        self.Tree.SetBranchStatus(branchname,1)
        return int(self.Tree.GetMaximum(branchname))
    
    # Functions to retrieve object collections (Tuplereader is called Store in the analysis code)
    def getEtMiss(self):
        return self.EtMiss
        
    def getEventInfo(self):
        return self.EventInfo
        
    #def getLeptons(self):
        #return self.Leptons[:self.Lep_n[0]]
    
    #def getJets(self):
        #return self.Jets[:self.Jet_n[0]]

#===========================================================

class EtMiss(object):
    """Missing Transverse Momentum Object.
    Missing Transverse Momentum has only two variables, its magnitude (et) and its azimuthal angle (phi).
    It is used as a proxy for all particles that escaped detection (neutrinos and the likes).
    """
    def __init__(self, branches):
        super(EtMiss, self).__init__()
        self.Branches = branches
        self._tlv     = None
    
    def et(self):
      return self.Branches.Met_et[0]*0.001

    """def phi(self):
      return self.Branches.Met_phi[0]"""

    def __str__(self):
        return "MET: et: %4.3f " % (self.et())

#===========================================================

class EventInfo(object):
    """EventInfo class holding information about the event
    Information that can be accessed may either be metadata about the event (eventNumber, runNumber),
    information regarding the weight an event has (eventWeight, scalefactor, mcWeight, primaryVertexPosition) or
    information that may be used for selection purposes (passGRL, hasGoodVertex, numberofVertices, triggeredByElectron, 
    triggeredByMuon)
    """
    def __init__(self, branches):
        super(EventInfo, self).__init__()
        self.Branches = branches

    def eventNumber(self):
      return self.Branches.eventInfo_nom_Nominal__eventNumber[0]

    def runNumber(self):
      return self.Branches.eventInfo_nom_Nominal__runNumber[0]

    def eventWeight(self):
      return self.Branches.eventInfo_nom_Nominal__MCEventWeight[0]*self.Branches.eventInfo_nom_Nominal__Pileupweight[0]*self.Branches.eventInfo_nom_Nominal__ZPV[0]

    #def scalefactor(self):
      #return self.Branches.SF_Ele[0]*self.Branches.SF_Mu[0]*self.Branches.SF_Trigger[0] 

    #def passGRL(self):
      #return self.Branches.passGRL[0]
     
    def mcWeight(self):
      return self.Branches.eventInfo_nom_Nominal__MCEventWeight[0]
    
    #def hasGoodVertex(self):
      #return self.Branches.hasGoodVertex[0]
    
    #def numberOfVertices(self):
      #return self.Branches.pvxp_n[0]

    #def primaryVertexPosition(self):
      #return self.Branches.vxp_z[0]

    #def triggeredByElectron(self):
      #return self.Branches.trigE[0]

    #def triggeredByMuon(self):
      #return self.Branches.trigM[0]

    def __str__(self):
        return "EventInfo: run: %i  event: %i  eventweight: %4.2f" % (self.runNumber(), self.eventNumber(), self.eventWeight())


#===========================================================
