from abaqusGui import *
from kernelAccess import *
import abaqusConstants
from abq_setCurveRefinement.curveRefinementSymbConsts import *

###########################################################################
# Class definition
###########################################################################

class curveRefinementForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):

        self.owner = owner
        AFXForm.__init__(self, owner=owner)
        self.cmd = AFXGuiCommand(self,'setCurveRefinement','abq_setCurveRefinement.curveRefinementUtils',registerQuery=False)
        self.optionsKw = AFXSymConstKeyword(command=self.cmd,name='options',isRequired=True,defaultValue=COARSE.getId())
        self.partsKw =AFXTupleKeyword(command=self.cmd,name='parts',isRequired=True,opts=AFXTUPLE_TYPE_STRING)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        """Return the first dialog to be posted"""
        import abq_setCurveRefinement.curveRefinementDB
        reload(abq_setCurveRefinement.curveRefinementDB)
        self.db = abq_setCurveRefinement.curveRefinementDB.curveRefinementDB(self)
        return self.db

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self):
        mainWindow = getAFXApp().getAFXMainWindow()
        try:
            self.modelName = session.viewports[session.currentViewportName].displayedObject.modelName
        except:
            msg='There is no model database (MDB) \n'\
                'associated with the current viewport.\n'
            showAFXErrorDialog(mainWindow,msg)
            return
        if not mdb.models[self.modelName].parts.keys():
            showAFXErrorDialog(mainWindow,'No parts available in the current model\n')
        else:
            AFXForm.activate(self)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def deactivate(self):
        mainWindow = getAFXApp().getAFXMainWindow()
        AFXForm.deactivate(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def verifyKeywordValues(self):
        mainWindow = getAFXApp().getAFXMainWindow()
        numItems = self.db.list1.getNumItems()

        if numItems == 0:
            showAFXErrorDialog(mainWindow,'No parts available in the current model\n')
            return 0
        Flag=False
        for i in range(numItems):
            if self.db.list1.isItemSelected(i):
                Flag=True
                break
        if Flag == False:
            showAFXErrorDialog(mainWindow,'Please select at least one part.')
            return 0
        return 1