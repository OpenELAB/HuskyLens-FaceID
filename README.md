# summarize
## Face Recognition Execution Actions Based on HuskyLens Erha Literacy Map

![image](https://github.com/user-attachments/assets/bbcac29d-61a0-4449-b8e4-802ab2219394)  

## Things used in this project

1. Raspiberry Pi 4b

2. Two SG90 180 degree servos

3. SKU SEN0305 Gravity HUSKYLENS Artificial Intelligence Camera

## old practice

HuskyLens Erha Literacy is an easy-to-use AI vision sensor with 7 built-in functions: face recognition, object tracking, object recognition, patrol line tracking, color recognition, label recognition, and object classification. AI training can be completed with just one button, getting rid of tedious training and complex visual algorithms, allowing you to focus more on the conception and realization of your project.  
HuskyLens on-board UART / I2C interface, can be connected to Arduino, LattePanda, micro:bit and other mainstream controllers, to achieve seamless hardware.HuskyLens directly output recognition results to the controller, you do not need to toss the complex algorithms, you can make very creative projects.

## Materials we need to make this program  

1. breadboard 

2. Male to Male Patch Cords  

## wiring diagram  

pin = 5
![image](https://github.com/user-attachments/assets/df503f5a-dc7c-4d03-a8d5-83a25c7e8dd5)  

# concrete step  

## Recognize individual faces  

This function can detect any face profile; recognize and track the learned face and send the message through the serial port, the default setting is to learn and recognize a single face.   

## Operation Settings
Toggle the "Function Button" to the left until "Face Recognition" is displayed at the top of the screen.  

![20241007-133952](https://github.com/user-attachments/assets/a2053f66-62ce-4e63-866d-4e5ff840afc4)

## Learning and Recognition  

1. Face Detection  
2. Aim the HuskyLens at an area with faces, and the screen will automatically frame all the detected faces with a white box, and display the word "Face" respectively.  
3. If the "+" in the center of the screen is not aligned with any face frame at this time, the RGB light on the other side will not light up.  
![20241007-114345](https://github.com/user-attachments/assets/c1626f97-f7bb-49cb-ba92-48b0db50d8f7)  
4. If the "+" in the center of the screen is aligned within any face frame at this time, the RGB light on the other side will light up blue.  
![20241007-114636](https://github.com/user-attachments/assets/21beacd0-79ce-494b-9319-d9f310597c54)  

Tip:  
6. If you need to have the HuskyLens learn or recognize your face, i.e., take a selfie, and you can't see the screen at this point, then you can determine the status based on the different colors of the RGB indicators.  
7. Learning faces  
8. Aim the "+" in the center of the HuskyLens screen at the face to be learned, and press the "Learn Button" briefly to complete the learning. If the same face is recognized, a blue box will appear on the screen and display "Face: ID1". This indicates that face recognition is now possible.  
![image](https://github.com/user-attachments/assets/bb135796-e733-4171-8215-20f7497f9eab)
9. However, the above operation only allows HuskyLens to learn one angle (dimension) of the face, but in reality the face is three-dimensional, so there are multiple angles of the face. If the angle of the face changes, for example, a front face is replaced by a side face, then HuskyLens may not be able to recognize it. To solve this problem, HuskyLens has a built-in continuous learning function that can record all angles of the face, so that the more HuskyLens learns, the more accurate it becomes.  
10. How to record faces from different angles is as follows: (Note: Before you start to learn a new face, you need to let HuskyLens forget the face you have already learned. (Note: Before you start to learn a new face, you need to let HuskyLens forget the face you have already learned, please refer to the chapter of "Forgetting Learned Faces" for the operation method.) 
11. Aim the "+" in the center of the HuskyLens screen at the face that needs to be learned, and long press the "Learn button" without releasing it, at this time the screen will display a yellow box on the face and mark "Face:ID1 At this time, the screen will display a yellow box on the face and mark "Face:ID1", indicating that HuskyLens is learning the face. Then, the yellow box in the center of the HuskyLens screen will be aligned with different angles of the same person's face, such as the front face, side face (it can also be the same person's multiple photographs), and record the various angles of the face. The RGB light is yellow during the learning process. 
![img_v3_02fe_ab74b309-3333-48ec-8e12-1dc0741bd4bg](https://github.com/user-attachments/assets/7423f070-8223-466f-bfa8-b207719a97f5)
12. Then, release the "Learn Button" to end the learning. If HuskyLens recognizes a learned face, the face will be selected by the blue box on the screen and "Face: ID1" will be displayed.  
13. Tip: If there is no "+" in the center of the screen, it means that HuskyLens has already learned under this function (Learned Status). If you want HuskyLens to learn a new face, you need to make HuskyLens forget the learned face first.  
14. face recognition  
15. The face information learned by HuskyLens will be saved automatically. Later, when HuskyLens detects a learned face, it will select the face with a blue box and identify it as "Face:ID1", the size of the border will change with the size of the face, and automatically track the face. At this time, the RGB indicator is green.  
![image](https://github.com/user-attachments/assets/0d8cf33e-40a2-495d-be6a-e7cf5e3fab85)


16. Forgot to learn the human face  
17. If there is no "+" in the center of the screen, it means that the HuskyLens has already learned under this function (learned state). If you want HuskyLens to learn a new face, you need to delete the information of the previously learned face, that is, to make HuskyLens forget the learned face.  
18. Deleting something you have learned is done as follows:  
19. In the current function, press the "Learn button" briefly and the screen prompts "Press again to forget!". before the end of the countdown. Before the end of the countdown, press the "Learn Button" again, you can delete what you learned last time, and the screen displays "+" in the center of the screen, indicating that HuskyLens is ready to learn something new. If you accidentally short press the "Learn button", the screen has prompted "Press again to forget!" If you accidentally short press the "Learn button", the screen has prompted "Press again to forget!", but you don't want to delete what you've learned, then don't do anything until the countdown is over.  
![img_v3_02fe_a68d8f19-fa4b-409e-bae3-e95956be312g](https://github.com/user-attachments/assets/d8ea337d-bd4a-4879-9574-f548e4da07a0)  
Note: The procedure for making HuskyLens forget what it has learned is exactly the same with other features, and will not be repeated subsequently.

## Recognize multiple faces
The default setting is to learn and recognize a single face. If you want to learn and recognize multiple faces, you need to turn on the "Learn Multiple" option in the parameter settings of the secondary menu of the Face Recognition function.  
### The default setting is to learn and recognize a single face. If you want to learn and recognize multiple faces, you need to turn on the "Learn Multiple" option in the parameter settings of the secondary menu of the Face Recognition function.
Toggle the "Function Button" to the left to display "Face Recognition" at the top of the screen.  
1. Press and hold the "Function Button" to enter the second level menu parameter setting interface of the face recognition function.  
2. Toggle the "Function button" to the left or right, select "Learn more than one", then press the "Function button" briefly, then toggle the "Function button" to the right. Then press the "Function Button" briefly, then press the "Function Button" to the right to turn on the switch of "Learn Multiple", i.e. the color of the progress bar turns blue, and the square on the progress bar is located on the right side of the progress bar. Confirm the parameter by pressing the "Function button" again.  
3. Toggle the "Function button" to the left, select "Save and return", press the "Function button" briefly, and the screen prompts "Do you want to save the parameter? The screen prompts "Do you want to save the parameter? The default choice is "Confirm", then press "Function Button" briefly to save the parameters and return to face recognition mode automatically.  
### Learning and Recognition
1. Learning multiple faces:  
2. Aim the "+" in the center of the HuskyLens screen at the face you want to learn, and press and hold the "Learn Button" to finish learning the first face (from all angles). After releasing the "learning button", the screen will prompt: "Press the button again to continue! Press another button to finish". If you want to continue learning the next face, press the "Learn Button" briefly before the countdown ends to continue learning the next face. If you don't need to learn another face anymore, just press the "Function button" before the countdown ends, or don't operate any button and wait for the countdown to end.  
3. In this chapter, we need to continue to learn the next face, so press the "Learn Button" briefly before the countdown ends. Then align the "+" in the center of the HuskyLens screen with the next face to be learned, and press and hold the "Learn Button" to finish learning the second face. And so on.  
4. The face IDs labeled by HuskyLens are in the same order as the recorded faces, i.e., the learned faces are labeled as "Face: ID1", "Face: ID2", "Face: ID3" and so on. Face: ID3", and so on, and different face IDs correspond to different border colors. 
5. Tip: If there is no "+" in the center of the screen, it means that HuskyLens has already learned under this function (learned status). If you want HuskyLens to learn a new face, you need to let HuskyLens forget the learned face first. Please refer to the section "Forgetting Learned Faces" for the operation method.
6. Recognize multiple faces:
7. The information of the faces learned by HuskyLens will be saved automatically. Subsequently, when HuskyLens detects the learned faces, it will select these faces with a box and identify the ID, the first learned face is labeled as "Face: ID1", the second learned face is labeled as "Face: ID2", the third learned face is labeled as "Face: ID3", and so on. The third learned face is labeled as "Face: ID3", and so on. Different face IDs correspond to different border colors, and the size of the border will change with the size of the face, and automatically track the face.  
![img_v3_02fe_f487fa28-5537-4b5b-9c96-e44dd920332g](https://github.com/user-attachments/assets/886c1760-5007-4f0c-a8ee-7a09ad2f247f)
## Experimental Phenomena
https://github.com/user-attachments/assets/ca646a3d-14b9-4742-b308-6583ad8a0ba0  

## How to contact the maintainer or developer
__OpenELAB:__   
[![OpenELAB_logo_resized_150](https://github.com/user-attachments/assets/5d3de375-359c-46a3-96bb-aaa211c6c636)](https://openelab.io)  
__YouTube:__  
[![youtube_logo_200x150](https://github.com/user-attachments/assets/d2365e7f-4ffe-4124-bf62-21eba19a71e4)](https://www.youtube.com/@OpenELAB)  
__X :__  
[![X_logo_150x150](https://github.com/user-attachments/assets/4ad5095f-2573-4791-9360-b355530093bf)](https://twitter.com/openelabio)  
__FaceBook:__  
[![facebook_logo_cropped_150x150](https://github.com/user-attachments/assets/52f2dc9a-a564-49a5-b72e-30eafbbc281f)](https://www.facebook.com/profile.php?id=61559154729457)  
__Discord__  
[![resized_image_150x150](https://github.com/user-attachments/assets/93ecd098-3391-45bb-9d80-b166c197a475)](https://discord.gg/VQspWyck)  

## Material Purchase Links
[HuskyLens AI](https://openelab.io/products/huskylens-ai-camera?_pos=1&_psq=HuskyLens&_ss=e&_v=1.0)  
[Raspberry Pi 4 Model B](https://openelab.io/products/raspberry-pi?_pos=3&_sid=e7313cc6c&_ss=r&variant=43457708130502)  
[Servo Motor SG90](https://openelab.io/products/servo-motor-sg90?_pos=1&_sid=228e703ec&_ss=r)
