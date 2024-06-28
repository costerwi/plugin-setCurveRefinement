from abaqusGui import *
from kernelAccess import *
from abq_setCurveRefinement.curveRefinementSymbConsts import *
###########################################################################
# Class definition
###########################################################################

class curveRefinementDB(AFXDataDialog):
    [ID_PART, ID_ALLON, ID_ALLOFF]= range(AFXDataDialog.ID_LAST,AFXDataDialog.ID_LAST+3)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #
        self.form = form
        AFXDataDialog.__init__(self, form, 'Set Curve Refinement',
            0, opts=DECOR_RESIZE|DIALOG_NORMAL|DIALOG_ACTIONS_SEPARATOR)
        self.okBtn = self.appendActionButton(text='OK',tgt=self,sel=self.ID_CLICKED_OK)
        self.applyBtn = self.appendActionButton(text='Apply',tgt=self,sel=self.ID_CLICKED_APPLY)
        self.dismissBtn = self.appendActionButton(text='Dismiss',tgt=self,sel=self.ID_CLICKED_DISMISS)

        self.buttons = []

        hf1 = FXHorizontalFrame(self, LAYOUT_FILL_X,0, 0, 0, 0, 0, 0, 0, 0)
        gb=FXGroupBox(hf1,text='Curve Refinement',opts=FRAME_GROOVE|LAYOUT_FILL_X)
        FXRadioButton(p=gb,text="Extra Coarse",tgt=self.form.optionsKw, sel=EXTRA_COARSE.getId())
        FXRadioButton(p=gb,text="Coarse",tgt=self.form.optionsKw, sel=COARSE.getId())
        FXRadioButton(p=gb,text="Medium",tgt=self.form.optionsKw, sel=MEDIUM.getId())
        FXRadioButton(p=gb,text="Fine",tgt=self.form.optionsKw, sel=FINE.getId())
        FXRadioButton(p=gb,text="Extra Fine",tgt=self.form.optionsKw, sel=EXTRA_FINE.getId())


        hf2 = FXHorizontalFrame(self, LAYOUT_FILL_X|LAYOUT_SIDE_BOTTOM,0, 0, 0, 0, 0, 0, 0, 0)
        w1 = FXButton(p=hf2, text='Set All On',tgt=self,sel=self.ID_ALLON,opts=BUTTON_NORMAL)
        w2 = FXButton(p=hf2, text='Set All Off',tgt=self,sel=self.ID_ALLOFF,opts=BUTTON_NORMAL)

        gb2=FXGroupBox(self,text='Parts',opts=FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.va = AFXVerticalAligner(gb2,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW|LAYOUT_FILL_COLUMN|FRAME_SUNKEN)
        self.list1 = AFXList(self.va, 6, self,self.ID_PART,LAYOUT_FILL_X|LAYOUT_FILL_Y|
                            LIST_EXTENDEDSELECT|HSCROLLING_OFF|FRAME_SUNKEN,w=50,h=200)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_PART,curveRefinementDB.onPartsPicked)
        self.populateParts()


        FXMAPFUNC(self, SEL_COMMAND, self.ID_ALLON,curveRefinementDB.onAllOnSelected)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ALLOFF,curveRefinementDB.onAllOffSelected)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def populateParts(self):
        mainWindow = getAFXApp().getAFXMainWindow()
        if self.list1.getNumItems() > 0:
            self.list1.clearItems()
        try:
            self.modelName = session.viewports[session.currentViewportName].displayedObject.modelName
        except:
            msg='There is no model database (MDB) \n'\
                'associated with the current viewport.\n'
            showAFXErrorDialog(mainWindow,msg)
            return
        self.partNames= mdb.models[self.modelName].parts.keys()
        for partName in self.partNames:
            self.list1.appendItem(partName)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onAllOnSelected(self, sender, sel, ptr):
        numItems = self.list1.getNumItems()
        for i in range(numItems):
            self.list1.selectItem(i)
        self.onPartsPicked(0, 0, 0)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onAllOffSelected(self, sender, sel, ptr):
        numItems = self.list1.getNumItems()
        for i in range(numItems):
            self.list1.deselectItem(i)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onPartsPicked(self,sender,sel,ptr):
        items = ''
        numItems = self.list1.getNumItems()
        for i in range(numItems):
            if self.list1.isItemSelected(i):
                items += self.list1.getItemText(i)
                items += ','
        self.form.partsKw.setValues(items[:-1])

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        unregisterCurrentContext(self.populateParts)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):

        registerCurrentContext(self.populateParts)
        AFXDataDialog.show(self)