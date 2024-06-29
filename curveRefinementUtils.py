from __future__ import print_function
from abaqus import mdb, session

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setCurveRefinement(refinement, parts):
    modelName = session.viewports[session.currentViewportName].displayedObject.modelName
    for p in parts:
        mdb.models[modelName].parts[p].setValues(geometryRefinement=refinement)

    # refresh assembly instance, since they disappear
    #
    a = mdb.models[modelName].rootAssembly
    a.regenerate()
