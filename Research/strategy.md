Statistically significant features based on the chi-square test:
'LemmaID', 'Batch', 'IconicityType', 'LexicalClass', 'SelectedFingers.2.0', 'ThumbPosition.2.0', 'SignType.2.0', 'Movement.2.0', 'MajorLocation.2.0', 'MinorLocation.2.0', 'SignTypeM4.2.0', 'MovementM4.2.0', 'MajorLocationM4.2.0', 'MinorLocationM4.2.0', 'ThumbPositionM6.2.0', 'SignBankAnnotationID', 'SignBankLemmaID', 'SignBankSemanticField', 'InCDI', 'CDISemanticCategory

Statistically significant numerical features based on ANOVA:
'EnglishWF(lg10)', 'SignFrequency(M)', 'SignFrequency(Z)', 'SignFrequency(M-Native)', 'SignFreq(Z-native)', 'SignFrequency(N-Native)', 'SignFrequency(N-Nonnative)', 'SignFreq(Z-Nonnative)', 'Iconicity(M)', 'Iconicity(SD)', 'Iconicity(Z)', 'Iconicity(N)', 'D.Iconicity(M)', 'D.Iconicity(SD)', 'D.Iconicity(N)', 'D.Iconicity(Z)', 'D.Iconicity(M-native)', 'D.Iconicity(SD-native)', 'D.Iconicity(Z-native)', 'D.Iconicity(N-native)', 'GuessConsistency', 'GuessAccuracy', 'Transparency(M)', 'Transparency SD', 'Transparency Z', 'Initialized.2.0', 'Compound.2.0', 'SignOnset(ms)', 'ClipDuration(ms)', 'MarkedHandshape.2.0', 'FlexionChange.2.0', 'Spread.2.0', 'ThumbContact.2.0', 'RepeatedMovement.2.0', 'Contact.2.0', 'UlnarRotation.2.0', 'MarkedHandshapeM2.2.0', 'SpreadM2.2.0', 'UlnarRotationM2.2.0', 'ContactM4.2.0', 'SignType.2.0Frequency', 'MajorLocation.2.0Frequency', 'MinorLocation.2.0Frequency', 'SecondMinorLocation.2.0Frequency', 'Movement.2.0Frequency', 'SelectedFingers.2.0Frequency', 'Flexion.2.0Frequency', 'FlexionChange.2.0Frequency', 'RepeatedMovement.2.0Frequency', 'Contact.2.0Frequency', 'Spread.2.0Frequency', 'SpreadChange.2.0Frequency', 'ThumbContact.2.0Frequency', 'ThumbPosition.2.0Frequency', 'UlnarRotation.2.0Frequency', 'Parameter.Neighborhood.Density.2.0', 'PhonotacticProbability', 'Phonological Complexity', 'SignBankReferenceID', 'bglm_aoa', 'empirical_aoa'

Data strategy: 

1. Detectable by the device: SelectedFingers.2.0, ThumbPosition.2.0, Movement.2.0, MovementM4.2.0, ThumbPositionM6.2.0, Initialized.2.0, ClipDuration(ms), ThumbContact.2.0 (Interpreting whether the contact meets the criteria specified in the coding scheme (e.g., contact with the tip or pad of the thumb touching selected fingers) may require inference), ContactM4.2.0, Contact.2.0, 

2. Inference required: 

Location-related features: MajorLocation.2.0 (inference required?), MinorLocation.2.0,  MajorLocationM4.2.0, MinorLocationM4.2.0, 

Iconcity: Iconicity(M), Iconicity(SD)', 'Iconicity(Z)', 'Iconicity(N)', 'D.Iconicity(M)', 'D.Iconicity(SD)', 'D.Iconicity(N)', 'D.Iconicity(Z)', 'D.Iconicity(M-native)', 'D.Iconicity(SD-native)', 'D.Iconicity(Z-native)', 'D.Iconicity(N-native)', 'GuessConsistency', 'GuessAccuracy', 'Transparency(M)', 'Transparency SD', 'Transparency Z'  (these all require at least partial calculation)



SignTypeM4.2.0, CDISemanticCategory, SignBankLemmaID, SignBankAnnotationID, batch, IconicityType, SignFrequency(M), SignFrequency (Z), SignFrequency(M-Native), SignFreq(Z-native), SignFrequency(N-Native), SignFrequency(N-Nonnative), SignFreq(Z-Nonnative)

 Compound.2.0 (complex sign -> identify sign), SpreadM2.2.0, FlexionChange.2.0, Spread.2.0, RepeatedMovement.2.0 (determining whether the repetition meets the specific criteria outlined in the coding scheme (e.g., exact repetition of path movement, ulnar rotation, or handshape change) may require inference), UlnarRotation.2.0 (Ulnar rotation refers to a specific type of wrist movement where the hand rotates towards the ulnar side (the side of the little finger) of the forearm. While a device like a camera or motion capture system could potentially detect wrist movement, interpreting whether the movement corresponds to ulnar rotation specifically would require analysis.), SpreadM2.2.0, UlnarRotationM2.2.0, SignType.2.0Frequency, MajorLocation.2.0Frequency, MinorLocation.2.0Frequency, SecondMinorLocation.2.0Frequency, Movement.2.0Frequency (movement per se is detectable but whether it meets certain criteria (and counting) may require inference), SelectedFingers.2.0Frequency, Flexion.2.0Frequency', 'FlexionChange.2.0Frequency', 'RepeatedMovement.2.0Frequency', 'Contact.2.0Frequency', 'Spread.2.0Frequency', 'SpreadChange.2.0Frequency', ThumbContact.2.0Frequency', 'ThumbPosition.2.0Frequency', 'UlnarRotation.2.0Frequency', Parameter.Neighborhood.Density.2.0', 'PhonotacticProbability', 'Phonological Complexity', 'SignBankReferenceID, empirical_aoa, bglm_aoa

3. Machine learning classification/user labeling: LexicalClass, SignBankSemanticField, CDISemanticCategory, Compound.2.0 (complex sign -> identify sign)

InCDI? (not found), EnglishWF?, MarkedHandshape.2.0 = what specifically?
MarkedHandshapeM2.2.0 = ? aoa = age of acquisition? 