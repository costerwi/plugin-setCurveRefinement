from abaqusGui import *
from abaqusConstants import EXTRA_COARSE, COARSE, MEDIUM, FINE, EXTRA_FINE

class curveRefinementDB(AFXDataDialog):
    """Define the dialog box appearance and behavior"""

    ID_LAST = AFXDataDialog.ID_LAST + 3
    ID_ALLON, ID_ALLOFF, ID_INV = range(AFXDataDialog.ID_LAST, ID_LAST)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        self.form = form
        AFXDataDialog.__init__(self, form,
            title='Set Curve Refinement',
            actionButtonIds=self.OK|self.APPLY|self.DISMISS,
            opts=DECOR_RESIZE|DIALOG_NORMAL|DIALOG_ACTIONS_SEPARATOR)

        p = FXGroupBox(self, text='Curve Refinement', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        for refinement in EXTRA_COARSE, COARSE, MEDIUM, FINE, EXTRA_FINE:
            FXRadioButton(p,
                text=refinement.name.replace('_', ' ').title(),
                tgt=form.refinementKw,
                sel=refinement.getId(),
                )

        p = FXHorizontalFrame(self, LAYOUT_FILL_X|LAYOUT_SIDE_BOTTOM)
        FXButton(p, text='Select All', tgt=self, sel=self.ID_ALLON)
        FXButton(p, text='Select None', tgt=self, sel=self.ID_ALLOFF)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ALLON, curveRefinementDB.onAllOnSelected)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ALLOFF, curveRefinementDB.onAllOffSelected)

        p = FXGroupBox(self,text='Parts',opts=FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.partsWidget = AFXList(p,
            nvis=6,
            tgt=form.partsKw,
            opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|LIST_EXTENDEDSELECT|HSCROLLING_OFF|FRAME_SUNKEN,
            )

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def populateParts(self):
        "Collect part names for the active model"
        modelName = getCurrentContext().get('modelName', '')
        self.partNames = sorted(mdb.models[modelName].parts.keys())
        self.partsWidget.clearItems()
        for partName in self.partNames:
            self.partsWidget.appendItem(partName)
        self.form.partsKw.setValueToDefault()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):
        registerCurrentContext(self.populateParts)
        AFXDataDialog.show(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):
        unregisterCurrentContext(self.populateParts)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def selectParts(self, partList):
        "Select only the specified list of parts"
        self.form.partsKw.setValueToDefault()
        for i, partName in enumerate(partList):
            # Append to partsKw. The keyword will notify partsWidget
            self.form.partsKw.setValue(i, partName)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onAllOnSelected(self, sender, sel, ptr):
        "Respond to Select All button"
        self.selectParts(self.partNames)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onAllOffSelected(self, sender, sel, ptr):
        "Respond to Select None button"
        self.selectParts([])

