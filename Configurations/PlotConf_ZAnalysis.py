config = {
"Luminosity": 1000,
"InputDirectory": "results",

"Histograms" : {
    "invMass"              : {},
    "etmiss"               : {},
    "vxp_z"                : {},
    "pvxp_n"               : {},
    "lep_n"                : {},
    "leadlep_pt"           : {},
    "leadlep_eta"          : {"y_margin" : 0.2},
    "leadlep_E"            : {},
    "leadlep_phi"          : {"y_margin" : 0.6},
    "leadlep_charge"       : {"y_margin" : 0.6},
    "leadlep_type"         : {"y_margin" : 0.5},
    "leadlep_ptconerel30"  : {},
    "leadlep_etconerel20"  : {},
    "leadlep_z0"           : {},
    "leadlep_d0"           : {},
    "traillep_pt"          : {},
    "traillep_eta"         : {"y_margin" : 0.2},
    "traillep_E"           : {},
    "traillep_phi"         : {"y_margin" : 0.6},
    "traillep_charge"      : {"y_margin" : 0.6},
    "traillep_type"        : {"y_margin" : 0.5},
    "traillep_ptconerel30" : {},
    "traillep_etconerel20" : {},
    "traillep_z0"          : {},
    "traillep_d0"          : {},
    "n_jets"               : {},
    "jet_pt"               : {},
    "jet_m"                : {},
    "jet_jvf"              : {"y_margin" : 0.5},
    "jet_eta"              : {"y_margin" : 0.3},
    "jet_MV1"              : {},
},

"Paintables": {
    "Stack": {
        "Order": ["Diboson"], 
        "Processes" : {                
            "Diboson" : {
                "Color"         : "#fa7921",
                "Contributions" : ["WW", "WZ", "ZZ"]},
        }  
    },
    "data" : {
        "Contributions": ["data_Muons"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data"]},

        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]},
    }
},
}
