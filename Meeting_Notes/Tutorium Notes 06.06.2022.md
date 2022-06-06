# Meeting Notes
**06.06.2022**

---

## Last week's progress
- Implementing k means
- Generating ground truth images
- Implementing dice score

## Questions
- Warum funktioniert unsere Farbraumkonversion für HSV nicht? Umrechnen der Werte stimmt, aber output Bild sieht anders aus als output von der cv2-Funktion
- Graue Pixel im ground truth image: hat das großen Einfluss auf unseren dice score?
- Farbraumkonversion LAB nicht von PIL unterstützt, mit welchem package geht das?

## Plans for next week
- Optimizing k means (make it work for grayscale images)
- Optimizing ground truth images (and dice score)
- Fixing color conversion
- Testing out pre-processing methods
