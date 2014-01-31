(define (script-fu-simple-drop-shadow image
                                      drawable
                                      shadow-x
                                      shadow-y
                                      shadow-color
                                      shadow-opacity)
  (let* ((shadow-opacity (max (min shadow-opacity 100) 0))
	 (old-bg (car (gimp-palette-get-background)))
	 (shadow-layer 0))

  (gimp-undo-push-group-start image)

  ; Create new layer and add to the image
  (set! shadow-layer (car (gimp-layer-copy drawable 1)))
  (gimp-image-add-layer image shadow-layer -1)
  (gimp-layer-set-name shadow-layer "Shadow")

  ; Copy layer, lower it below the original, translate, select opacity
  (gimp-image-lower-layer image shadow-layer)
  (gimp-layer-translate shadow-layer shadow-x shadow-y)
  (gimp-layer-set-opacity shadow-layer shadow-opacity)

  ; Fill with shadow color, but keep transparency.
  (gimp-layer-set-preserve-trans shadow-layer 1)
  (gimp-palette-set-background shadow-color)
  (gimp-edit-fill shadow-layer 1)
  
  ; Cleanup
  (gimp-palette-set-background old-bg)
  (gimp-image-set-active-layer image drawable)
  (gimp-undo-push-group-end image)
  (gimp-displays-flush)))

(script-fu-register "script-fu-simple-drop-shadow"
		    _"<Image>/Script-Fu/Shadow/Drop-Shadow (simple)..."
		    "Add a simple drop-shadow of the alpha-channel"
		    "Simon Budig <simon@gimp.org>"
		    "Simon Budig"
		    "2001/4/2"
		    "RGBA GRAYA"
		    SF-IMAGE "Image" 0
		    SF-DRAWABLE "Drawable" 0
		    SF-ADJUSTMENT _"Offset X" '(8 -4096 4096 1 10 0 1)
		    SF-ADJUSTMENT _"Offset Y" '(8 -4096 4096 1 10 0 1)
		    SF-COLOR      _"Color" '(0 0 0)
		    SF-ADJUSTMENT _"Opacity" '(75 0 100 1 10 0 0))
