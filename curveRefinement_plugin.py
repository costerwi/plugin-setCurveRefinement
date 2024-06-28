from abaqusGui import *

from curveRefinementForm import curveRefinementForm

# Register commands

version = '1.1-2-1'

toolset=getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    object=curveRefinementForm(toolset),
    buttonText='Tools|Set Curve Refinement...',
    messageId=AFXMode.ID_ACTIVATE,
    kernelInitString='import curveRefinementUtils',
    applicableModules=['Part', 'Assembly'],
    version=version,
    author='Dassault Systemes Simulia Corp.',
    description='This plug-in allows the user to set curve refinement'\
                'for different parts in the model',
    helpUrl='https://github.com/costerwi/plugin-setCurveRefinement'
    )

