#MenuTitle: Re-compose pixels
"""Looks for decomposed pixels and puts 'pixel' components back in their place."""

pixelGlyphName = "pixel"

import GlyphsApp

Doc  = Glyphs.currentDocument
Font = Glyphs.font
FontMaster = Doc.selectedFontMaster()
selectedLayers = Doc.selectedLayers()

def process( thisLayer ):
	for originPoint in set( [ (p.bounds.origin.x, p.bounds.origin.y) for p in thisLayer.paths ] ):
		x, y = originPoint[0], originPoint[1]
		newComponent = GSComponent( pixelGlyphName, NSPoint( x, y ) )
		thisLayer.components.append( newComponent )
		
	countOfPaths = len( thisLayer.paths )
	for x in range( countOfPaths )[::-1]:
		del thisLayer.paths[x]

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Processing", thisGlyph.name
	thisGlyph.undoManager().beginUndoGrouping()
	process( thisLayer )
	thisGlyph.undoManager().endUndoGrouping()

Font.enableUpdateInterface()
