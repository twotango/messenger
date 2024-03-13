Data strategy: 

Based on column analysis, we can group the columns in frequency, iconizity, movement, handshape, thumb, location, guessability, time/duration, flexion, ulnar rotation, spread, selected fingers, sign type, and identifiers (CDISemanticCategory, LemmaID, SignBankEnglishTranslations, SemanticField...)

Further, we can group thumb, handshape, location, selected fingers, flexion, ulnar rotation, spread, movement, and time/duration as features of the signs. 

Correlation analysis has shown that distances between major, minor location, spread, flexion, ulnar rotation, neighbourhood density, parameter neighboorhood density, and phonotactic probability are informative for models. Calculating these as additional features might increase accuracy. Even without neighbourhood density, parameter neighboorhood density, and phonotactic probability, phonological complexity seems to contribute to model performance. Hence, one part of the data strategy should probably be defining a subset of features as above and calculating the phonological complexity from these. This could also potentially contribute to distinguishing meaningful "personal signs" and "meaningless" motion data. 

Frequency, iconizity, guessability, and sign type are second-level features of the signs that follow the attributes of them. Iconcizity and/or guessability are useful when it comes to a global and family/personal/local data set and the relationship between them. This parameter could help for applications like Sign Work/Remote. 

Thumb, Handshape, Location, Selected Fingers, Flexion, Ulnar Rotation, Spread, and Movement: These features can be captured using the accelerometer, gyroscope, and magnetometer sensors present in most smartphones. These sensors can detect orientation, movement, and spatial positioning of the device, which can be used to infer the handshape, location, and movement characteristics of signs.

Time/Duration: A (pre-trained) model can be used to determine the on- and offset of "personal gestures." This data can then be populated with timestamp. 

Frequency: Frequency can be measured by counting the number of times a particular sign or gesture is performed within a specific time frame, which can be tracked using timestamps or a dedicated counter.

Iconicity and Guessability: These attributes are more abstract and may require additional input from users or contextual information. Users can provide feedback on the iconicity and guessability of signs through dedicated interfaces.

Sign Type: The type of sign can be identified based on the movement characteristics, handshape, and other visual features captured by the smartphone's sensors. Machine learning algorithms can be trained to classify signs into different types based on these features. Based on that the frequency can be counted later on. Frequency can be important when it comes to distinguishing "neurotypical" and "neurodivergent" communication but also the individual user for model training and weight setting. 

Tap on the Screen Only: In this scenario, where only tap data is available, we're limited to capturing information related to the timing and frequency of interactions. We won't have access to motion or image data, so features like handshape, movement, and location will not be captured directly. However, we can still gather valuable information about the user's interaction patterns and preferences.

Motion or Image Data Only: If we have access to motion or image data, but not both, we can capture different aspects of sign language expression. Motion data, captured through the smartphone's sensors, allows us to track movements, handshapes, and spatial positioning. Image data, on the other hand, enables us to analyze visual features, such as handshapes, facial expressions, and body language. Depending on the specific application and available data, we can focus on either motion-based or image-based analysis.

Combination of Motion, Image, and Tap Data: When we have access to all three types of data, we can leverage a comprehensive approach to capture a wide range of sign language features. Motion data provides insights into movement dynamics and spatial gestures, while image data offers detailed visual information about handshapes and facial expressions. Tap data complements these by providing interaction context. By integrating all three sources of data, we can develop more robust models for sign language recognition and interpretation.