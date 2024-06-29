from abaqusGui import *
from abaqusConstants import COARSE
from curveRefinementDB import curveRefinementDB

class curveRefinementForm(AFXForm):
    """Associate the dialog box with a kernel command and parameters (keywords)"""

    def __init__(self, owner):
        AFXForm.__init__(self, owner)

        cmd = AFXGuiCommand(
                mode=self,
                method='setCurveRefinement',
                objectName='curveRefinementUtils')

        self.refinementKw = AFXSymConstKeyword(
                command=cmd,
                name='refinement',
                isRequired=True,
                defaultValue=COARSE.getId())

        self.partsKw = AFXTupleKeyword(
                command=cmd,
                name='parts',
                isRequired=True,
                opts=AFXTUPLE_TYPE_STRING)


    def getFirstDialog(self):
        """Return the first dialog to be posted"""
        return curveRefinementDB(self)
