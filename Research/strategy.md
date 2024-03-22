**#Data strategy:**

**##ASL-Lex Dataset:**

1. Correlation analysis has shown that distances between major, and minor locations, spread, flexion, ulnar rotation, neighborhood density, parameter neighborhood density, and phonotactic probability are informative for models. Calculating these as additional features might increase accuracy. Even without neighborhood density, parameter neighborhood density, and phonotactic probability, phonological complexity seems to contribute to model performance. Hence, one part of the data strategy should probably be defining a subset of features as above and calculating the phonological complexity from these. This could also potentially contribute to distinguishing meaningful "personal signs" and "meaningless" motion data. 

2. Frequency, iconicity, guessability, and sign type are second-level features of the signs that follow their attributes of them. Iconcizity and/or guessability are useful when it comes to a global and family/personal/local data set and the relationship between them. This parameter could help for applications like Sign Work/Remote. 

3. Thumb, Handshape, Location, Selected Fingers, Flexion, Ulnar Rotation, Spread, and Movement: These features can be captured using the accelerometer, gyroscope, and magnetometer sensors present in most smartphones. These sensors can detect the orientation, movement, and spatial positioning of the device, which can be used to infer the handshape, location, and movement characteristics of signs.

Upon discussion Omatola, it is clear that accessibility should be one integral element of the application. Thus, in terms of motion data it is reasonable to limit sensor data to accelerometer and gyroscope for the time being to ensure widespread usability. 

**##Motion Data Feedback Loop:**

1. I will define motion types with a function based on the gyroscope, accelerometer, and orientation (Euler angle) data (stationary, vertical movement, horizontal movement ...). 
2. Even without orientation data (relative angle of the device to earth as a data stream), this type of data can be inferred through complimentary fusion (roll, path, yaw angles) based on XYZ accelerometer and gyroscope data. 
3. With that given, I can train a model that predicts motion types and adds them as a new column in the user's data set. Timestamp, frequency, and duration data (frequency and duration inferred) can give additional context as to what motion type is expected at that time point of the day. That information can be particularly useful for the contextual assistance of the app. 
4. Motion types will be fed into a language model that predicts activity/gesture types. This model should be fine-tuneable, as user feedback should be used to correct/test the model predictions through a feedback loop. The model training should be made almost real-time through Node-RED. 


**##Other Considerations##:**

Time/Duration: A (pre-trained) model can be used to determine the on- and offset of "personal gestures." This data can then be populated with a timestamp. 

Frequency: Frequency can be measured by counting the number of times a particular sign or gesture is performed within a specific time frame, which can be tracked using timestamps or a dedicated counter.

Iconicity and Guessability: These attributes are more abstract and may require additional input from users or contextual information. Users can provide feedback on the iconicity and guessability of signs through dedicated interfaces.

Sign Type: The type of sign can be identified based on the movement characteristics, handshape, and other visual features captured by the smartphone's sensors. Machine learning algorithms can be trained to classify signs into different types based on these features. Based on that the frequency can be counted later on. Frequency can be important when it comes to distinguishing "neurotypical" and "neurodivergent" communication but also the individual user for model training and weight setting. 

Tap on the Screen Only: In this scenario, where only tap data is available, we're limited to capturing information related to the timing and frequency of interactions. We won't have access to motion or image data, so features like hand shape, movement, and location will not be captured directly. However, we can still gather valuable information about the user's interaction patterns and preferences.

Motion or Image Data Only: If we have access to motion or image data but not both, we can capture different aspects of sign language expression. Motion data, captured through the smartphone's sensors, allows us to track movements, handshapes, and spatial positioning. Image data, on the other hand, enables us to analyze visual features, such as handshapes, facial expressions, and body language. Depending on the specific application and available data, we can focus on either motion-based or image-based analysis.

Combination of Motion, Image, and Tap Data: When we have access to all three types of data, we can leverage a comprehensive approach to capture a wide range of sign language features. Motion data provides insights into movement dynamics and spatial gestures, while image data offers detailed visual information about handshapes and facial expressions. Tap data complements these by providing interaction context. By integrating all three sources of data, we can develop more robust models for sign language recognition and interpretation.

Finally, I propose to use a combination of user-feedback and model learning for identifiers. Users can create "personal gestures" along with their intended meaning, and the model will create LemmaID, CDISignBankCategory, and SignBankSemanticField as well as sign type accordingly. That is, the "SignBankEnglishTranslations" will come from the users. However, as the model learns, it may also identify patterns and recognize what the user intends to say, even though the user doesn't. Therefore, our priority data strategy will involve creating labeled data for handshape, location, and movement characteristics of signs based on accelerometer, gyroscope, magnetometer, image, and direct tap data, where a pre-trained large language model takes over the natural language model. My experience is that a neural network needs at least 5 - 10 samples (10 samples, on average consistently produce some precision while sample sizes below often can lead to 0% accuracy or lucky successes) to learn efficiently. 

Field studies and beta testing might help to iteratively narrow down the parameters and build a global (starter) data set, considering that this is a research field to be researched. 

The model can continuously learn and adapt based on user feedback over time. As more data is collected and analyzed, the model can refine its predictions and become more precise in identifying identifiers. In turn, the application can be advanced in terms of "semi-universal sign language," where the application serves as an interpreter for the global dataset context. 

In order to uphold privacy and data security standards, the application should function mostly on a local level with a reduced parameter number. Furthermore, if a large language model is used, it should be fine-tuneable, open-source, and potentially run locally. Thus, a reduced parameter size is crucial, as is a small - large language model in a smaller, computationally doable range. At best, the app can fully run natively, where updates bring an improved model trained on a larger global data set, but where the app itself mostly "overfits" to the particular user and their use cases with compressed model size.