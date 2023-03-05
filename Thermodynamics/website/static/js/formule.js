const GAMMA = 1.4
function otto() { return ((1-(1/(Math.pow(compression_ratio.value,(GAMMA-1)))))*100).toFixed(2) }
function otto_rev() { return (Math.pow((1/(1-(compression_ratio.value/100))), 1/(GAMMA-1))).toFixed(2) }
function diesel() { return ((1-((Math.pow(cut_off_ratio.value,GAMMA)-1)/((GAMMA*Math.pow(compression_ratio.value,(GAMMA-1)))*(cut_off_ratio.value-1))))*100).toFixed(2) }
function brayton() { return ((1-(1/(Math.pow(pressure_ratio.value,((GAMMA-1)/GAMMA)))))*100).toFixed(2) }
function brayton_rev() { return (Math.pow((1/(1-(pressure_ratio.value/100))), GAMMA/(GAMMA-1))).toFixed(2)}
function dual() { return ((1-(((Math.pow(cut_off_ratio.value,GAMMA)*pressure_ratio.value)-1)/(Math.pow(compression_ratio.value,(GAMMA-1))*((pressure_ratio.value-1)+(GAMMA*pressure_ratio.value*(cut_off_ratio.value-1))))))*100).toFixed(2) }