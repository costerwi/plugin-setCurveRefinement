from abaqusGui import *

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
from abq_setCurveRefinement.curveRefinementForm import *

# Register commands

version = '1.1-2'

majorNumber, minorNumber, updateNumber = getAFXApp().getBaseVersionNumbers()
import _abqPluginUtils, os
status = _abqPluginUtils.checkCompatibility('setCurveRefinement', version)
if status:
    toolset=getAFXApp().getAFXMainWindow().getPluginToolset()
    toolset.registerGuiMenuButton(
        object=curveRefinementForm(toolset),
        buttonText='Tools|Set Curve Refinement...',
        messageId=AFXMode.ID_ACTIVATE,
        kernelInitString='import abq_setCurveRefinement.curveRefinementUtils\n'
                         'from abq_setCurveRefinement.curveRefinementSymbConsts import *',
        applicableModules=['Part', 'Assembly'],
        version=version,
        author='Dassault Systemes Simulia Corp.',
        description='This plug-in allows the user to set curve refinement'\
                    'for different parts in the model',
        helpUrl='https://support.3ds.com/knowledge-base/?q=docid:QA00000008230'
        )
else:
    getAFXApp().getAFXMainWindow().writeToMessageArea(status)
    getAFXApp().beep()

