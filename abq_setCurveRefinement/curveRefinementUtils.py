from abaqus import *
from abaqusConstants import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setCurveRefinement(options, parts):
    flag = False
    modelName = session.viewports[session.currentViewportName].displayedObject.modelName
    for p in parts:
        mdb.models[modelName].parts[p].setValues(geometryRefinement=options)
        flag = True
    if flag == True:
        print 'Curve refinement setting has been successfully set for parts '+ \
            str(list(parts))+' in model '+ '"' + str(modelName) + '"'

    # refresh assembly instance, since they disappear
    #
    a = mdb.models[modelName].rootAssembly
    a.regenerate()