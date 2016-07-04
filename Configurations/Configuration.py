Job = {
    "Batch"           : True,
    "Analysis"        : "TTbarAnalysis",
    "Fraction"        : 1,
    "MaxEvents"       : 1234567890,
    "OutputDirectory" : "results/"
}

#VBSAnalysis

Processes = {
  # Diboson processes
  "WW"                    : "Input/MC/data15_13TeV.00276262.physics_Main.HIGG5D1.21-3b_Tuple.root",
  "WZ"                    : "Input/MC/data15_13TeV.00276262.physics_Main.HIGG5D1.21-3b_Tuple.root",
  "ZZ"                    : "Input/MC/data15_13TeV.00276262.physics_Main.HIGG5D1.21-3b_Tuple.root",
  

  # Data
  "data_Muons"            : "Input/Data/data15_13TeV.00283780.physics_Main.HIGG5D1.21-3b_Tuple.root"
    }

