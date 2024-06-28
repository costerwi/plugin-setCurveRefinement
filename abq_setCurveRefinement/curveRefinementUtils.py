from __future__ import print_function
from abaqus import mdb, session

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setCurveRefinement(options, parts):
    modelName = session.viewports[session.currentViewportName].displayedObject.modelName
    for p in parts:
        mdb.models[modelName].parts[p].setValues(geometryRefinement=options)
    else:
        print('Curve refinement setting has been successfully set for parts '+ \
            str(list(parts))+' in model '+ '"' + str(modelName) + '"')

    # refresh assembly instance, since they disappear
    #
    a = mdb.models[modelName].rootAssembly
    a.regenerate()
