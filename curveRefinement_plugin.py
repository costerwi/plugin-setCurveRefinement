from abaqusGui import *

from curveRefinementForm import curveRefinementForm

# Register commands

__version__ = '1.2-0'

toolset=getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    object=curveRefinementForm(toolset),
    buttonText='Tools|Set Curve Refinement...',
    messageId=AFXMode.ID_ACTIVATE,
    kernelInitString='import curveRefinementUtils',
    applicableModules=['Part', 'Assembly'],
    version=__version__,
    author='Dassault Systemes Simulia Corp.',
    description='This plug-in allows the user to set curve refinement '\
                'for some or all of the parts in the model',
    helpUrl='https://github.com/costerwi/plugin-setCurveRefinement'
    )
